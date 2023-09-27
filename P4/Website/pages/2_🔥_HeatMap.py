import streamlit as st
import pandas as pd
# import plost
import plotly.express as px
import plotly.graph_objects as go
from tools import *

st.set_page_config(
    page_title="HeatMap",
    page_icon="🔥",
)

heatmap_m = st.container()

# st.sidebar.success("Select a page above")

df, heat, factors, meses_df, weekdays_df, horas_df = load_data()

with heatmap_m:
    #df, heat, factors, meses_df, weekdays_df, horas_df = load_data()
    st.sidebar.subheader('Heatmap parameter')
    year_heat = st.sidebar.slider('Select a year for the HeatMap', min_value=2016, max_value=2022, value=2022, step=1)
    st.header('Heatmap: year {a} 🔥🗺️'.format(a=year_heat))
    display_heatmap(heat, year_heat)