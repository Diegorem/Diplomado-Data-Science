"""
This is a boilerplate pipeline 'preprocess_data'
generated using Kedro 0.19.15
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa
from .nodes import filter_client_id, filter_id

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=filter_id,
                inputs="cards",
                outputs="cards_filtered",
                name="filtered_cards_node",
            ),
            node(
                func=filter_id,
                inputs="transactions",
                outputs="transactions_filtered",
                name="filtered_transactions_node",
            ),
            node(
                func=filter_client_id,
                inputs="users",
                outputs="users_filtered",
                name="filtered_users_node",
            ),
        ]
    )
