import math


class SearchProblem:

    def __init__(
        self,
        graph,
        start,
        goal,
        positions=None
    ):

        self.graph = graph
        self.start = start
        self.goal = goal
        self.positions = (
            positions
            if positions
            else {}
        )

    def get_heuristic(
        self,
        state
    ):

        if (
            state not in self.positions
            or self.goal not in self.positions
        ):
            return 0

        return math.dist(
            self.positions[state],
            self.positions[self.goal]
        )