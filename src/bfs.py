import json

def bfs(graph, start):
    queue = []
    visited = []
    result = []

    queue.append(start)
    visited.append(start)

    while queue:
        current = queue[0]
        result.append(current)

        # Check neighbors
        neighbors = graph[current]

        for neighbor_info in neighbors:
            # First element is the neighbor's name
            neighbor = neighbor_info[0]  

            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

    return result


with open(f"graph", "r") as file:
    data = json.load(file)

graph = data["graph"]
start = data["start"]

result = bfs(graph, start)

print("Visited Nodes in Order:", result)
