from collections import deque
from utils import reconstruct_path


def run_label_correcting(graph, start, target):
    n = graph.n
    INF = float('inf')
    dis = [INF] * n
    parent = [-1] * n
    in_queue = [False] * n

    queue = deque([start])
    dis[start] = 0
    in_queue[start] = True

    while queue:
        u = queue.popleft()
        in_queue[u] = False

        for item in graph.adj[u]:
            if graph.weighted:
                v, w = item
            else:
                v, w = item, 1

            if dis[u] + w < dis[v]:
                dis[v] = dis[u] + w
                parent[v] = u

                if not in_queue[v]:
                    queue.append(v)
                    in_queue[v] = True

    return reconstruct_path(start, target, parent, dis)