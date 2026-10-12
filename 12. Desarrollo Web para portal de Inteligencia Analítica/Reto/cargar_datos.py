"""
cargar_datos.py
Carga los datos del csv a Firestore.
"""

import pandas as pd
from google.cloud import firestore

db = firestore.Client.from_service_account_json("keys.json")

df = pd.read_csv("movies.csv")
movies_ref = db.collection("movies")

for movie in df.to_dict(orient='records'):
    movies_ref.add(movie)
    print(f"Added movie: {movie['name']}")

total = len(movies_ref.get())
print(total)
