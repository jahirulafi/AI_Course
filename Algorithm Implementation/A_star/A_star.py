# A* Algorithm Implementation

graph = {}
n = int(input("Enter number of nodes: "))

# Input graph (with costs for each edge)
for i in range(n):
    node = input("Enter node name: ")
    neighbours = input(f"Enter neighbours of {node} with cost (format: B:2 C:4): ").split()
    graph[node] = {}
    for nb in neighbours:
        if ":" in nb:
            neigh, cost = nb.split(":")
            graph[node][neigh] = int(cost)

# Input heuristic values
heuristic = {}
for node in graph:
    h = int(input(f"Enter heuristic value of {node}: "))
    heuristic[node] = h

start = input("Enter starting node: ")
goal = input("Enter goal node: ")

open_list = [(start, 0)]  # (node, g-cost)
visited = {}

print("\nThe A* Search Path is:")

while open_list:
    # Sort by f(n) = g(n) + h(n)
    open_list.sort(key=lambda x: x[1] + heuristic[x[0]])
    node, g_cost = open_list.pop(0)

    if node in visited:
        continue
    
    print(node, end=" ")
    visited[node] = g_cost

    if node == goal:
        break

    # Explore neighbours
    for neighbour, cost in graph[node].items():
        if neighbour not in visited:
            open_list.append((neighbour, g_cost + cost))