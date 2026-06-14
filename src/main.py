from graph import Graph
from dfs import DFS
from dls import DLS
from ids import IDS
from search_problem import SearchProblem

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

print(problem.start)
print(problem.goal)

dfs = DFS()
dfs.search(problem)


# *****************************************************
# get input for data set and algorithm and start point and goal
# check input, call loader for jsons, 

options = {
    "1": "graph1.json",
    "2": "graph2.json",
    "3": "graph3.json",
    "4": "custom graph"
}

algorithms = {
    "1": "BFS",
    "2": "UCS",
    "3": "DFS",
    "4": "DLS",
    "5": "IDS",
    "6": "Greedy",
    "7": "A*",

}


