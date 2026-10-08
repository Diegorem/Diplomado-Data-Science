import streamlit as st

conn = st.connection("postgresql", type="sql")

if st.button("Query Postgresql table"):
    # Ejecutar la consulta (resultado guardado 10 minutos)
    df = conn.query("SELECT * FROM people;", ttl="10m")   # ✅ el PDF corta "ttl" con un guion por salto de línea
    # Mostrar resultados
    for row in df.itertuples():
        st.write(row)