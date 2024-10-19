from typing import List, Optional
from langchain.graphs.graph_document import Node as BaseNode
from models.graph_entities.property import Property
from langchain.pydantic_v1 import Field


class Node(BaseNode):
    properties: Optional[List[Property]] = Field(
        None, description="List of node properties"
    )
