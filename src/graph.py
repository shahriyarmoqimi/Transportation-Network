

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


    def add_edge(self, u, v, weight=None):
        if self.weighted:
            self.adj[u].append((v, weight))
            if not self.directed:
                self.adj[v].append((u, weight))
        else:
            self.adj[u].append(v)
            if not self.directed:
                self.adj[v].append(u)