class SearchProblem:

    def __init__(
        self,
        graph,
        start,
        goal,
        heuristic=None
    ):

        self.graph = graph
        self.start = start
        self.goal = goal

        self.heuristic = (
            heuristic if heuristic
            else {}
        )

    def get_heuristic(
        self,
        state
    ):

        return self.heuristic.get(
            state,
            0
        )