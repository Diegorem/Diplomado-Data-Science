import pandas as pd
import streamlit as st

titanic_data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')
selected_class = st.radio("Select Class", titanic_data['class'].unique())

st.write("Selected Class:", selected_class)
