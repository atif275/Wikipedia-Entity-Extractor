from typing import List, Optional
from langchain.graphs.graph_document import Relationship as BaseRelationship
from models.graph_entities.property import Property
from langchain.pydantic_v1 import Field


class Relationship(BaseRelationship):
    properties: Optional[List[Property]] = Field(
        None, description="List of relationship properties"
    )
