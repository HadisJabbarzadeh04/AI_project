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
        expanded_nodes = 1
        cutoff_occurred = False
        step = 1

        while frontier:

            print(f"STEP {step}")

            
            current = frontier.pop()

            print(f"Current Node: {current.state}")
            print(f"Depth: {current.depth}")

            # SUCCESS
            if current.state == problem.goal:
                print(40*"=")
                print("Goal is Found.")
                print("Final Result")
                print("Path: ",current.get_path())
                print("Cost: ",current.cost)
                print("Expanded Nodes: ",expanded_nodes)
                return
            

            # CUTOFF check
            if current.depth >= limit:

                print(">>> CUTOFF REACHED")

                cutoff_occurred = True
                step += 1
                continue

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
            print(40*"=")
            print("Final Result")
            print("Path: ",[])
            print("Cost: ",0)
            print("Expanded Nodes: ",expanded_nodes)
            return


        else:
            print(40*"=")
            print("Final Result")
            print("Path: ",[])
            print("Cost: ",0)
            print("Expanded Nodes: ",expanded_nodes)
            return
