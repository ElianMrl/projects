import plotly.graph_objects as go
import plotly.express as px
from tools import *
import streamlit as st

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout='wide',
    initial_sidebar_state='expanded'
)

header_c = st.container()
line_chart_c = st.container()
barchart_c = st.container()
factors_c = st.container()

# loading data
df, heat, factors, meses_df, weekdays_df, horas_df = load_data()

st.sidebar.subheader('Facts parameter')
year_heatmap = st.sidebar.slider('Select a Year:', min_value=2016, max_value=2022, value=2022, step=1)

with header_c:
    st.title("Car Accidents in New York City 🚘💥🚗")
    # st.text("Analyzing car accidents within New York City")

    co1, co2, co3 = st.columns(3)
    # Adding number of accidents per year
    total1 = len(df[df['CRASH DATE'].dt.year == year_heatmap])
    report = 'Number of Accidents in {}:'.format(year_heatmap)
    with co1:
        st.metric(report, '{:,}'.format(total1))

    # Adding number of death people per year
    df1 = df[df['CRASH DATE'].dt.year == year_heatmap]
    total2 = df1['NUMBER OF PERSONS KILLED'].sum()
    report1 = 'Number of Deaths in {}:'.format(year_heatmap)
    with co2:
        st.metric(report1, '{:,}'.format(int(total2)))

    # Adding number of Injured people per year
    df1 = df[df['CRASH DATE'].dt.year == year_heatmap]
    total3 = df1['NUMBER OF PERSONS INJURED'].sum()
    report2 = 'Number of Injured Victims in {}:'.format(year_heatmap)
    with co3:
        st.metric(report2, '{:,}'.format(int(total3)))

    #style_metric_cards(border_left_color="#1E1E1E")

