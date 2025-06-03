# streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('airline_customer_satisfaction.csv')

# Title
st.title("Airline Customer Satisfaction Dashboard")

# Filter
travel_type = st.selectbox("Select Travel Type", df['Type of Travel'].unique())
filtered_df = df[df['Type of Travel'] == travel_type]

# Pie chart
st.subheader("Satisfaction Distribution")
fig1 = px.pie(filtered_df, names='satisfaction')
st.plotly_chart(fig1)

# Bar chart
st.subheader("Average Ratings by Feature")
feature_cols = ['Inflight wifi service', 'Food and drink', 'Seat comfort']
mean_ratings = filtered_df[feature_cols].mean().reset_index()
mean_ratings.columns = ['Feature', 'Average Rating']
fig2 = px.bar(mean_ratings, x='Feature', y='Average Rating', color='Feature')
st.plotly_chart(fig2)
