# Take user input for graph
graph = {}
n = int(input("Enter number of nodes: "))
for i in range(n):
    node = input("Enter node name/number: ")
    neighbours = input(f"Enter neighbours of {node} : ").split()
    graph[node] = neighbours

visited = []  # List for visited nodes.
stack = []    # Initialize a stack

def dls (visited, graph, start_node, limit):
    # Stack holds tuples: (node, current_depth)
    stack.append((start_node, 0))

    while stack:
        node, depth = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.append(node)

            if depth < limit:
                # Add neighbors with incremented depth
                for neighbour in reversed(graph[node]):
                    if neighbour not in visited:
                        stack.append((neighbour, depth + 1))

start = input("Enter starting node: ")
limit = int(input("Enter depth limit: "))

print("The Depth-Limited Search is:")
dls (visited, graph, start, limit)