with line_chart_c:
    col1, line_chart_col = st.columns([0.7,2.3])

    with col1:
        df_Injured = df1[df1.columns[[7, 9, 11]]].sum()

        lista = [df1.columns[7][10:], df1.columns[9][10:], df1.columns[11][10:]]

        data = {'names': [lista[0][:-6], lista[1][:-6], lista[2][:-6]],
                'values': [df_Injured[0], df_Injured[1], df_Injured[2]]}

        df2 = pd.DataFrame(data)

        fig = go.Figure(data=[go.Pie(labels=df2['names'], values=df2['values'])])
        fig.update_traces(textfont_size=14, textinfo='percent',
                          # pull=[0.1,0.05,0.1],
                          hole=.5
                          )

        fig.update_layout(margin=dict(l=0, r=100, t=0, b=0))
        fig.update_layout(width=300, height=300)
        fig.update_traces(legendgrouptitle=dict(text='Number of Deaths - {}:'.format(year_heatmap)))

        fig.update_layout(legend=dict(
            orientation="h",
            entrywidth=70,
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))

        st.write(fig)

    with line_chart_col:
        st.sidebar.subheader('Line Chart Parameter')

        year_list = list(df['Year'].unique())
        # year_list.remove(2012)
        year_list.sort(reverse=True)

        parametro = st.sidebar.selectbox("What would you like to compared?", options=['Month', 'Weekday', 'Hours'], index=0)

        if parametro == 'Month':
            plot_data_l = st.sidebar.multiselect('Select Years', year_list, default=[year_list[1], year_list[2]])

            # st.header('Line Chart - Months')
            fig = go.Figure(layout=go.Layout(
                title=go.layout.Title(text="Comparing Car Accidents on each Year - Months")
            ))

            for anos in plot_data_l:
                if anos == float(2022):
                    fig.add_trace(go.Scatter(x=meses_df.Months_22, y=meses_df.Accidents_22, name='2022'))
                elif anos == float(2021):
                    fig.add_trace(go.Scatter(x=meses_df.Months_21, y=meses_df.Accidents_21, name='2021'))
                elif anos == float(2020):
                    fig.add_trace(go.Scatter(x=meses_df.Months_20, y=meses_df.Accidents_20, name='2020'))
                elif anos == float(2019):
                    fig.add_trace(go.Scatter(x=meses_df.Months_19, y=meses_df.Accidents_19, name='2019'))
                elif anos == float(2018):
                    fig.add_trace(go.Scatter(x=meses_df.Months_18, y=meses_df.Accidents_18, name='2018'))
                elif anos == float(2017):
                    fig.add_trace(go.Scatter(x=meses_df.Months_17, y=meses_df.Accidents_17, name='2017'))
                elif anos == float(2016):
                    fig.add_trace(go.Scatter(x=meses_df.Months_16, y=meses_df.Accidents_16, name='2016'))

        elif parametro == 'Weekday':
            plot_data_l = st.sidebar.multiselect('Select Years', year_list, default=[year_list[1], year_list[2]])

            # st.header('Line Chart - Weekdays')
            fig = go.Figure(layout=go.Layout(
                title=go.layout.Title(text="Comparing Car Accidents on each Year - Weekdays")
            ))

            for anos in plot_data_l:
                if anos == float(2022):
                    fig.add_trace(go.Scatter(x=weekdays_df.Weekday_22, y=meses_df.Accidents_22, name='2022'))
                elif anos == float(2021):
                    fig.add_trace(go.Scatter(x=weekdays_df.Weekday_21, y=meses_df.Accidents_21, name='2021'))
                elif anos == float(2020):
                    fig.add_trace(go.Scatter(x=weekdays_df.Weekday_20, y=meses_df.Accidents_20, name='2020'))
                elif anos == float(2019):
                    fig.add_trace(go.Scatter(x=weekdays_df.Weekday_19, y=meses_df.Accidents_19, name='2019'))
                elif anos == float(2018):
                    fig.add_trace(go.Scatter(x=weekdays_df.Weekday_18, y=meses_df.Accidents_18, name='2018'))
                elif anos == float(2017):
                    fig.add_trace(go.Scatter(x=weekdays_df.Weekday_17, y=meses_df.Accidents_17, name='2017'))
                elif anos == float(2016):
                    fig.add_trace(go.Scatter(x=weekdays_df.Weekday_16, y=meses_df.Accidents_16, name='2016'))

        elif parametro == 'Hours':
            plot_data_l = st.sidebar.multiselect('Select Years', year_list, default=[year_list[1], year_list[2]])

            fig = go.Figure(layout=go.Layout(
                title=go.layout.Title(text="Comparing Car Accidents on each Year - Hours")
            ))

            for anos in plot_data_l:
                if anos == float(2022):
                    fig.add_trace(go.Scatter(x=horas_df.Hours_22, y=horas_df.Accidents_22, name='2022'))
                elif anos == float(2021):
                    fig.add_trace(go.Scatter(x=horas_df.Hours_21, y=horas_df.Accidents_21, name='2021'))
                elif anos == float(2020):
                    fig.add_trace(go.Scatter(x=horas_df.Hours_20, y=horas_df.Accidents_20, name='2020'))
                elif anos == float(2019):
                    fig.add_trace(go.Scatter(x=horas_df.Hours_19, y=horas_df.Accidents_19, name='2019'))
                elif anos == float(2018):
                    fig.add_trace(go.Scatter(x=horas_df.Hours_18, y=horas_df.Accidents_18, name='2018'))
                elif anos == float(2017):
                    fig.add_trace(go.Scatter(x=horas_df.Hours_17, y=horas_df.Accidents_17, name='2017'))
                elif anos == float(2016):
                    fig.add_trace(go.Scatter(x=horas_df.Hours_16, y=horas_df.Accidents_16, name='2016'))

        fig.update_layout(margin=dict(l=30, r=30, t=30, b=30))
        fig.update_layout(width=710, height=300)
        fig.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ))

        st.write(fig)


