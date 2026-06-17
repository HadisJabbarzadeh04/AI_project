import json
from graph import Graph


def load_graph(file_path):

    with open(file_path, "r") as f:
        data = json.load(f)

    graph_data = data["graph"]
    positions = data.get("positions", {})

    graph = Graph()

    for node in graph_data:
        for neighbor, cost in graph_data[node]:
            graph.add_edge(node, neighbor, cost)

    return graph, positions