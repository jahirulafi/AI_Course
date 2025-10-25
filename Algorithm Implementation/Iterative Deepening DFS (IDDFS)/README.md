# Iterative Deepening Search (IDS) Implementation

## Overview

The **Iterative Deepening Search (IDS)** algorithm is a hybrid of **Depth-First Search (DFS)** and **Breadth-First Search (BFS)**.  
It performs repeated depth-limited searches (DLS) with increasing depth limits until the goal node is found or a maximum depth is reached.

This approach combines the **space efficiency of DFS** with the **completeness of BFS**, making it suitable for large or infinite search spaces.

## How it Works

1. **Initialization**: The algorithm starts from the given start node with depth = 0.  
2. **Depth-Limited Search (DLS)**: It explores all nodes up to a certain depth limit using DFS.  
3. **Iterative Deepening**: If the goal is not found within the current limit, it increases the depth limit by 1 and repeats the search.  
4. **Termination**: The process continues until the goal is found or the maximum depth limit is reached.

## Code Structure

### Functions

1.  `dls(graph, node, limit, visited, stack)`:
    *   Performs a **Depth-Limited Search (DLS)** on the graph using an explicit stack.
    *   Traverses nodes up to a given depth limit.
    *   Uses the `visited` list to avoid revisiting nodes within a single depth level.
    *   Prints the nodes visited during the current depth-limited traversal.

2.  `ids(graph, start, max_depth)`:
    *   Implements the **Iterative Deepening Search (IDS)** by repeatedly calling `dls()` with increasing depth limits from 0 up to `max_depth`.
    *   Clears the `visited` and `stack` lists before each iteration.
    *   Displays the traversal result for each depth limit.

3.  `main` (top-level script):
    *   Takes user input for:
        - Number of nodes  
        - Node names and their neighbours (graph structure)  
        - Starting node  
        - Maximum search depth
    *   Builds the graph as a **Python dictionary** (adjacency list).
    *   Calls the `ids()` function and prints the nodes visited at each depth level.

## Sample Execution

### Example Input
```
Enter number of nodes: 4
Enter node name/number: A
Enter neighbours of A : B C
Enter node name/number: B
Enter neighbours of B : D
Enter node name/number: C
Enter neighbours of C :
Enter node name/number: D
Enter neighbours of D :
Enter starting node: A
Enter max depth for IDS: 3
```

### Example Output
```
The Iterative Deepening Search is:

Depth limit = 0: A 
Depth limit = 1: A B C 
Depth limit = 2: A B D C 
Depth limit = 3: A B D C
```

### Explanation
* At **depth 0**, only the start node `A` is visited.  
* At **depth 1**, `A`’s neighbours `B` and `C` are explored.  
* At **depth 2**, the algorithm goes deeper to visit `D`.  
* The process repeats until the maximum depth (3) is reached.

## Complexity

* **Time Complexity**: O(b^d), where  
  `b` = branching factor and `d` = depth of the shallowest goal node.
* **Space Complexity**: O(d), as IDS uses DFS internally and stores only the current path in memory.

## Applications

1. **Game Trees** – Exploring possible game moves efficiently.  
2. **Pathfinding** – Finding routes in large or infinite graphs.  
3. **AI Search Problems** – Used in uninformed search algorithms like those in AI planning and robotics.

## Advantages

1. **Completeness**: Guaranteed to find the solution if one exists.  
2. **Low Memory Usage**: Uses less memory than BFS.  
3. **Optimal for Unweighted Graphs**: Returns the shallowest goal node.

## Disadvantages

1. **Repetition**: Nodes at shallow levels are re-explored multiple times.  
2. **Time Consumption**: May take longer than BFS in small graphs due to repeated searches.

## Example Python Code

```
graph = {}
n = int(input("Enter number of nodes: "))
for i in range(n):
    node = input("Enter node name/number: ")
    neighbours = input(f"Enter neighbours of {node} : ").split()
    graph[node] = neighbours

visited = []
stack = []

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
    visited.clear()
    stack.clear()
    print(f"\nDepth limit = {depth_limit}: ", end="")
    ids(visited, graph, start, depth_limit)
```

## License

This project is open-source—feel free to use, modify, or distribute it.
