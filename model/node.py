
class Node:
    def __init__(self, vertex, weight):
        self.vertex = int(vertex)
        self.weight = int(weight)

    def __repr__(self):
        return f'({self.vertex} , {self.weight})'
