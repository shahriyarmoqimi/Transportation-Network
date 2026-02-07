import time
import os
from data_loader import build_graph_task1
from utils import find_node_index
from dijkstra_algo import run_dijkstra
from lc_algo import run_label_correcting
from max_flow_algo import run_max_flow
from ml.ml import run_ml_task


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))

    project_root = os.path.dirname(current_dir)
    data_dir = os.path.join(project_root, 'data')

    airports_path = os.path.join(data_dir, 'airports.dat')
    routes_path = os.path.join(data_dir, 'routes.dat')

    if not os.path.exists(airports_path) or not os.path.exists(routes_path):
        print(f"❌ Error: Data files not found in: {data_dir}")
        print("Please ensure structure is: Project/data/*.dat and Project/src/*.py")
        return

    g = build_graph_task1(airports_path, routes_path)

    print("\n--- Flight Route Optimization System ---")

    while True:
        print("=" * 50)
        start_node = find_node_index(g, "🛫 Source city name: ")
        target_node = find_node_index(g, "🛬 Destination city name: ")

        if start_node == target_node:
            print("❌ Source and destination cannot be the same!");
            continue

        print("\n" + "-" * 20 + " Results " + "-" * 20)

        print("\n🔹 Method 1: Dijkstra (Array Implementation)")
        t0 = time.time()

        dist1, path1 = run_dijkstra(g, start_node, target_node)

        t1 = time.time()

        if dist1 >= 10 ** 9:
            print("❌ No path found.")
        else:
            print(f"✅ Total distance: {dist1:.2f} km")
            print(f"⏱️ Execution time: {t1 - t0:.6f} seconds")
            print("📋 Suggested Path:")
            for s, n in enumerate(path1):
                info = g.node_info[n]
                print(f"   {s + 1}. {info['name']} ({info['city']})")

        print("\n🔸 Method 2: Label Correcting (Queue Implementation)")
        t0 = time.time()

        dist2, path2 = run_label_correcting(g, start_node, target_node)

        t1 = time.time()

        if dist2 == float('inf'):
            print("❌ No path found.")
        else:
            print(f"✅ Total distance: {dist2:.2f} km")
            print(f"⏱️ Execution time: {t1 - t0:.6f} seconds")
            # Print if the path is different
            if len(path1) != len(path2) and len(path1) > 0:
                print("   (Found path is different)")

        print("\n" + "-" * 20 + " Task 2: Maximum Flow " + "-" * 20)
        print("🔹 Computing Max Flow ...")
        print("   (Assumption: Capacity = Number of Flights)")

        t0 = time.time()
        max_flow_val = run_max_flow(g, start_node, target_node)
        t1 = time.time()

        print(f"✅ Maximum Flow: {max_flow_val:.2f} units")
        print(f"⏱️ Time: {t1 - t0:.6f} sec")

        print("\n" + "-" * 20 + " Bonus Task: ML " + "-" * 20)
        ask_ml = input("Do you want to run ML Link Prediction? (y/n): ").lower()
        if ask_ml == 'y':
            run_ml_task(g)

        if input("\nDo you want to continue? (y/n): ").lower() != 'y':
            break


if __name__ == "__main__":
    main()
