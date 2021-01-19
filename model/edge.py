
class Edge:
    def __init__(self, starting_point, destination, weight):
        self.starting_point = int(starting_point)
        self.destination = int(destination)
        self.weight = int(weight)

    def __repr__(self):
        return f'({self.starting_point} , {self.destination}, {self.weight})'
