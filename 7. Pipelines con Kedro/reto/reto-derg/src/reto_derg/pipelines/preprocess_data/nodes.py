"""
This is a boilerplate pipeline 'preprocess_data'
generated using Kedro 0.19.15
"""

import pandas as pd

def filter_id(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["client_id"] < 1000]

def filter_client_id(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["id"] < 1000]