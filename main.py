import sys

from managers.dijkstra_algorithm import dijkstra
from model.edge import Edge
from model.graph import Graph

INPUT_FILE_LOCATION = 'data/gamsrv.in'
OUTPUT_FILE_LOCATION = 'data/gamsrv.out'

if __name__ == '__main__':
    with open(INPUT_FILE_LOCATION, 'r') as fileIn:
        nodes_amount, edges_amount = fileIn.readline().split()
        clients = [int(client) - 1 for client in next(fileIn).split()]
        routers = [int(router) for router in range(int(nodes_amount))]
        [routers.remove(client) for client in clients]

        edges = []
        for _ in range(int(edges_amount)):
            starting_point, destination, weight = fileIn.readline().split()
            edges.append(Edge(int(starting_point) - 1, int(destination) - 1, weight))
            edges.append(Edge(int(destination) - 1, int(starting_point) - 1, weight))

        graph = Graph(int(nodes_amount), edges)
        print('Graph:')
        graph.printGraph()

        min_weight = sys.maxsize
        for vertex in range(len(graph.adjacency_list)):
            if vertex not in clients:
                dijkstra_result = dijkstra(graph.adjacency_list, vertex)
                current_max_weight = max(dijkstra_result[client] for client in clients)
                min_weight = min(current_max_weight, min_weight)

        print(f'Answer: {min_weight}')

    with open(OUTPUT_FILE_LOCATION, 'w') as fileOut:
        fileOut.write(str(min_weight))
