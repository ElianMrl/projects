import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from PIL import Image
from tools import *
sns.set()

st.set_page_config(
    page_title="Insights",
    page_icon="📖",
    layout='wide',
    initial_sidebar_state='expanded'
)

df, heat, factors, meses_df, weekdays_df, horas_df = load_data()

st.title("Data Exploratory Analysis 🕵🏻‍♂️")
st.markdown("In this section, go over a collection of some of the most interesting facts 💡 that we encountered after a rigorous Analysis 🔍. The Data used in this project was collected from the Motor Vehicle Database found on [NYC OpenData](https://opendata.cityofnewyork.us/) 📡.")

# Question 1
st.subheader("1. Which borough has the highest number of accidents?")
st.markdown("Brooklyn is the borough with the highest number of car accidents. According to a research from [John Jay](https://guides.lib.jjay.cuny.edu/c.php?g=288385&p=1922495#:~:text=Brooklyn,part%20of%20New%20York%20City.) College of Criminal Justice 'The most populous of the five boroughs, Brooklyn.' Which implies a correlation between number of people and car accidents. The more people implies a higher number of car accidents.")
image1 = Image.open(r"C:\Users\elian\website\data\Images_DEA\Borough_Acc.png")
st.image(image1, caption='Car Accidents - Borough')

# Question 2
st.subheader("2. How many car accidents happen because of city negligence?")
st.markdown("In the last 6, almost 3,000 car accidents have happened due to city negligence. Among these factors, the one that cost the most accidents is pavement defective followed by improper lane marking and non-working traffic control devices.")
image2 = Image.open(r"C:\Users\elian\website\data\Images_DEA\all_years_cityfault_acc.png")
st.image(image2, caption='City Negligence')

# Question 3
st.subheader("3. What is the trend of accidents yearly (decreasing/increasing)?")
st.markdown("Although, there was a noticeable yearly increase between 2016 and 2018. The pandemic positively affected car accidents. There were fewer car accidents when the pandemic started in March 2020. The country was shut down in 2020 to prevent the spread of COVID-19, which was the reason for the decrease in car accidents in New York City. As we recover from the pandemic, there is a notable increasing trend in car accidents each year.")
image3 = Image.open(r"C:\Users\elian\website\data\Images_DEA\Trend_Accidents_Yearly.png")
st.image(image3, caption='Car Accidents - Yearly Trend')

# Question 4
st.subheader("4. How many people die because of car accidents?")
st.markdown("So far this year, 2022, we have about 300 deaths due to car accidents and almost 60,000 injured victims. And most of this victims are not even driving, half of these victims are pedestrian.")
image4 = Image.open(r"C:\Users\elian\website\data\Images_DEA\dead_people.png")
st.image(image4, caption='Car Accidents - Tragedies')

# Question 5
st.subheader("5. What are the areas (zip code) with the highest accident rates?")
st.markdown("Out of the 231 zip codes collected on this analysis, the top 5 with the most car accidents belong to Brooklyn.")
image3 = Image.open(r"C:\Users\elian\website\data\Images_DEA\zipcode_acc.png")
st.image(image3, caption='Zip Codes')

# Question 6
st.subheader("6. At what time of the day we experienced the most car accidents?")
image6 = Image.open(r"C:\Users\elian\website\data\Images_DEA\Working_hours.png")
st.markdown("New Yorkers usually go to work at 9 AM and finish at 5 PM. Hence New Yorkers start driving at 8 AM to get to their jobs, and they start driving at 5 PM to get to their homes. Accidents peak occurs when people go to work and after they finish working. There is a higher peak at the end of people's shifts. Therefore, there is a clear correlation between the stress generated at work with car accidents. This confirms a correlation between car accidents and the number of drivers.")
st.image(image6, caption='Car Accidents per Hour')

# Question 7
st.subheader("7. Which months have the most accidents?")
st.markdown("Looking closely, we notice a peak between May and July, proving that there are more accidents in a warmer climate. One of the reasons for a higher increase in the summer is that after being in winter for most of the year, many people go out, and many new drivers start driving for the first time, causing more car accidents.")
image7 = Image.open(r"C:\Users\elian\website\data\Images_DEA\Day_of_Week.png")
st.image(image7, caption='Car Accidents per Weekday')

# Question 8
st.subheader("8. Which days of the week have the most accidents?")
image8 = Image.open(r"C:\Users\elian\website\data\Images_DEA\Month_Accidents.png")
st.markdown("There are more accidents on weekdays, with the peak being on Thursday. There are fewer chances of being in a car accident on the weekends. The reason for this is that on the weekends, there are less people driving because New Yorkers usually have the weekends off.")
st.image(image8, caption='More Car Accidents in the Hot Summer.')

# Question 9
st.subheader("9. What is the number one factor of a car accident?")
st.markdown("The main contributing factor to car accidents is Driver Inattention (Drivers using their cellphone). Even though the data has a count for drivers using cell phones separated from driver inattention, these two factors should be placed in the same category. One of the main distractions of a driver are cellphones, and many drivers will lie about the reason for their distraction when driving to avoid getting in more trouble by confessing that they were using their cellphone.")
image9 = Image.open(r"C:\Users\elian\website\data\Images_DEA\factors_acc.png")
st.image(image9, caption='Car Accidents Contributing Factors')

# Question 10
st.subheader("10. Is there any relation between the vehicle make/model and accidents?")
st.markdown("According to [ISeeCars](https://www.iseecars.com/popular-vehicle-type-by-state-study) the most popular type of vehicles in New York are Sedans (Honda CRV) and SUVs (Toyota RAV4). According our findings from our analysis, the type of car with the most dominina number of accidents are Sedans and SUVs.")
image10 = Image.open(r"C:\Users\elian\website\data\Images_DEA\type_of_vehicle.png")
st.image(image10, caption='Type of Vehicle')

# Question 11
st.subheader("11. How the Pandemic affected the number of car accidents?")
st.markdown("The pandemic was definitely a miserable and heartbreaking event. But despite the many negative events that arose from the confinement, positive effects arose simultaneously. Among these events or positive results of the pandemic was a decline in the number of car accidents starting in March 2020. That same year we experienced a drop of 100,000 car accidents.")
image11 = Image.open(r"C:\Users\elian\website\data\Images_DEA\Month_Accidents_and_Covid.png")
st.image(image11, caption='COVID-19 (Pandemic)')