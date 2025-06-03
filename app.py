import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Aviation Dashboard", layout="wide")

# Sidebar selection with user-friendly labels
dataset_name = st.sidebar.selectbox(
    "Choose a dataset",
    (
        "Airline Dataset (Updated v2)",
        "Aircraft Data",
        "Airline Customer Satisfaction",
        "Airlines Reference Table",
        "Synthetic Flight Passenger Data"
    )
)

# Load selected dataset
@st.cache_data
def load_data(name):
    if name == "Airline Dataset (Updated v2)":
        return pd.read_csv("datasets/Airline_Dataset_Updated_-_v2.csv")
    elif name == "Aircraft Data":
        return pd.read_csv("datasets/aircraft_data.csv")
    elif name == "Airline Customer Satisfaction":
        return pd.read_csv("datasets/airline_customer_satisfaction.csv")
    elif name == "Airlines Reference Table":
        return pd.read_csv("datasets/airlines.csv")
    elif name == "Synthetic Flight Passenger Data":
        return pd.read_csv("datasets/synthetic_flight_passenger_data.csv")

# Load and display the selected dataset
df = load_data(dataset_name)

st.title(f"{dataset_name}")
st.dataframe(df)

# Optional quick chart preview if relevant columns exist
if "satisfaction" in df.columns:
    fig = px.histogram(df, x="satisfaction", color="Class", barmode="group")
    st.plotly_chart(fig, use_container_width=True)
elif "airline" in df.columns:
    fig = px.histogram(df, x="airline")
    st.plotly_chart(fig, use_container_width=True)
elif "passenger_id" in df.columns and "flight_date" in df.columns:
    df['flight_date'] = pd.to_datetime(df['flight_date'])
    fig = px.histogram(df, x="flight_date")
    st.plotly_chart(fig, use_container_width=True)
