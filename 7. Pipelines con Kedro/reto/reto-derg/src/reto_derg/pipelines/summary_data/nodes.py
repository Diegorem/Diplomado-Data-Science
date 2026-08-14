"""
This is a boilerplate pipeline 'summary_data'
generated using Kedro 0.19.15
"""

import pandas as pd


def _clean_symbol(df: pd.DataFrame, column: str = "amount") -> pd.DataFrame:
    df = df.copy()
    df[column] = df[column].astype(str).str.replace("$", "", regex=False).astype(float)
    return df


def preprocess_transactions(transactions_filtered: pd.DataFrame) -> pd.DataFrame:
    return _clean_symbol(transactions_filtered, "amount")


def build_users_summary(
    cards_filtered: pd.DataFrame,
    transactions_clean: pd.DataFrame,
    users_filtered: pd.DataFrame,
) -> pd.DataFrame:
    base = users_filtered.rename(columns={"id": "client_id"})[["client_id"]]

    credit_count = (
        cards_filtered[cards_filtered["card_type"] == "Credit"]
        .groupby("client_id")
        .size()
        .rename("total_credit_cards")
    )
    debit_count = (
        cards_filtered[cards_filtered["card_type"] == "Debit"]
        .groupby("client_id")
        .size()
        .rename("total_debit_cards")
    )

    trans_summary = (
        transactions_clean
        .groupby("client_id")
        .agg(total_transactions=("id", "count"), total_amount=("amount", "sum"))
    )

    summary = (
        base
        .merge(credit_count, on="client_id", how="left")
        .merge(debit_count, on="client_id", how="left")
        .merge(trans_summary, on="client_id", how="left")
    )

    count_cols = ["total_credit_cards", "total_debit_cards", "total_transactions"]
    summary[count_cols] = summary[count_cols].fillna(0).astype(int)
    summary["total_amount"] = summary["total_amount"].fillna(0).round(2)

    return summary[
        ["client_id", "total_credit_cards", "total_debit_cards",
         "total_transactions", "total_amount"]
    ]


def build_merchant_summary(transactions_clean: pd.DataFrame) -> pd.DataFrame:
    summary = (
        transactions_clean
        .groupby(["merchant_id", "merchant_city", "use_chip"], as_index=False)["amount"]
        .sum()
        .rename(columns={"amount": "total_amount"})
    )
    summary["total_amount"] = summary["total_amount"].round(2)
    return summary
