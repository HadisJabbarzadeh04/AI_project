from node import Node


class UniformCostSearch:

    def f(self, node):
        return node.cost

    def search(self, problem):

        start_node = Node(
            state=problem.start,
            cost=0
        )

        frontier = [start_node]
        reached = {problem.start: start_node}

        explored = set()

        expanded_nodes = 0
        step = 1

        print("=" * 40)
        print(f"STEP {step}")
        print(f"Frontier: {[n.state for n in frontier]}")

        while frontier:

            step += 1

            min_index = 0
            for i in range(1, len(frontier)):
                if self.f(frontier[i]) < self.f(frontier[min_index]):
                    min_index = i

            current = frontier.pop(min_index)
            explored.add(current.state)

            print("="*  40)
            print(f"STEP {step}")
            print(f"Selected Node: {current.state}")
            print(f"Current Cost: {current.cost}")
            print(f"Explored Nodes: {explored}")

            if current.state == problem.goal:
                print("Goal is Found.")
                return {
                    "path": current.get_path(),
                    "cost": current.cost,
                    "expanded_nodes": expanded_nodes
                }

            expanded_nodes += 1

            generated = []

            for neighbor, cost in problem.graph.get_neighbors(current.state):

                new_cost = current.cost + cost

                child = Node(
                    state=neighbor,
                    parent=current,
                    cost=new_cost,
                    depth=current.depth + 1
                )

                if neighbor not in reached or new_cost < reached[neighbor].cost:

                    reached[neighbor] = child

                    found_index = -1
                    for i in range(len(frontier)):
                        if frontier[i].state == neighbor:
                            found_index = i
                            break

                    if found_index == -1:
                        frontier.append(child)
                        generated.append(f"{neighbor} (Cost={new_cost})")
                    else:
                        frontier[found_index] = child
                        generated.append(f"{neighbor} replaced (Cost={new_cost})")

            print(f"Generated Nodes: {generated}")
            print(f"Frontier: {[f'{n.state}(cost={n.cost})' for n in frontier]}")
        return None