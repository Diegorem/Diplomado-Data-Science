"""
This is a boilerplate pipeline 'summary_data'
generated using Kedro 0.19.15
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import build_merchant_summary, build_users_summary, preprocess_transactions


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_transactions,
                inputs="transactions_filtered",
                outputs="transactions_clean",
                name="clean_transactions_amount_node",
            ),
            node(
                func=build_users_summary,
                inputs=["cards_filtered", "transactions_clean", "users_filtered"],
                outputs="users_summary",
                name="build_users_summary_node",
            ),
            node(
                func=build_merchant_summary,
                inputs="transactions_clean",
                outputs="merchant_summary",
                name="build_merchant_summary_node",
            ),
        ]
    )
