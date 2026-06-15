from graph import Graph
from search_problem import SearchProblem

from bfs import BFS
from dfs import DFS
from dls import DLS
from ids import IDS
from ucs import UniformCostSearch
from greedy import GreedyBestFirstSearch
from astar import AStar

from search_result import print_result


graph = Graph()

graph.add_edge("A", "S", 140)
graph.add_edge("A", "Z", 75)
graph.add_edge("A", "T", 118)
graph.add_edge("S", "F", 99)
graph.add_edge("S", "R", 80)
graph.add_edge("F", "B", 211)
graph.add_edge("R", "P", 97)
graph.add_edge("P", "B", 101)

graph.display()

problem = SearchProblem(
    graph,
    start="A",
    goal="B"
)

print("Start:", problem.start)
print("Goal:", problem.goal)

# bfs = BFS()
# result = bfs.search(problem)
# print_result(result)


# dfs = DFS()
# result = dfs.search(problem)
# print_result(result)


# ucs = UniformCostSearch()
# result = ucs.search(problem)
# print_result(result)

# dls = DLS()
# result = dls.search(problem, limit=4)
# print_result(result)

# ids = IDS()
# result = ids.search(problem)
# print_result(result)


# greedy = GreedyBestFirstSearch()
# result = greedy.search(problem)
# print_result(result)

astar = AStar()
result = astar.search(problem)
print_result(result)