# The Edge simply represents an edge in a graph from source node
# to destination node
# The weight is just any value such as cost associated to trasversing
# from source to destination
class Edge():
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight
        
    def __eq__(self, other):
        if not isinstance(other, type(self)): return False
        return self.source == other.source and self.destination == other.destination and self.weight == other.weight
    
    def __hash__(self):
        return 17 * self.source + 31 * self.destination + 37 * self.weight