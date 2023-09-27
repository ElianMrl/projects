import pandas as pd
from sodapy import Socrata
from datetime import date
from dateutil.relativedelta import relativedelta

data_url='data.cityofnewyork.us'    # The Host Name for the API endpoint (the https:// part will be added automatically)
data_set='h9gi-nx95'    # The data set at the API endpoint (311 data in this case)
app_token='hqQpJzIE0DqD1hXkzCU65bJ3H'   # The app token created in the prior steps
client = Socrata(data_url,app_token)      # Create the client to point to the API endpoint
# Set the timeout to 60 seconds
client.timeout = 60
# Retrieve the first 2000 results returned as JSON object from the API
# The SoDaPy library converts this JSON object to a Python list of dictionaries
results = client.get(data_set, limit=10000)
# Convert the list of dictionaries to a Pandas data frame
data = pd.DataFrame.from_records(results)

import os
if os.path.exists("accidents_API_data.csv"):
    os.remove("accidents_API_data.csv")
else:
    pass

import os
if os.path.exists("city_fault.csv"):
    os.remove("city_fault.csv")
else:
    pass

# fix columns:
data.rename(columns = {'crash_date':'CRASH DATE', 'crash_time':'CRASH TIME',
                     'on_street_name':'ON STREET NAME', 'off_street_name':'OFF STREET NAME',
                     'number_of_persons_injured':'NUMBER OF PERSONS INJURED',
                     'number_of_persons_killed':'NUMBER OF PERSONS KILLED',
                     'number_of_pedestrians_injured':'NUMBER OF PEDESTRIANS INJURED',
                     'number_of_pedestrians_killed':'NUMBER OF PEDESTRIANS KILLED',
                     'number_of_cyclist_injured':'NUMBER OF CYCLIST INJURED',
                     'number_of_cyclist_killed':'NUMBER OF CYCLIST KILLED',
                     'number_of_motorist_injured':'NUMBER OF MOTORIST INJURED',
                     'number_of_motorist_killed':'NUMBER OF MOTORIST KILLED',
                     'contributing_factor_vehicle_1':'CONTRIBUTING FACTOR VEHICLE 1',
                     'contributing_factor_vehicle_2':'CONTRIBUTING FACTOR VEHICLE 2',
                     'collision_id':'COLLISION_ID', 'vehicle_type_code1':'VEHICLE TYPE CODE 1',
                     'vehicle_type_code2':'VEHICLE TYPE CODE 2', 'borough':'BOROUGH',
                     'zip_code':'ZIP CODE', 'latitude':'LATITUDE', 'longitude':'LONGITUDE',
                     'location':'LOCATION', 'cross_street_name':'CROSS STREET NAME',
                     'contributing_factor_vehicle_3':'CONTRIBUTING FACTOR VEHICLE 3',
                     'vehicle_type_code_3':'VEHICLE TYPE CODE 3',
                     'contributing_factor_vehicle_4':'CONTRIBUTING FACTOR VEHICLE 4',
                     'vehicle_type_code_4':'VEHICLE TYPE CODE 4',
                     'contributing_factor_vehicle_5':'CONTRIBUTING FACTOR VEHICLE 5',
                     'vehicle_type_code_5':'VEHICLE TYPE CODE 5'
                    }, inplace = True)

# drop null rows
# data = data[data['LONGITUDE'].notna()]

# Save the new data frame to a CSV file
data.to_csv("accidents_API_data.csv")

# append all the data together into a csv file
master_df = pd.DataFrame()

for file in os.listdir(os.getcwd()):
    if file.endswith('.csv'):
        master_df = master_df.append(pd.read_csv(file))

# drop duplicates
master_df.drop_duplicates()

# fixing the data type of 'CRASH DATE' column
master_df['CRASH DATE'] = pd.to_datetime(master_df['CRASH DATE'])
master_df['CRASH TIME'] = pd.to_datetime(master_df['CRASH TIME'])

# breaking down of the crash date column
master_df['Month'] = master_df['CRASH DATE'].dt.month
master_df['Year'] = master_df['CRASH DATE'].dt.year
master_df['Weekday'] = master_df['CRASH DATE'].dt.weekday
master_df['Hour'] = master_df['CRASH TIME'].dt.hour

# # fixing data type of lat and lon
# master_df['LATITUDE'] = master_df['LATITUDE'].astype(float)
# master_df['LONGITUDE'] = master_df['LONGITUDE'].astype(float)

# create file to store all the data
master_df.to_csv('Master.CSV', index=False)

# making city fault

df = master_df.copy()

# remove crashes that does not have lat and long
df = df[df['LONGITUDE'].notna()]

# fixing the data type of 'CRASH DATE' column
df['CRASH DATE'] = pd.to_datetime(df['CRASH DATE'])
df['CRASH TIME'] = pd.to_datetime(df['CRASH TIME'])

# breaking down of the crash date column
df['Month'] = df['CRASH DATE'].dt.month
df['Year'] = df['CRASH DATE'].dt.year
df['Weekday'] = df['CRASH DATE'].dt.weekday
df['Hour'] = df['CRASH TIME'].dt.hour

# drop meaningless factors
factors = ['Unspecified', 'Other Vehicular']
df_factors = df[df['CONTRIBUTING FACTOR VEHICLE 1'].isin(factors) == False]

from datetime import date
from dateutil.relativedelta import relativedelta

# calculates 6 months ago as of today
six_months = date.today() - relativedelta(months=+6)
six_months_str = str(six_months) # turn date into a string

city_fault = df_factors[(df_factors['CONTRIBUTING FACTOR VEHICLE 1'] == 'Traffic Control Device Improper/Non-Working') |
                        (df_factors['CONTRIBUTING FACTOR VEHICLE 1'] == 'Lane Marking Improper/Inadequate') |
                        (df_factors['CONTRIBUTING FACTOR VEHICLE 1'] == 'Pavement Defective')]

# city_fault = city_fault[city_fault['CRASH DATE'] > six_months_str]

# Save the new data frame to a CSV file
city_fault.to_csv("city_fault.csv")