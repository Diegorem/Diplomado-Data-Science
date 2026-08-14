"""
This is a boilerplate pipeline 'preprocess_data'
generated using Kedro 0.19.15
"""
import pandas as pd

def split_data(
    data: pd.DataFrame,
    test_size: float = 0.2,
    random_state: int = 42) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Splits the data into training and testing sets.
    """
    # 1. Reorganizar/Mezclar los datos
    data = data.sample(frac=1, random_state=random_state)

    # 2. Calcular punto de corte
    split_index = int(len(data) * (1 - test_size))

    # 3. Separar los dataframes
    train_data = data.iloc[:split_index]
    test_data = data.iloc[split_index:]

    return train_data, test_data