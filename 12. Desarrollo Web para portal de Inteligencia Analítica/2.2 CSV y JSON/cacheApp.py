import pandas as pd
import streamlit as st

DATA_URL = 'dataset.csv'

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

# Create the tite for the web app
st.title('Streamlit and Pandas')
data = load_data(1000)
st.dataframe(data)