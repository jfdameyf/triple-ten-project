import pandas as pd
import streamlit as st
import plotly.express as px

st.header("Vehicles Listings Dashboard")

df = pd.read_csv('vehicles_us_data.csv')

show_excellent = st.checkbox("Show only 'excellent' condition")
show_good = st.checkbox("Show only 'good' condition")
show_like_new = st.checkbox("Show only 'like new' condition")
show_fair = st.checkbox("Show only 'fair' condition")
if show_excellent:
    data = df[df.condition == 'excellent']
elif show_good:
    data = df[df.condition == 'good']
elif show_like_new:
    data = df[df.condition == 'like new']
else:
    data = df[df.condition =='fair']

hist = px.histogram(data, x = 'price', nbins=50, title='Price Distribution',
                    labels= {'price': 'Listing Price (USD)'})

st.plotly_chart(hist, use_container_width=True)

scatter = px.scatter(data, x='odometer', y='price', color='fuel',
                     opacity=0.5, title='Mileage vs. Price by fuel type',
                     labels={'odomter':'Mileage (mi)', 'price': 'Price (USD)'})

st.plotly_chart(scatter, use_container_width=True)