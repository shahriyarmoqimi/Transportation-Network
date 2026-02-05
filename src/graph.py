

class Graph:
    def __init__(self, n, directed=False, weighted=False):
        self.n = n
        self.directed = directed
        self.weighted = weighted
        self.adj = [[] for _ in range(n)]
        self.node_info = [{} for _ in range(n)]
