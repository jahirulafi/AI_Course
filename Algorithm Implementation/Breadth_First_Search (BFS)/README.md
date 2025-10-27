![bfs](https://github.com/user-attachments/assets/612d86ef-58b2-4dc3-86f5-7bcaba5a005d)
# Breadth-First Search (BFS) Implementation

## Overview

**Breadth-First Search (BFS)** is a graph traversal algorithm that explores all the neighbors of a node before moving on to their neighbors.  
BFS is commonly used for finding the shortest path in unweighted graphs and for level-order traversal.

## How it Works

1. **Initialization**: Start from the given start node.  
2. **Traversal**: Explore nodes using a queue (FIFO) to visit all neighbors first.  
3. **Visited Tracking**: Keep track of visited nodes to avoid revisiting.  
4. **Termination**: The search stops when all reachable nodes from the starting node are visited.

## Code Structure

### Functions

1.  `bfs(visited, graph, node)`:
    *   Performs **Breadth-First Search** using an explicit queue.
    *   `visited`: List to track visited nodes.  
    *   `graph`: Dictionary representing the adjacency list.  
    *   `node`: Starting node for BFS.  
    *   Prints nodes in the order they are visited.

2.  `main` (top-level script):
    *   Takes user input for:
        - Number of nodes  
        - Node names and their neighbors  
        - Starting node
    *   Builds the graph as a **Python dictionary**.  
    *   Calls `bfs()` and prints the traversal result.

## Sample Execution

### Example Input


This example uses a graph with **6 vertices** and **7 edges**.
![Image](https://github.com/user-attachments/assets/501a46bc-47d5-43ed-8df7-69e0181ebdad)
### Explanation

*   The algorithm starts at node **0** and explores all its neighbors at each depth level.
*   The visited nodes are printed in the order they are traversed.

## Complexity

*   **Time Complexity**: O(V + E), where V is the number of vertices, and E is the number of edges.
*   **Space Complexity**: O(V), as the algorithm needs to store the visited nodes.

## Applications

1.  **Graph Traversal**: BFS is used in graph traversal problems, such as finding connected components.
2.  **Network Analysis**: It is used in network analysis to find the shortest path between two nodes.
3.  **Web Crawling**: BFS can be used in web crawling to traverse the web graph.

## Advantages

1.  **Efficiency**: BFS is efficient for finding the shortest path in an unweighted graph.
2.  **Simplicity**: It is a simple algorithm to implement.

## Disadvantages

1.  **Not Suitable for Weighted Graphs**: BFS is not suitable for finding the shortest path in a weighted graph.
2.  **Space Requirements**: The algorithm requires significant space to store the visited nodes.

## How it Works

1.  **Initialization**: The algorithm starts with an initial node and a queue.
2.  **Node Exploration**: The algorithm explores all the neighbors of the current node.
3.  **Queue Operations**: The algorithm uses queue operations (enqueue and dequeue) to manage the nodes to be visited.

## License

This project is open-source—feel free to use, modify, or distribute it.
