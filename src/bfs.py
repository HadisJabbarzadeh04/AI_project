from node import Node

class BFS:

    def search(self, problem):

        start_node = Node(state=problem.start, depth=0)

        queue = []
        visited = []
        result = []

        queue.append(start_node)
        visited.append(start_node.state)

        step = 1

        print("=" * 40)
        print(f"STEP {step}")
        print(f"Queue: {[n.state for n in queue]}")

        while queue:

            step += 1

            print("=" * 40)
            print(f"STEP {step}")

            current = queue.pop(0)

            print(f"Expanded Node: {current.state}")

            result.append(current.state)

            if current.state == problem.goal:

                print("=" * 40)
                print("Goal is Found.")
                print("Final Result")
                print("Path:", " -> ".join(current.get_path()))
                print("Cost:", current.cost)
                print("Visited Nodes:", result)

                return

            neighbors = problem.graph.get_neighbors(
                current.state
            )

            generated = []

            for neighbor_info in neighbors:

                neighbor = neighbor_info[0]
                cost = neighbor_info[1]

                if neighbor not in visited:

                    child = Node(
                        state=neighbor,
                        parent=current,
                        cost=current.cost + cost,
                        depth=current.depth + 1
                    )

                    visited.append(neighbor)
                    queue.append(child)
                    generated.append(neighbor)

            print(f"Generated Nodes: {generated}")
            print(f"Queue: {[n.state for n in queue]}")
            print(f"Visited: {visited}")

        print("=" * 40)
        print("Goal not found.")