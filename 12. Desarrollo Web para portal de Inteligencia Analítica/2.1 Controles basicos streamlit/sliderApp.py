import pandas as pd
import streamlit as st

titanic_data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')

optionals = st.expander("Optional Configurations", expanded=True)
fare_select = optionals.slider(
    "Select the Fare",
    min_value=float(titanic_data["fare"].min()),
    max_value=float(titanic_data["fare"].max()),
)

subset_fare = titanic_data[(titanic_data['fare'] >= fare_select)]
st.write(f"Number of Records With this Fare {fare_select}: {subset_fare.shape[0]}")
