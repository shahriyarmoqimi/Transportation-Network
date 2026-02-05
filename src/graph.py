

class Graph:
    def __init__(self, n, directed=False, weighted=False):
        self.n = n
        self.directed = directed
        self.weighted = weighted
        self.adj = [[] for _ in range(n)]
        self.node_info = [{} for _ in range(n)]


    def set_node_details(self, node_index, name, city, country, real_id):
        self.node_info[node_index] = {
            'name': name,
            'city': city,
            'country': country,
            'real_id': real_id
        }