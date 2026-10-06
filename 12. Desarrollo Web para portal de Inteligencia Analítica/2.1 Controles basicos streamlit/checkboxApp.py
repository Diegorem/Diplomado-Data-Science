import pandas as pd
import streamlit as st

titanic_data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')

# Display the content of the dataset if the checkbox is true
st.header("Dataset")
agree = st.checkbox("Show DataSet Overview? ")
if agree:
    st.dataframe(titanic_data)