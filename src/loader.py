import json
from graph import Graph
from search_problem import SearchProblem


def load_problem(file_path):

    with open(file_path, "r") as f:
        data = json.load(f)

    graph_data = data["graph"]
    start = data["start"]
    goal = data["goal"]
    heuristic = data.get("heuristic", {})

    graph = Graph()

    for node in graph_data:

        for neighbor, cost in graph_data[node]:
            graph.add_edge(node, neighbor, cost)

    return SearchProblem(
        graph=graph,
        start=start,
        goal=goal,
        heuristic=heuristic
    )