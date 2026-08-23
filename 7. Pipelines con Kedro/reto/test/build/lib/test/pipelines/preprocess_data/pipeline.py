"""
This is a boilerplate pipeline 'preprocess_data'
generated using Kedro 0.19.15
"""

from kedro.pipeline import node, Pipeline, pipeline # noqa
from .nodes import split_data

split_data_node = node(
    func=split_data,
    inputs=[
        "tracks",                  # Dataset definido en catalog.yml
        "params:data.train_fraction", # Parámetro definido en YAML
        "params:data.random_seed"     # Parámetro definido en YAML
    ],
    outputs=["train_data", "test_data"],
    name="split_data_node",
)

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([split_data_node])
