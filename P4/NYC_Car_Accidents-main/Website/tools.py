import streamlit as st
import pandas as pd
import numpy as np
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium # pip install streamlit-folium
from streamlit_folium import folium_static
from datetime import date
from dateutil.relativedelta import relativedelta
import calendar

# to run this web: streamlit run app.py
# watch this to prevent the website to refresh: https://youtu.be/nF-PQj0k5-o



# LOAD DATA ONCE
@st.experimental_singleton
def load_data():
    df = pd.read_csv(r'C:\Users\elian\website\data\Master.CSV')
    meses = pd.read_csv(r'C:\Users\elian\website\data\meses.CSV')
    weekdays = pd.read_csv(r'C:\Users\elian\website\data\weekdays.CSV')
    horas = pd.read_csv(r'C:\Users\elian\website\data\hours.CSV')

    df = df[df['LONGITUDE'].notna()]  # dropping na values

    # fixing the data type of 'CRASH DATE' column
    df['CRASH DATE'] = pd.to_datetime(df['CRASH DATE'])
    df['CRASH TIME'] = pd.to_datetime(df['CRASH TIME'])

    # breaking down of the crash date column
    df['Month'] = df['CRASH DATE'].dt.month
    df['Year'] = df['CRASH DATE'].dt.year
    df['Weekday'] = df['CRASH DATE'].dt.weekday
    df['Hour'] = df['CRASH TIME'].dt.hour

    # fixing weekdays and months
    df['Month'] = df['Month'].apply(lambda x: calendar.month_abbr[x])
    df['Weekday'] = df['Weekday'].apply(lambda x: calendar.day_abbr[x])

    # fixing data type of lat and lon
    df['LATITUDE'] = df['LATITUDE'].astype(float)
    df['LONGITUDE'] = df['LONGITUDE'].astype(float)

    df.drop(["OFF STREET NAME", "VEHICLE TYPE CODE 2", "CONTRIBUTING FACTOR VEHICLE 3", "LOCATION", "VEHICLE TYPE CODE 3", "CONTRIBUTING FACTOR VEHICLE 4", "VEHICLE TYPE CODE 4", "CONTRIBUTING FACTOR VEHICLE 5", "VEHICLE TYPE CODE 5"], axis=1, inplace=True)

    heat_df = df.sample(frac=0.0025)

    factors = ['Unspecified', 'Other Vehicular']
    df_factors = df[df['CONTRIBUTING FACTOR VEHICLE 1'].isin(factors) == False]

    return df, heat_df, df_factors , meses, weekdays, horas

def display_markers_map(file, month):
    df = pd.read_csv(file)

    # calculates 6 months ago as of today
    six_months = date.today() - relativedelta(months=+int(month))
    six_months_str = str(six_months)  # turn date into a string

    city_fault = df[df['CRASH DATE'] > six_months_str]

    # Setting the initial top view
    map = folium.Map(location=[40.7765753, -73.830104], zoom_start=11, tiles='CartoDB positron')

    # generating the dataframe with Lat and Long
    for i in range(0, len(city_fault)):
        html = f"""
         <p>Location: {city_fault.iloc[i]['ON STREET NAME']}</p>
         <p>Cross Street: {city_fault.iloc[i]['CROSS STREET NAME']}</p>
         <p>Issue: {city_fault.iloc[i]['CONTRIBUTING FACTOR VEHICLE 1']}</p>
         <p>Report Date: {city_fault.iloc[i]['CRASH DATE']}</p>
        """
        iframe = folium.IFrame(html)
        popup = folium.Popup(iframe, min_width=230, max_width=230)

        if city_fault.iloc[i]['CONTRIBUTING FACTOR VEHICLE 1'] == 'Traffic Control Device Improper/Non-Working':
            folium.Marker(
                location=[city_fault.iloc[i]['LATITUDE'], city_fault.iloc[i]['LONGITUDE']],
                popup=popup,
                icon=folium.Icon(color="red")
            ).add_to(map)

        elif city_fault.iloc[i]['CONTRIBUTING FACTOR VEHICLE 1'] == 'Lane Marking Improper/Inadequate':
            folium.Marker(
                location=[city_fault.iloc[i]['LATITUDE'], city_fault.iloc[i]['LONGITUDE']],
                popup=popup,
                icon=folium.Icon(color="green")
            ).add_to(map)

        elif city_fault.iloc[i]['CONTRIBUTING FACTOR VEHICLE 1'] == 'Pavement Defective':
            folium.Marker(
                location=[city_fault.iloc[i]['LATITUDE'], city_fault.iloc[i]['LONGITUDE']],
                popup=popup,
                icon=folium.Icon(color="blue", icon="fa-solid fa-road", prefix='fa')
            ).add_to(map)

    folium.TileLayer('openstreetmap').add_to(map)

    st_map = folium_static(map, width=700, height=450)


def display_heatmap(df, year):
    df = df[df['Year']==year]

    # Setting the initial top view
    map = folium.Map(location=[40.7765753, -73.830104], zoom_start=11)

    # border styles
    bordersStyle = {
        'color': 'black',
        'weight': 2,
    }
    # Collects the information from the borders locate it in a geojson file
    folium.GeoJson(
        data=(open(r"C:\Users\elian\website\data\borders.geojson").read()),
        name='Borders',
        style_function=lambda x: bordersStyle).add_to(map)

    # generating the dataframe with Lat and Long
    heat_data = [[row['LATITUDE'], row['LONGITUDE']] for index, row in df.iterrows()]

    # Ploting the heat map
    HeatMap(heat_data, name='Heatmap').add_to(map)

    # add borders over the map
    folium.LayerControl().add_to(map)

    st_map = folium_static(map, width=700, height=450)



