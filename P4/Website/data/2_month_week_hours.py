import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import calendar
import os

# df = pd.read_csv('Collisions_Crashes.csv')
df = pd.read_csv(r'C:\Users\elian\website\data\Master.CSV')

# fixing the data type of 'CRASH DATE' column
df['CRASH DATE'] = pd.to_datetime(df['CRASH DATE'])
df['CRASH TIME'] = pd.to_datetime(df['CRASH TIME'])

# breaking down of the crash date column
df['Month'] = df['CRASH DATE'].dt.month
# df['Month'] = df['Month'].astype(int)
# df['Month'] = df['Month'].apply(lambda x: calendar.month_abbr[x])

df['Year'] = df['CRASH DATE'].dt.year

df['Weekday'] = df['CRASH DATE'].dt.weekday
# df['Weekday'] = df['Weekday'].apply(lambda x: calendar.day_abbr[x])


df['Hour'] = df['CRASH TIME'].dt.hour


# separating data frame in years
def oneYear(year):
    df_year = df[df['CRASH DATE'].dt.year == int(year)]
    return df_year


df_2016 = oneYear(2016)
df_2017 = oneYear(2017)
df_2018 = oneYear(2018)
df_2019 = oneYear(2019)
df_2020 = oneYear(2020)
df_2021 = oneYear(2021)
df_2022 = oneYear(2022)
df_2023 = oneYear(2023)


def month_cre(df_2016, df_2017, df_2018, df_2019, df_2020, df_2021, df_2022):
    # 2016 - Month
    df_Month_2016 = pd.DataFrame(df_2016.Month.value_counts().reset_index().values,
                                 columns=["Months_16", "Accidents_16"])
    df_Month_2016 = df_Month_2016.sort_values(by=['Months_16']).reset_index()
    df_Month_2016 = df_Month_2016.drop(columns=['index'])

    # 2017 - Month
    df_Month_2017 = pd.DataFrame(df_2017.Month.value_counts().reset_index().values,
                                 columns=["Months_17", "Accidents_17"])
    df_Month_2017 = df_Month_2017.sort_values(by=['Months_17']).reset_index()
    df_Month_2017 = df_Month_2017.drop(columns=['index'])

    # 2018 - Month
    df_Month_2018 = pd.DataFrame(df_2018.Month.value_counts().reset_index().values,
                                 columns=["Months_18", "Accidents_18"])
    df_Month_2018 = df_Month_2018.sort_values(by=['Months_18']).reset_index()
    df_Month_2018 = df_Month_2018.drop(columns=['index'])

    # 2019 - Month
    df_Month_2019 = pd.DataFrame(df_2019.Month.value_counts().reset_index().values,
                                 columns=["Months_19", "Accidents_19"])
    df_Month_2019 = df_Month_2019.sort_values(by=['Months_19']).reset_index()
    df_Month_2019 = df_Month_2019.drop(columns=['index'])

    # 2020 - Month
    df_Month_2020 = pd.DataFrame(df_2020.Month.value_counts().reset_index().values,
                                 columns=["Months_20", "Accidents_20"])
    df_Month_2020 = df_Month_2020.sort_values(by=['Months_20']).reset_index()
    df_Month_2020 = df_Month_2020.drop(columns=['index'])

    # 2021 - Month
    df_Month_2021 = pd.DataFrame(df_2021.Month.value_counts().reset_index().values,
                                 columns=["Months_21", "Accidents_21"])
    df_Month_2021 = df_Month_2021.sort_values(by=['Months_21']).reset_index()
    df_Month_2021 = df_Month_2021.drop(columns=['index'])

    # 2022 - Month
    df_Month_2022 = pd.DataFrame(df_2022.Month.value_counts().reset_index().values,
                                 columns=["Months_22", "Accidents_22"])
    df_Month_2022 = df_Month_2022.sort_values(by=['Months_22']).reset_index()
    df_Month_2022 = df_Month_2022.drop(columns=['index'])

    # Append all years - Month
    meses_df = pd.concat(
        [df_Month_2016, df_Month_2017, df_Month_2018, df_Month_2019, df_Month_2020, df_Month_2021, df_Month_2022],
        axis=1)

    return (meses_df)


meses_df = month_cre(df_2016, df_2017, df_2018, df_2019, df_2020, df_2021, df_2022)

