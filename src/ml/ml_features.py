
def extract_features(graph, u, v):
    neighbors_u = set()
    for item in graph.adj[u]:
        neighbors_u.add(item[0] if isinstance(item, tuple) else item)

    neighbors_v = set()
    for item in graph.adj[v]:
        neighbors_v.add(item[0] if isinstance(item, tuple) else item)

    # feature1 sum of degree
    deg_sum = len(neighbors_u) + len(neighbors_v)

    # feature2 common neighbors
    common = len(neighbors_u.intersection(neighbors_v))

    # feature3 common neighbors/all neighbors
    union_len = len(neighbors_u.union(neighbors_v))
    jaccard = common / union_len if union_len > 0 else 0

    return [deg_sum, common, jaccard]
