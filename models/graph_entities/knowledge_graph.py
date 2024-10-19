from typing import List
from langchain.pydantic_v1 import Field, BaseModel

from models.graph_entities.node import Node
from models.graph_entities.relationship import Relationship


class KnowledgeGraph(BaseModel):
    """Generate a knowledge graph with entities and relationships."""

    nodes: List[Node] = Field(..., description="List of nodes in the knowledge graph")
    relationships: List[Relationship] = Field(
        ..., description="List of relationships in the knowledge graph"
    )
