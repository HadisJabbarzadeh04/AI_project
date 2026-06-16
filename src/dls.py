from node import Node


class DLS:

    def search(
        self,
        problem,
        limit
    ):

        start_node = Node(
            state=problem.start,
            depth=0
        )

        frontier = [start_node]
        expanded_nodes = 0
        cutoff_occurred = False
        step = 1

        while frontier:

            print(f"STEP {step}")

            
            current = frontier.pop()

            print(f"Selected Node: {current.state}")
            print(f"Depth: {current.depth}")

            # SUCCESS
            if current.state == problem.goal:
                    return {
                        "status": "success",
                        "path": current.get_path(),
                        "cost": current.cost,
                        "expanded_nodes": expanded_nodes
                    }

            # CUTOFF check
            if current.depth >= limit:
                print("CUTOFF!")
                print(40 * "=")
                cutoff_occurred = True
                step += 1
                continue

            print(f"Expanding {current.state} cause it's not goal.")

            expanded_nodes += 1

            neighbors = problem.graph.get_neighbors(current.state)

            generated = []

            for neighbor, cost in reversed(neighbors):

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
            print("=" * 40)

            step += 1

        # END LOOP

        if cutoff_occurred:
            return {
                "status": "cutoff",
                "path": [],
                "cost": 0,
                "expanded_nodes": expanded_nodes
            }

        print("FAILURE!")
        return {
            "status": "failure",
            "path": [],
            "cost": 0,
            "expanded_nodes": expanded_nodes
        }