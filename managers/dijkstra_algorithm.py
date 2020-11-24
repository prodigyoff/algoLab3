from queue import PriorityQueue
from model.edge import Edge
from model.graph import Graph
import sys

vertex_distance = []
parent_vertexes = []


def dijkstra(graph: list, start_vertex: int):
    """
    >>> edges = [Edge(0, 2, 10), Edge(2, 3, 80), Edge(2, 1, 40), Edge(2, 0, 10), Edge(2, 3, 80),
    ...    Edge(3, 2, 80), Edge(3, 1, 100), Edge(3, 4, 50), Edge(4, 3, 50), Edge(4, 5, 20),
    ...    Edge(5, 4, 20), Edge(1, 2, 40), Edge(1, 3, 100)]
    >>> graph = Graph(6, edges)
    >>> dijkstra(graph.adjacency_list, 0)
    [0, 50, 10, 90, 140, 160]

    >>> edges = [Edge(0, 2, 60), Edge(2, 3, 100), Edge(2, 1, 80), Edge(2, 0, 60), Edge(2, 3, 180),
    ...    Edge(3, 2, 180), Edge(3, 1, 100), Edge(3, 4, 150), Edge(4, 3, 150), Edge(4, 5, 120),
    ...    Edge(5, 4, 120), Edge(1, 2, 80), Edge(1, 3, 100)]
    >>> graph = Graph(6, edges)
    >>> dijkstra(graph.adjacency_list, 0)
    [0, 140, 60, 160, 310, 430]
    """

    global vertex_distance
    vertex_distance = []
    [vertex_distance.append(sys.maxsize) for _ in graph]
    [parent_vertexes.append(None) for _ in graph]
    vertex_distance[start_vertex] = 0
    available_vertexes_queue = PriorityQueue()
    available_vertexes_queue.put((0, start_vertex))

    while not available_vertexes_queue.empty():
        vertex_to_check = available_vertexes_queue.get()[1]

        for child_vertex_tuple in graph[vertex_to_check]:
            child_vertex = child_vertex_tuple.vertex
            distance = vertex_distance[vertex_to_check] + child_vertex_tuple.weight
            if relax_edge(child_vertex, vertex_to_check, distance):
                available_vertexes_queue.put((distance, child_vertex))
    return vertex_distance


def relax_edge(child_vertex: int, parent_vertex: int, distance: int):
    if vertex_distance[child_vertex] < distance:
        return False
    parent_vertexes[child_vertex] = parent_vertex
    vertex_distance[child_vertex] = distance
    return True


def main():
    import doctest

    doctest.testmod(verbose=True)


if __name__ == '__main__':
    main()
