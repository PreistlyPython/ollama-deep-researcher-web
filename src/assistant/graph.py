from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class Node:
    """A node in the knowledge graph."""
    id: str # Unique identifier
    content: str # Text content
    source: Optional[str] = None # Source URL if from web search
    node_type: str = "general" # Type of node (e.g. "general", "source", "concept")
    metadata: Dict[str, Any] = field(default_factory=dict) # Additional metadata

@dataclass
class Edge:
    """An edge in the knowledge graph."""
    source_id: str # ID of source node
    target_id: str # ID of target node
    relation: str # Type of relationship
    weight: float = 1.0 # Strength of relationship
    metadata: Dict[str, Any] = field(default_factory=dict) # Additional metadata

class KnowledgeGraph:
    """A knowledge graph representing connected information."""
    def __init__(self):
        self.nodes: Dict[str, Node] = {} # Map of node ID to Node
        self.edges: List[Edge] = [] # List of all edges
        self.adj_list: Dict[str, List[str]] = {} # Adjacency list

    def add_node(self, node: Node) -> None:
        """Add a node to the graph."""
        self.nodes[node.id] = node
        if node.id not in self.adj_list:
            self.adj_list[node.id] = []

    def add_edge(self, edge: Edge) -> None:
        """Add an edge to the graph."""
        if edge.source_id not in self.nodes or edge.target_id not in self.nodes:
            raise ValueError("Both source and target nodes must exist in the graph")
        self.edges.append(edge)
        self.adj_list[edge.source_id].append(edge.target_id)

    def get_node(self, node_id: str) -> Optional[Node]:
        """Get a node by its ID."""
        return self.nodes.get(node_id)

    def get_neighbors(self, node_id: str) -> List[str]:
        """Get all neighboring node IDs for a given node."""
        return self.adj_list.get(node_id, [])

    def get_edges(self, source_id: str, target_id: str) -> List[Edge]:
        """Get all edges between two nodes."""
        return [
            edge for edge in self.edges
            if edge.source_id == source_id and edge.target_id == target_id
        ]

    def get_all_nodes(self) -> List[Node]:
        """Get all nodes in the graph."""
        return list(self.nodes.values())

    def get_all_edges(self) -> List[Edge]:
        """Get all edges in the graph."""
        return self.edges

    def clear(self) -> None:
        """Clear all nodes and edges from the graph."""
        self.nodes.clear()
        self.edges.clear()
        self.adj_list.clear()
