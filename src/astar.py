from node import Node
from search_problem import SearchProblem

class AStar:

    def search(self, problem):

        start_node = Node(state=problem.start, cost=0, depth=0)

        open_list = [start_node]  # nodes waiting to be explored
        closed_list = []  # explored nodes

        expanded_nodes = 1
        step = 1

        print("=" * 40)
        print(f"STEP {step}")
        print(f"Open List: {[n.state for n in open_list]}")

        while open_list:

            step += 1

            print("=" * 40)
            print(f"STEP {step}")

            current = min(open_list, key=lambda node:node.cost + problem.get_heuristic(node.state))

            open_list.remove(current)

            current_h = problem.get_heuristic(current.state)
            current_f = current.cost + current_h

            print(
                f"Expanded Node: {current.state}"
            )

            print(
                f"g={current.cost}, "
                f"h={current_h}, "
                f"f={current_f}"
            )

            if current.state == problem.goal:

                print("=" * 40)
                print("Goal is Found.")
                print("Final Result")
                print(
                    "Path:",
                    " -> ".join(current.get_path())
                )
                print(
                    "Cost:",
                    current.cost
                )
                print(
                    "Expanded Nodes:",
                    expanded_nodes
                )

                return

            neighbors = problem.graph.get_neighbors(current.state)

            generated = []

            for neighbor, edge_cost in neighbors:

                g = current.cost + edge_cost
                h = problem.get_heuristic(neighbor)
                f = g + h

                skip = False

                # Check Open List
                for node in open_list:

                    node_f = (
                        node.cost +
                        problem.get_heuristic(node.state)
                    )

                    if (
                        node.state == neighbor
                        and node_f <= f
                    ):
                        skip = True
                        break

                # Check Closed List
                if not skip:

                    for node in closed_list:

                        node_f = (
                            node.cost +
                            problem.get_heuristic(node.state)
                        )

                        if (
                            node.state == neighbor
                            and node_f <= f
                        ):
                            skip = True
                            break

                if skip:
                    continue

                child = Node(
                    state=neighbor,
                    parent=current,
                    cost=g,
                    depth=current.depth + 1
                )

                open_list.append(child)

                generated.append(
                    f"{neighbor}(f={f})"
                )

            closed_list.append(current)

            expanded_nodes += 1

            print(
                f"Generated Nodes: {generated}"
            )

            print(
                "Open List:",
                [
                    f"{n.state}(f={n.cost + problem.get_heuristic(n.state)})"
                    for n in open_list
                ]
            )

            print(
                "Closed List:",
                [n.state for n in closed_list]
            )

        print("=" * 40)
        print("Goal not found.")
        print(
            "Expanded Nodes:",
            expanded_nodes
        )