from langchain.graphs.neo4j_graph import Neo4jGraph

from models.graph_entities.node import Node
from models.graph_entities.relationship import Relationship
from langchain.graphs.graph_document import Node as BaseNode
from langchain.graphs.graph_document import Relationship as BaseRelationship


class Neo4jGraphPlottingService:
    def __init__(self, neo4j_graph: Neo4jGraph) -> None:
        self._neo4j_graph = neo4j_graph
        pass

    @property
    def neo_4j_graph(self) -> Neo4jGraph:
        return self._neo_4j_graph

    @neo_4j_graph.setter
    def neo_4j_graph(self, neo_4j_graph):
        self._neo4j_graph = neo_4j_graph

    def format_property_key(s: str) -> str:
        words = s.split()
        if not words:
            return s
        first_word = words[0].lower()
        capitalized_words = [word.capitalize() for word in words[1:]]
        return "".join([first_word] + capitalized_words)

    def props_to_dict(self, props) -> dict:
        """Convert properties to a dictionary."""
        properties = {}
        if not props:
            return properties
        for p in props:
            properties[self.format_property_key(p.key)] = p.value
        return properties

    def map_to_base_node(self, node: Node) -> BaseNode:
        """Map the KnowledgeGraph Node to the base Node."""
        properties = self.props_to_dict(node.properties) if node.properties else {}
        # Add name property for better Cypher statement generation
        properties["name"] = node.id.title()
        return BaseNode(
            id=node.id.title(), type=node.type.capitalize(), properties=properties
        )

    def map_to_base_relationship(self, rel: Relationship) -> BaseRelationship:
        """Map the KnowledgeGraph Relationship to the base Relationship."""
        source = self.map_to_base_node(rel.source)
        target = self.map_to_base_node(rel.target)
        properties = self.props_to_dict(rel.properties) if rel.properties else {}
        return BaseRelationship(
            source=source, target=target, type=rel.type, properties=properties
        )
