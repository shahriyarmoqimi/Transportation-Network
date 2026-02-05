from utils import reconstruct_path


def run_dijkstra(graph, start, target):
    n = graph.n
    INF = 10 ** 10
    dis = [INF] * n
    parent = [-1] * n
    visited = [False] * n

    dis[start] = 0

    for i in range(n):
        u = -1
        best = INF

        for j in range(n):
            if not visited[j] and dis[j] < best:
                best = dis[j]
                u = j

        if u == -1 or dis[u] == INF:
            break

        visited[u] = True

        if u == target:
            break

        for item in graph.adj[u]:
            if graph.weighted:
                v, w = item
            else:
                v, w = item, 1

            if not visited[v]:
                if dis[u] + w < dis[v]:
                    dis[v] = dis[u] + w
                    parent[v] = u

    return reconstruct_path(start, target, parent, dis)