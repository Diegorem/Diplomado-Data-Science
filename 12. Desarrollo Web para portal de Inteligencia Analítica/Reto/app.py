"""
app.py
Dashboard de Netflix App con Streamlit, Firestore y PostgreSQL.
"""

import streamlit as st
import pandas as pd
from google.cloud import firestore
from sqlalchemy import text
from google.oauth2 import service_account

#----Conexion----
@st.cache_resource
def get_db():
    """Crea y devuelve el cliente de Firestore usando keys.json."""
    if "firestore" in st.secrets:
        # Modo producción (Streamlit Cloud)
        key_dict = dict(st.secrets["firestore"])
        creds = service_account.Credentials.from_service_account_info(key_dict)
        return firestore.Client(credentials=creds, project=key_dict["project_id"])
    else:
        # Modo local (tu computadora)
        return firestore.Client.from_service_account_json("keys.json")

#----Carga de datos----
@st.cache_data
def load_movies():
    """Lee todos los documentos de 'movies' y los devuelve como DataFrame."""
    db = get_db().collection("movies")
    movies = []
    for doc in db.stream():
        data = doc.to_dict()
        movies.append(data)
    df = pd.DataFrame(movies)
    return df

#----Carga de db y funciones----
df = load_movies()    
conn_postgre = st.connection("postgresql", type="sql")

def filter_by_director(df, director):
    """Filtrar el df por director."""
    direc = df[df['director'] == director]
    st.header(f"Total de filmes: {len(direc)}")
    st.dataframe(direc)

#----Inicio de app----
st.title("Netflix App")
sb = st.sidebar
sb.header("Opciones")

#----Checkbox----
actDB = sb.checkbox("Mostrar todos los filmes")
if actDB:
    st.header("Todos los filmes")
    st.dataframe(df)
sb.markdown("---")

#----Busqueda por titulo----
titulo_buscado = sb.text_input("Titulo del filme")
if sb.button("Buscar filmes"):
    if titulo_buscado:
        filmTit = df[df['name'].str.contains(titulo_buscado, case=False, regex=False)]
        st.header(f"Total de filmes mostrados: {len(filmTit)}")
        st.dataframe(filmTit)
    else:
        st.warning("Ingrese texto para buscar un filme.")
sb.markdown("---")

#----Busqueda por director----
director_selec = sb.selectbox("Seleccionar director", options=sorted(df['director'].unique()))
if sb.button("Filtrar por director"):
    if director_selec:
        filter_by_director(df, director_selec)
    else:
        st.warning("Seleccione un director para filtrar.")
sb.markdown("---")

#----Formulario para insertar nueva peli----
db = get_db()
movies_ref = db.collection("movies")

sb.header("Nuevo filme")
with sb.form("formulario"):
    name = st.text_input("Name")
    genre= st.text_input("Genre")
    director = st.text_input("Director")
    company = st.text_input("Company")
    complete = st.form_submit_button("Crear nuevo filme")

if complete:
    if name and genre and director and company:
        nuevo_filme = {
            "name": name,
            "genre": genre,
            "director": director,
            "company": company
        }
        movies_ref.add(nuevo_filme)
        load_movies.clear()
        st.success(f"Filme '{name}' agregado exitosamente!")
        st.rerun()
    else:
        st.warning("Llena todos los campos.")
sb.markdown("---")

#----Formulario postgreSQL para comentarios----
sb.header("Libro de visitas")

with sb.form("form_postgre"):
    email = st.text_input("Email")
    comment = st.text_input("Comentario")
    enviar_coment = st.form_submit_button("Registrar visita")

if enviar_coment:
    if email and comment:
        with conn_postgre.session as session:
            session.execute(
                text("INSERT INTO people (email, comment) VALUES (:email, :comment);"),
                {"email": email, "comment": comment}
            )
            session.commit()
        st.toast("Comentario guardado!")
    else:
        st.warning("Por favor completa el correo y el comentario.")
sb.markdown("---")

#----Mostrar comentarios----
if sb.button("Ver visitas"):
    df_comments = conn_postgre.query("SELECT * FROM people;", ttl=0)
    st.dataframe(df_comments)