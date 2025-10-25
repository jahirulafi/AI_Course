# Depth-First Search (DFS) Implementation

## Overview

**Depth-First Search (DFS)** is a graph traversal algorithm that explores as far as possible along each branch before backtracking.  
DFS is commonly used in pathfinding, scheduling problems, and exploring graph structures.

## How it Works

1. **Initialization**: Start from the given start node.  
2. **Traversal**: Explore nodes using a stack (LIFO) to go deep along each branch.  
3. **Visited Tracking**: Keep track of visited nodes to avoid revisiting.  
4. **Termination**: The search stops when all reachable nodes from the starting node are visited.

## Code Structure

### Functions

1.  `dfs(visited, graph, node)`:
    *   Performs **Depth-First Search** using an explicit stack.
    *   `visited`: List to track visited nodes.  
    *   `graph`: Dictionary representing the adjacency list.  
    *   `node`: Starting node for DFS.  
    *   Prints nodes in the order they are visited.

2.  `main` (top-level script):
    *   Takes user input for:
        - Number of nodes  
        - Node names and their neighbors  
        - Starting node
    *   Builds the graph as a **Python dictionary**.  
    *   Calls `dfs()` and prints the traversal result.

## Sample Execution

### Example Input


## Sample Execution

This example uses a graph with **6 vertices** and **7 edges**.

![Image](https://github.com/user-attachments/assets/401d237e-e9d2-45e0-a88a-450136be286e)
### Explanation

*   The algorithm starts at node **0** and explores as far as possible along each branch before backtracking.
*   The visited nodes are printed in the order they are traversed.

## Complexity

*   **Time Complexity**: O(V + E), where V is the number of vertices, and E is the number of edges.
*   **Space Complexity**: O(V), as the algorithm needs to store the visited nodes.

## Applications

1.  **Graph Traversal**: DFS is used in graph traversal problems, such as finding connected components.
2.  **Network Analysis**: It is used in network analysis to find strongly connected components.
3.  **Maze Solving**: DFS can be used to solve mazes.

## Advantages

1.  **Efficiency**: DFS is efficient for finding connected components in a graph.
2.  **Simplicity**: It is a simple algorithm to implement.

## Disadvantages

1.  **Not Suitable for Finding Shortest Paths**: DFS is not suitable for finding the shortest path in a graph.
2.  **Space Requirements**: The algorithm requires significant space to store the visited nodes.

## How it Works

1.  **Initialization**: The algorithm starts with an initial node and a boolean array to track visited nodes.
2.  **Node Exploration**: The algorithm explores as far as possible along each branch.
3.  **Backtracking**: The algorithm backtracks when it reaches a dead end.

## License

This project is open-source—feel free to use, modify, or distribute it.
