from graph import Graph
from search_problem import SearchProblem

from bfs import BFS
from dfs import DFS
from dls import DLS
from ids import IDS
from ucs import UniformCostSearch
from greedy import GreedyBestFirstSearch
from astar import AStarSearch

from search_result import print_result


graph = Graph()

graph.add_edge("A", "B", 2)
graph.add_edge("A", "C", 4)
graph.add_edge("B", "D", 3)
graph.add_edge("C", "E", 1)
graph.add_edge("D", "G", 2)
graph.add_edge("E", "G", 5)

graph.display()

problem = SearchProblem(
    graph,
    start="A",
    goal="G"
)

print("Start:", problem.start)
print("Goal:", problem.goal)

bfs = BFS()
result = bfs.search(problem)
print_result(result)


dfs = DFS()
result = dfs.search(problem)
print_result(result)


ucs = UniformCostSearch()
result = ucs.search(problem)
print_result(result)


greedy = GreedyBestFirstSearch()
result = greedy.search(problem)
print_result(result)

astar = AStarSearch()
result = astar.search(problem)
print_result(result)