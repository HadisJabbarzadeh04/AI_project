from node import Node


class GreedyBestFirstSearch:

    def f(self, node, problem):
        return problem.get_heuristic(node.state)

    def search(self, problem):

        start_node = Node(
            state=problem.start,
            cost=0
        )

        frontier = [start_node]
        reached = {problem.start: start_node}

        expanded_nodes = 0
        step = 1

        print("=" * 40)
        print(f"STEP {step}")
        print(f"Frontier: {[(n.state, self.f(n, problem)) for n in frontier]}")

        while frontier:

            step += 1

            min_index = 0
            for i in range(1, len(frontier)):
                if self.f(frontier[i], problem) < self.f(frontier[min_index], problem):
                    min_index = i

            current = frontier.pop(min_index)

            print("=" * 40)
            print(f"STEP {step}")
            print(f"Selected Node: {current.state}")
            print(f"f(n)=h(n): {self.f(current, problem)}")
            print(f"Path Cost: {current.cost}")

            if current.state == problem.goal:
                print("Goal is Found.")
                return {
                    "path": current.get_path(),
                    "cost": current.cost,
                    "expanded_nodes": expanded_nodes
                }

            expanded_nodes += 1
            generated = []

            for neighbor, edge_cost in problem.graph.get_neighbors(current.state):

                child = Node(
                    state=neighbor,
                    parent=current,
                    cost=current.cost + edge_cost,
                    depth=current.depth + 1
                )

                if neighbor not in reached:

                    reached[neighbor] = child
                    frontier.append(child)

                    generated.append(
                        f"{neighbor} (h={problem.get_heuristic(neighbor)}, cost={child.cost})"
                    )

            print(f"Generated Nodes: {generated}")
            print(f"Frontier: {[(n.state, self.f(n, problem)) for n in frontier]}")

        return None