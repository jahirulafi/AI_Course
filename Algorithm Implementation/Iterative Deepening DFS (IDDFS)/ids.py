# Your existing code for graph input remains the same
graph = {}
n = int(input("Enter number of nodes: "))
for i in range(n):
    node = input("Enter node name/number: ")
    neighbours = input(f"Enter neighbours of {node} : ").split()
    graph[node] = neighbours

visited = []  # We'll clear this before each DLS run
stack = []    # Same here

def ids(visited, graph, node, limit):
    stack.append((node, 0))

    while stack:
        m, depth = stack.pop()
        if m not in visited:
            print(m, end=" ")
            visited.append(m)

            if depth < limit:
            
               for neighbour in reversed(graph[m]):
                    if neighbour not in visited:
                        stack.append((neighbour, depth + 1))

start = input("Enter starting node: ")
max_depth = int(input("Enter max depth for IDS: "))

print("The Iterative Deepening Search is:")

for depth_limit in range(max_depth + 1):
    visited.clear()  # clear visited nodes before each iteration
    stack.clear()
    print(f"\nDepth limit = {depth_limit}: ", end="")
    ids(visited, graph, start, depth_limit)