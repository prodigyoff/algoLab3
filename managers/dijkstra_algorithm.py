from queue import PriorityQueue
import sys

vertex_distance = []
parent_vertexes = []


def dijkstra(graph: list, start_vertex: int):
    global vertex_distance
    vertex_distance = []
    init_graph_vars(graph, start_vertex)
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


def init_graph_vars(graph: list, start_vertex: int):
    for _ in graph:
        vertex_distance.append(sys.maxsize)
        parent_vertexes.append(None)
    vertex_distance[start_vertex] = 0
