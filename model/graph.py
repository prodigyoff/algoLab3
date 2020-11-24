from model.node import Node


class Graph:
    def __init__(self, number_of_vertexes, edges):
        self.adjacency_list = [[] for _ in range(number_of_vertexes)]
        for edge in edges:
            node = Node(edge.destination, edge.weight)
            self.adjacency_list[edge.starting_point].append(node)

    def printGraph(self):
        for node in range(len(self.adjacency_list)):
            for edge in self.adjacency_list[node]:
                print(f"({node} -> {edge.vertex}, {edge.weight}) ", end='')
            print()
