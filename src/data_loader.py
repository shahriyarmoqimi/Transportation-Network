import csv
import sys
from graph import Graph
from utils import haversine


def build_graph_task1(airports_file, routes_file):

    print("⏳ Reading files and building graph...")

    id_map = {}
    coords = {}
    temp_details = {}
    current_idx = 0

    try:
        with open(airports_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                try:
                    real_id = int(row[0])
                    name = row[1]
                    city = row[2]
                    country = row[3]
                    lat = float(row[6])
                    lon = float(row[7])

                    id_map[real_id] = current_idx
                    coords[real_id] = (lat, lon)

                    temp_details[current_idx] = {
                        'name': name, 'city': city, 'country': country, 'real_id': real_id
                    }
                    current_idx += 1
                except:
                    continue
    except FileNotFoundError:
        print(f"❌ File {airports_file} not found!");
        sys.exit()

    g = Graph(current_idx, directed=True, weighted=True)

    for idx, info in temp_details.items():
        g.set_node_details(idx, info['name'], info['city'], info['country'], info['real_id'])


