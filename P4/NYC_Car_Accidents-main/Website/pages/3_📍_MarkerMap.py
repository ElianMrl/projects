import streamlit as st
import pandas as pd
# import plost
import plotly.express as px
import plotly.graph_objects as go
from tools import *

st.set_page_config(
    page_title="MarkerMap",
    page_icon="📍",
)

markermap_m = st.container()


with markermap_m:
    #df, heat, factors, meses_df, weekdays_df, horas_df = load_data()
    st.header('Marker Map: 📍🗺️')
    st.sidebar.subheader('Marker parameter')
    month_markers_list = [1, 2, 3, 4, 5, 6]
    month_markers_list.sort(reverse=True)
    parametro = st.sidebar.selectbox("Choose how many months ago:", options=month_markers_list, index=0)
    if parametro == 1:
        st.caption(' Malfunctioning Devices: {a} Month ago'.format(a=parametro))
    elif parametro > 1:
        st.caption(' Malfunctioning Devices: {a} Months ago'.format(a=parametro))
    display_markers_map(r'C:\Users\elian\website\data\city_fault.csv', parametro)
    # display_markers_map('city_fault.csv', parametro)