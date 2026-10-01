import streamlit as st

#Crear el título para la aplicación web
st.title("Mi Primera App con Streamlit")
sidebar = st.sidebar
sidebar.title("Esta es la barra lateral")
sidebar.write("Aquí van los elementos de entrada.")

st.header("Información sobre el Conjunto de datos")

st.header("Descripción de los datos")

st.write("""
Este es un simple ejemplo de una app para predecir

Esta app predice mis datos!
""")

