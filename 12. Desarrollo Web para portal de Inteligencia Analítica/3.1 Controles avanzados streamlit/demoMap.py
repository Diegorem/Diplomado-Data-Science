import pandas as pd
import numpy as np
import streamlit as st

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"],
)

# Título de la app
st.title("San Francisco Map")
st.header("Using Streamlit and Mapbox")
st.map(map_data)