with barchart_c:
    colu1, barchart_col = st.columns([0.7,2.3])

    with colu1:
        df_Injured = df1[df1.columns[[6, 8, 10]]].sum()

        lista = [df1.columns[6][10:], df1.columns[8][10:], df1.columns[10][10:]]

        data = {'names': [lista[0][:-7], lista[1][:-7], lista[2][:-7]],
                'values': [df_Injured[0], df_Injured[1], df_Injured[2]]}

        df2 = pd.DataFrame(data)

        fig = go.Figure(data=[go.Pie(labels=df2['names'], values=df2['values'])])
        fig.update_traces(textfont_size=14, textinfo='percent',
                          # pull=[0.1,0.05,0.1],
                          hole=.5
                          )

        fig.update_layout(margin=dict(l=0, r=100, t=0, b=0))
        fig.update_layout(width=300, height=300)
        fig.update_traces(legendgrouptitle=dict(text='Number of Injured Victims - {}:'.format(year_heatmap)))
        fig.update_layout(legend=dict(
            orientation="h",
            entrywidth=70,
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))

        st.write(fig)

    with barchart_col:
        st.sidebar.subheader('Barchart parameter')

        parameters1 = st.sidebar.selectbox("What would you like to analyze?", options=['Weekday', 'Month', 'Year'], index=2)

        year_list = list(df['Year'].unique())
        # year_list.remove(2012)
        year_list.sort(reverse=True)

        month_list = list(df['Month'].unique())
        # month_list.sort(reverse=True)

        weekday_list = list(df['Weekday'].unique())
        # weekday_list.sort(reverse=True)

        hour_list = list(df['Hour'].unique())
        hour_list.sort(reverse=True)

        if parameters1 == 'Year':
            parameters2 = st.sidebar.selectbox("Choose the year:", options=year_list, index=0)
            parameters3 = st.sidebar.selectbox("Choose an x-value:", options=['Hour', 'Weekday', 'Month'])
            st.text('Barplots {a}: {b} vs {c}'.format(a=parameters1, b=parameters2, c=parameters3))
            dfb = df[df['CRASH DATE'].dt.year == parameters2]

        elif parameters1 == 'Month':
            parameters2 = st.sidebar.selectbox("Choose option 2:", options=month_list, index=0)
            parameters3 = st.sidebar.selectbox("Choose option 3:", options=['Hour', 'Weekday', 'Year'])
            st.text('Barplots {a}: {b} vs {c}'.format(a=parameters1, b=parameters2, c=parameters3))
            # df = df[df['CRASH DATE'].dt.month == parameters2]
            dfb = df[df['Month'] == parameters2]

        elif parameters1 == 'Weekday':
            parameters2 = st.sidebar.selectbox("Choose option 2:", options=weekday_list, index=0)
            parameters3 = st.sidebar.selectbox("Choose option 3:", options=['Hour', 'Month', 'Year'])
            st.text('Barplots {a}: {b} vs {c}'.format(a=parameters1, b=parameters2, c=parameters3))
            # df = df[df['CRASH DATE'].dt.weekday == parameters2]
            dfb = df[df['Weekday'] == parameters2]

        frequency = pd.DataFrame(dfb[parameters3].value_counts())  # creates data frame with our data
        st.bar_chart(data=frequency, width=740, height=280, use_container_width=False)


with factors_c:
    st.sidebar.subheader('Contributing Factors - PieChart')
    year_list_facts = list(df['Year'].unique())
    # year_list.remove(2012)
    year_list_facts.sort(reverse=True)
    parameters_facts = st.sidebar.selectbox("Select a Year:", options=year_list_facts, index=0)

    df_f = df[df['CRASH DATE'].dt.year == parameters_facts]

    factorss = ['Unspecified', 'Other Vehicular']
    df_factors = df_f[df_f['CONTRIBUTING FACTOR VEHICLE 1'].isin(factorss) == False]
    df_factors = df_factors['CONTRIBUTING FACTOR VEHICLE 1'].dropna()

    fig = go.Figure(data=[go.Pie(labels=df_factors, values=df_factors.value_counts())])
    fig.update_traces(textfont_size=14, textinfo='percent',
                      pull=[0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2,
                            0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2,
                            0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
                      )
    #
    fig.update_layout(margin=dict(l=0, r=100, t=0, b=0))
    fig.update_layout(width=1000, height=600)
    # fig.update_traces(legendgrouptitle=dict(text='Number of Injured Victims - {}:'.format(year_heatmap)))
    fig.update_layout(legend=dict(
        orientation="h",
        entrywidth=70,
        yanchor="top",
        y=0.9,
        xanchor="right",
        x=0
    ))

    fig.update_layout(
        title={'text': "Contributing Factors - Car Accidents",
            'y': 0.9,
            'x': .17,
            'xanchor': 'center',
            'yanchor': 'top'})

    #fig.update_traces(textinfo='percent+label')


    st.write(fig)
