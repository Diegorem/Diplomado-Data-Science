import streamlit as st
import pymongo

# Inicializa la conexión. cache_resource: se ejecuta una sola vez.
@st.cache_resource
def init_connection():
    return pymongo.MongoClient(**st.secrets["mongo"])

client = init_connection()

# Trae los datos de la colección. cache_data: se vuelve a ejecutar
# solo si cambia la consulta o pasados 10 minutos (ttl=600).
@st.cache_data(ttl=600)
def get_data():
    db = client.people            # base de datos "people"
    items = db.people.find()      # colección "people"
    items = list(items)           # lista (para que se pueda cachear)
    return items

if st.button("Query mongodb collection"):
    items = get_data()
    # Mostrar resultados
    for item in items:
        st.write(item)