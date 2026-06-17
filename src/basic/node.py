class Node:
    def __init__(
        self,
        state,
        parent = None,
        cost=0,
        depth=0
    ):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.depth = depth

    def get_path(self):
        path = []

        current = self

        while current:
            path.append(current.state)
            current = current.parent

        return path[::-1]

    def __repr__(self):
        return (
            f"Node(state={self.state}, "
            f"cost={self.cost}, "
            f"depth={self.depth})"
        )