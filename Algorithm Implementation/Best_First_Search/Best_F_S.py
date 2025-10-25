# Best First Search using simple sorting

graph = {}
n = int(input("Enter number of nodes: "))

# Input graph
for i in range(n):
    node = input(f"Enter node name: ")
    neighbours = input(f"Enter neighbours of {node} (space separated): ").split()
    graph[node] = neighbours

# Input heuristic values
heuristic = {}
for node in graph:
    h = int(input(f"Enter heuristic value of {node}: "))
    heuristic[node] = h

start = input("Enter starting node: ")
goal = input("Enter goal node: ")

visited = []
open_list = [start]  # Nodes to explore

print("\nThe Best-First Search is:")

while open_list:
    # Sort the open_list based on heuristic values
    open_list.sort(key=lambda node: heuristic[node])
    
    # Pick the node with the lowest heuristic
    node = open_list.pop(0)
    
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        
        if node == goal:
            break
        
        # Add neighbors to open_list if not visited
        for neighbour in graph[node]:
            if neighbour not in visited and neighbour not in open_list:
                open_list.append(neighbour)