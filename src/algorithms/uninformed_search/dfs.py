from basic.node import Node


class DFS:

    def search(self, problem):

        start_node = Node(
            state=problem.start,
            depth=0
        )

        frontier = [start_node]
        explored = set()

        expanded_nodes = 0
        step = 1

        print("=" * 40)
        print(f"STEP {step}")
        print(f"Frontier: {[n.state for n in frontier]}")


        while frontier:

            step += 1

            print("=" * 40)
            print(f"STEP {step}")
            

            current = frontier.pop()

            if current.state in explored:
                continue

            print(f"Selected Node: {current.state}")

            if current.state == problem.goal:
                print("Goal Found.")
                return {
                    "path": current.get_path(),
                    "cost": current.cost,
                    "expanded_nodes": expanded_nodes
                }
            
            print(f"Expanding {current.state} cause it's not goal.")

            explored.add(current.state)
            expanded_nodes += 1

            neighbors = problem.graph.get_neighbors(current.state)

            generated = []

            for neighbor, cost in reversed(neighbors):

                if neighbor not in explored:

                    child = Node(
                        state=neighbor,
                        parent=current,
                        cost=current.cost + cost,
                        depth=current.depth + 1
                    )

                    frontier.append(child)
                    generated.append(neighbor)

            print(f"Generated Nodes: {generated}")
            print(f"Frontier: {[n.state for n in frontier]}")

            
        # number of expanded nodes
        print("Expanded Nodes: ",expanded_nodes)