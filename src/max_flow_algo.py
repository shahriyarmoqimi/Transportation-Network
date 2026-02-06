from collections import deque


def bfs(n, s, t, parent, capacity, graph_adj):
    visited = [False] * n
    queue = deque([s])
    visited[s] = True
    parent[s] = -1

    while queue:
        u = queue.popleft()
        for v in capacity[u]:
            if not visited[v] and capacity[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == t:
                    return True
    return False


def run_max_flow(graph, s, t):
    n = graph.n
    capacity = [{} for _ in range(n)]

    for u in range(n):
        for item in graph.adj[u]:
            if graph.weighted:
                v, w = item
            else:
                v, w = item, 1

            if v in capacity[u]:
                capacity[u][v] += 1
            else:
                capacity[u][v] = 1

            if u not in capacity[v]:
                capacity[v][u] = 0

    parent = [-1] * n
    max_flow = 0

    while bfs(n, s, t, parent, capacity, graph.adj):
        path_flow = float('inf')
        curr = t
        while curr != s:
            prev = parent[curr]
            path_flow = min(path_flow, capacity[prev][curr])
            curr = prev

        max_flow += path_flow
        curr = t
        while curr != s:
            prev = parent[curr]
            capacity[prev][curr] -= path_flow
            capacity[curr][prev] += path_flow
            curr = prev

    return max_flow
