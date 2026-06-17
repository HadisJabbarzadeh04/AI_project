from basic.node import Node

class GreedyBestFirstSearch:

    def f(self, node, problem):
        return problem.get_heuristic(node.state)

    def search(self, problem):

        start_node = Node(
            state=problem.start
        )

        frontier = [start_node]
        reached = {problem.start: start_node}

        explored = set()

        expanded_nodes = 0
        step = 1

        print("=" * 40)
        print(f"STEP {step}")
        print(
            "Frontier:",
            [(n.state, f"{self.f(n, problem):.3f}") for n in frontier]
        )

        while frontier:

            step += 1

            min_index = 0
            for i in range(1, len(frontier)):
                if self.f(frontier[i], problem) < self.f(frontier[min_index], problem):
                    min_index = i

            current = frontier.pop(min_index)

            explored.add(current.state)

            print("=" * 40)
            print(f"STEP {step}")
            print(f"Selected Node: {current.state}")
            print(f"f(n)=h(n): {self.f(current, problem):.3f}")
            print(f"Explored Nodes: {explored}")

            if current.state == problem.goal:
                print("Goal is Found.")
                return {
                    "path": current.get_path(),
                    "expanded_nodes": expanded_nodes
                }

            expanded_nodes += 1

            generated = []

            for neighbor, edge_cost in problem.graph.get_neighbors(current.state):

                child = Node(
                    state=neighbor,
                    parent=current
                )

                if neighbor not in reached:

                    reached[neighbor] = child
                    frontier.append(child)


                    generated.append(
                        f"{neighbor} "
                        f"(h={problem.get_heuristic(neighbor):.3f})"
                    )

            frontier_view = [
                f"{n.state}(h={self.f(n, problem):.3f})"
                for n in frontier
            ]

            print(f"Generated Nodes: {generated}")
            print(f"Frontier: {frontier_view}")

        return None