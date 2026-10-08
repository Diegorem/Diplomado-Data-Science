import streamlit as st
import pandas as pd
import numpy as np

st.title("Cycle Rides in NYC")

DATE_COLUMN = "started_at"
DATA_URL = "citibike-tripdata.csv"

@st.cache_data  # ✅ antes @st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data.rename({"start_lat": "lat", "start_lng": "lon"}, axis=1, inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text("Loading cycle NYC data...")
data = load_data(1000)
data_load_state.text("Done! (using st.cache_data)")

if st.sidebar.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.write(data)

if st.sidebar.checkbox("Recorridos por hora"):
    st.subheader("Número de recorridos por hora")
    hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
    st.bar_chart(hist_values)

# Número en el rango 0-23
hour_to_filter = st.slider("hour", 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader("Map of all pickups at %s:00" % hour_to_filter)
st.map(filtered_data)
