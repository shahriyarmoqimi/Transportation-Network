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


def find_node_index(graph, prompt_text):
    while True:
        query = input(prompt_text).lower().strip()
        if not query: continue

        found_candidates = []
        for i in range(graph.n):
            info = graph.node_info[i]
            if query in info['name'].lower() or query in info['city'].lower():
                found_candidates.append(i)

        if not found_candidates:
            print(f"❌ No item found with name '{query}'. Please try again.")
            continue

        if len(found_candidates) == 1:
            idx = found_candidates[0]
            print(f"✅ Selected: {graph.node_info[idx]['name']} ({graph.node_info[idx]['city']})")
            return idx

        print(f"\n⚠️ {len(found_candidates)} matches found. Please enter the option number:")
        for i, idx in enumerate(found_candidates[:10]):
            info = graph.node_info[idx]
            print(f"   [{i + 1}] {info['name']} | City: {info['city']} ({info['country']})")

        while True:
            try:
                inp = input("👉 Option number (0 to search again): ")
                choice = int(inp)
                if choice == 0: break
                if 1 <= choice <= len(found_candidates[:10]):
                    final_idx = found_candidates[choice - 1]
                    print(f"✅ You selected: {graph.node_info[final_idx]['name']}")
                    return final_idx
            except ValueError:
                pass