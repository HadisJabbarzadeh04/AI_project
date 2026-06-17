from loader import load_graph
from graph import Graph
from search_problem import SearchProblem
from search_result import print_result
from bfs import BFS
from ucs import UniformCostSearch
from dfs import DFS
from dls import DLS
from ids import IDS
from greedy import GreedyBestFirstSearch
from astar import AStar
from visualize import visualize_graph


data_sets = {
    "1": "graph1.json",
    "2": "graph2.json",
    "3": "graph3.json",
    "4": "graph4.json",
    "5": "graph5.json",
    "6": "graph6.json",
    "7": "graph7.json",
    "8": "custom graph"
}

algorithms = {
    "1": "BFS",
    "2": "UCS",
    "3": "DFS",
    "4": "DLS",
    "5": "IDS",
    "6": "Greedy",
    "7": "A*",
}

exit = False

while not exit:

    selected_data_set = None

    while selected_data_set not in data_sets:

        print("\nSelect dataset:\n")

        for k, v in data_sets.items():
            print(f"{k}. {v}")

        selected_data_set = input("\n>>> ").strip()

        if selected_data_set not in data_sets:
            print("Invalid choice\n")


    if selected_data_set != "8":

        file = data_sets[selected_data_set]

        graph, positions = load_graph(file_path="data_test/" + file)

        graph.display()

        start = input("\nStart node >>> ").strip().upper()
        goal = input("Goal node >>> ").strip().upper()

        problem = SearchProblem(
            graph=graph,
            start=start,
            goal=goal,
            positions=positions
        )



    else:

        graph = Graph()

        print("\nEnter edges (format: A B cost)")
        print("type 'done' to finish\n")

        while True:

            inp = input("edge >>> ").strip()

            if inp.lower() == "done":
                break

            try:
                u, v, c = inp.split()

                graph.add_edge(
                    u.upper(),
                    v.upper(),
                    float(c)
                )

            except:
                print("Invalid format. try again")

        graph.display()

        positions = {}

        print("\nEnter node positions (format: Node X Y)")
        print("type 'done' to finish\n")

        while True:

            inp = input("position >>> ").strip()

            if inp.lower() == "done":
                break

            try:
                node, x, y = inp.split()

                positions[node.upper()] = (
                    float(x),
                    float(y)
                )

            except:
                print("Invalid format. try again")

        start = input("\nStart node >>> ").strip().upper()
        goal = input("Goal node >>> ").strip().upper()

        problem = SearchProblem(
            graph=graph,
            start=start,
            goal=goal,
            positions=positions
        )

    

    selected_algorithm = None

    while selected_algorithm not in algorithms:

        print("\nSelect algorithm:\n")

        for k, v in algorithms.items():
            print(f"{k}. {v}")

        selected_algorithm = input("\n>>> ").strip()

        if selected_algorithm not in algorithms:
            print("Invalid choice\n")

    if selected_algorithm == "1":
        algorithm = BFS()

    elif selected_algorithm == "2":
        algorithm = UniformCostSearch()

    elif selected_algorithm == "3":
        algorithm = DFS()

    elif selected_algorithm == "4":
        limit = int(input("Enter depth limit: "))
        algorithm = DLS()

    elif selected_algorithm == "5":
        algorithm = IDS()

    elif selected_algorithm == "6":
        algorithm = GreedyBestFirstSearch()

    elif selected_algorithm == "7":
        algorithm = AStar()

    if selected_algorithm in ["6", "7"]:

        print("\n" + "=" * 30)
        print(f"Heuristics (Goal = {goal})")
        print("=" * 30)

        for node in sorted(graph.graph.keys()):
            print(
                f"h({node}) = "
                f"{problem.get_heuristic(node):.3f}"
            )

        print("=" * 30)


    if selected_algorithm == "4":
        result = algorithm.search(
            problem, limit
        )

    else:
        result = algorithm.search(
            problem
        )


    print_result(result)

    if result and "path" in result:
        visualize_graph(
            graph,
            result["path"]
        )


    continue_inp = None

    while continue_inp not in ["y", "n"]:

        continue_inp = input(
            "Do you want to continue? (y or n)\n>>> "
        ).lower()

        if continue_inp == "n":
            exit = True