meses_df['Months_16'] = meses_df['Months_16'].apply(lambda x: calendar.month_abbr[x])
meses_df['Months_17'] = meses_df['Months_17'].apply(lambda x: calendar.month_abbr[x])
meses_df['Months_18'] = meses_df['Months_18'].apply(lambda x: calendar.month_abbr[x])
meses_df['Months_19'] = meses_df['Months_19'].apply(lambda x: calendar.month_abbr[x])
meses_df['Months_20'] = meses_df['Months_20'].apply(lambda x: calendar.month_abbr[x])
meses_df['Months_21'] = meses_df['Months_21'].apply(lambda x: calendar.month_abbr[x])

meses_df['Accidents_22'] = meses_df['Accidents_22'].fillna(0)
meses_df.iloc[[10], [12]] = 11
meses_df.iloc[[11], [12]] = 12

meses_df['Months_22'] = meses_df['Months_22'].astype(int)

meses_df['Months_22'] = meses_df['Months_22'].apply(lambda x: calendar.month_abbr[x])

# meses_df

if os.path.exists("meses.CSV"):
    os.remove("meses.CSV")
else:
    pass

meses_df.to_csv('meses.CSV', index=False)


def week_cre(df_2016, df_2017, df_2018, df_2019, df_2020, df_2021, df_2022):
    # 2016 - Weekday
    df_Weekday_2016 = pd.DataFrame(df_2016.Weekday.value_counts().reset_index().values,
                                   columns=["Weekday_16", "Accidents_16"])
    df_Weekday_2016 = df_Weekday_2016.sort_values(by=['Weekday_16']).reset_index()
    df_Weekday_2016 = df_Weekday_2016.drop(columns=['index'])

    # 2017 - Weekday
    df_Weekday_2017 = pd.DataFrame(df_2017.Weekday.value_counts().reset_index().values,
                                   columns=["Weekday_17", "Accidents_17"])
    df_Weekday_2017 = df_Weekday_2017.sort_values(by=['Weekday_17']).reset_index()
    df_Weekday_2017 = df_Weekday_2017.drop(columns=['index'])

    # 2018 - Weekday
    df_Weekday_2018 = pd.DataFrame(df_2018.Weekday.value_counts().reset_index().values,
                                   columns=["Weekday_18", "Accidents_18"])
    df_Weekday_2018 = df_Weekday_2018.sort_values(by=['Weekday_18']).reset_index()
    df_Weekday_2018 = df_Weekday_2018.drop(columns=['index'])

    # 2019 - Weekday
    df_Weekday_2019 = pd.DataFrame(df_2019.Weekday.value_counts().reset_index().values,
                                   columns=["Weekday_19", "Accidents_19"])
    df_Weekday_2019 = df_Weekday_2019.sort_values(by=['Weekday_19']).reset_index()
    df_Weekday_2019 = df_Weekday_2019.drop(columns=['index'])

    # 2020 - Weekday
    df_Weekday_2020 = pd.DataFrame(df_2020.Weekday.value_counts().reset_index().values,
                                   columns=["Weekday_20", "Accidents_20"])
    df_Weekday_2020 = df_Weekday_2020.sort_values(by=['Weekday_20']).reset_index()
    df_Weekday_2020 = df_Weekday_2020.drop(columns=['index'])

    # 2021 - Weekday
    df_Weekday_2021 = pd.DataFrame(df_2021.Weekday.value_counts().reset_index().values,
                                   columns=["Weekday_21", "Accidents_21"])
    df_Weekday_2021 = df_Weekday_2021.sort_values(by=['Weekday_21']).reset_index()
    df_Weekday_2021 = df_Weekday_2021.drop(columns=['index'])

    # 2022 - Weekday
    df_Weekday_2022 = pd.DataFrame(df_2022.Weekday.value_counts().reset_index().values,
                                   columns=["Weekday_22", "Accidents_22"])
    df_Weekday_2022 = df_Weekday_2022.sort_values(by=['Weekday_22']).reset_index()
    df_Weekday_2022 = df_Weekday_2022.drop(columns=['index'])

    # Append all years - Month
    weekday_df = pd.concat(
        [df_Weekday_2016, df_Weekday_2017, df_Weekday_2018, df_Weekday_2019, df_Weekday_2020, df_Weekday_2021,
         df_Weekday_2022], axis=1)

    return (weekday_df)


