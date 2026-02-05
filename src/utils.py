from math import radians, cos, sin, asin, sqrt


def haversine(lon1, lat1, lon2, lat2):

    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371
    return c * r


def reconstruct_path(start, target, parent, dis):
    if dis[target] >= 10 ** 9:
        return float('inf'), []

    path = []
    curr = target
    while curr != -1:
        path.append(curr)
        if curr == start: break
        curr = parent[curr]

    path.reverse()
    return dis[target], path


