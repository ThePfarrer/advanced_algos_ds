from dataclasses import dataclass


@dataclass
class Vertex:
    label: str


@dataclass
class Edge:
    source: Vertex
    dest: Vertex
    weight: float
    label: str


class Graph:
    def __init__(self):
        self.vertices = []
        self.adjacency_list = {}

    def add_vertex(self, v):
        if v in self.vertices:
            return

        self.vertices.append(v)
        self.adjacency_list[v] = []

    def add_edge(self, v, u, weight=0, label=""):
        if not (v in self.vertices and u in self.vertices):
            return

        if not self._are_adjacent(v, u):
            self.adjacency_list[v].append(Edge(v, u, weight, label))

    def _are_adjacent(self, v, u):
        for e in self.adjacent_list[v]:
            if e.dest == u:
                return True
        return False
