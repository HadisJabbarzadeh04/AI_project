class Graph:

    def __init__(self):
        self.graph = {}

    def add_node(self, node):

        if node not in self.graph:
            self.graph[node] = []

    def add_edge(
        self,
        source,
        destination,
        cost=1
    ):

        self.add_node(source)
        self.add_node(destination)

        self.graph[source].append(
            (destination, cost)
        )

    def get_neighbors(self, node):

        return self.graph.get(node, [])

    def has_node(self, node):

        return node in self.graph

    def display(self):

        print("\nGraph:\n")

        for node, neighbors in self.graph.items():
            print(
                f"{node} -> {neighbors}"
            )