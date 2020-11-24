from model.node import Node


class Graph:
    def __init__(self, number_of_vertexes, edges):
        self.adjacency_list = [[] for _ in range(number_of_vertexes)]
        for edge in edges:
            node = Node(edge.destination, edge.weight)
            self.adjacency_list[edge.starting_point].append(node)
