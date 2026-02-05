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