weekdays_df = week_cre(df_2016, df_2017, df_2018, df_2019, df_2020, df_2021, df_2022)
# weekdays_df

if os.path.exists("weekdays.CSV"):
    os.remove("weekdays.CSV")
else:
    pass

weekdays_df['Weekday_16'] = weekdays_df['Weekday_16'].apply(lambda x: calendar.day_abbr[x])
weekdays_df['Weekday_17'] = weekdays_df['Weekday_17'].apply(lambda x: calendar.day_abbr[x])
weekdays_df['Weekday_18'] = weekdays_df['Weekday_18'].apply(lambda x: calendar.day_abbr[x])
weekdays_df['Weekday_19'] = weekdays_df['Weekday_19'].apply(lambda x: calendar.day_abbr[x])
weekdays_df['Weekday_20'] = weekdays_df['Weekday_20'].apply(lambda x: calendar.day_abbr[x])
weekdays_df['Weekday_21'] = weekdays_df['Weekday_21'].apply(lambda x: calendar.day_abbr[x])
weekdays_df['Weekday_22'] = weekdays_df['Weekday_22'].apply(lambda x: calendar.day_abbr[x])

# weekdays_df
weekdays_df.to_csv('weekdays.CSV', index=False)


def hour_cre(df_2016, df_2017, df_2018, df_2019, df_2020, df_2021, df_2022):
    # 2016 - Hour
    df_Hour_2016 = pd.DataFrame(df_2016.Hour.value_counts().reset_index().values, columns=["Hours_16", "Accidents_16"])
    df_Hour_2016 = df_Hour_2016.sort_values(by=['Hours_16']).reset_index()
    df_Hour_2016 = df_Hour_2016.drop(columns=['index'])

    # 2017 - Hour
    df_Hour_2017 = pd.DataFrame(df_2017.Hour.value_counts().reset_index().values, columns=["Hours_17", "Accidents_17"])
    df_Hour_2017 = df_Hour_2017.sort_values(by=['Hours_17']).reset_index()
    df_Hour_2017 = df_Hour_2017.drop(columns=['index'])

    # 2018 - Hour
    df_Hour_2018 = pd.DataFrame(df_2018.Hour.value_counts().reset_index().values, columns=["Hours_18", "Accidents_18"])
    df_Hour_2018 = df_Hour_2018.sort_values(by=['Hours_18']).reset_index()
    df_Hour_2018 = df_Hour_2018.drop(columns=['index'])

    # 2019 - Hour
    df_Hour_2019 = pd.DataFrame(df_2019.Hour.value_counts().reset_index().values, columns=["Hours_19", "Accidents_19"])
    df_Hour_2019 = df_Hour_2019.sort_values(by=['Hours_19']).reset_index()
    df_Hour_2019 = df_Hour_2019.drop(columns=['index'])

    # 2020 - Hour
    df_Hour_2020 = pd.DataFrame(df_2020.Hour.value_counts().reset_index().values, columns=["Hours_20", "Accidents_20"])
    df_Hour_2020 = df_Hour_2020.sort_values(by=['Hours_20']).reset_index()
    df_Hour_2020 = df_Hour_2020.drop(columns=['index'])

    # 2021 - Hour
    df_Hour_2021 = pd.DataFrame(df_2021.Hour.value_counts().reset_index().values, columns=["Hours_21", "Accidents_21"])
    df_Hour_2021 = df_Hour_2021.sort_values(by=['Hours_21']).reset_index()
    df_Hour_2021 = df_Hour_2021.drop(columns=['index'])

    # 2021 - Hour
    df_Hour_2022 = pd.DataFrame(df_2022.Hour.value_counts().reset_index().values, columns=["Hours_22", "Accidents_22"])
    df_Hour_2022 = df_Hour_2022.sort_values(by=['Hours_22']).reset_index()
    df_Hour_2022 = df_Hour_2022.drop(columns=['index'])

    # Append all years - Month
    horas_df = pd.concat(
        [df_Hour_2016, df_Hour_2017, df_Hour_2018, df_Hour_2019, df_Hour_2020, df_Hour_2021, df_Hour_2022], axis=1)

    return (horas_df)


horas_df = hour_cre(df_2016, df_2017, df_2018, df_2019, df_2020, df_2021, df_2022)
# horas_df

if os.path.exists("hours.CSV"):
    os.remove("hours.CSV")
else:
    pass

horas_df.to_csv('hours.CSV', index=False)