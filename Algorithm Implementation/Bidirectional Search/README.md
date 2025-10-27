![bidirectional](https://github.com/user-attachments/assets/53e4d327-58cf-40af-a5aa-d3e03b39a775)
# Bidirectional Search Algorithm Implementation in C++

# Bidirectional Search Implementation

## Overview

**Bidirectional Search** is a graph search algorithm that simultaneously searches from the **start node** and the **goal node** until the two searches meet.  
It is efficient for finding the shortest path in large graphs, as it reduces the search space compared to traditional BFS.

## How it Works

1. **Initialization**: Start BFS from both the start and goal nodes.  
2. **Traversal**: Alternate expanding nodes from the front (start) and back (goal) queues.  
3. **Meeting Point**: The search stops when a node is visited by both front and back searches.  
4. **Path Construction**: Reconstruct the path from start to goal via the meeting point.

## Code Structure

### Functions

1.  `bidirectional_search(graph, start, goal)`:
    * Performs bidirectional search on the graph.  
    * Uses two BFS queues and two visited dictionaries to track nodes from both directions.  
    * Returns the shortest path if a connection exists.

2.  `make_path(fv, bv, meet)`:
    * Helper function to reconstruct the path from the front and back visited dictionaries via the meeting node.

3.  `main` (top-level script):
    * Takes user input for:
        - Number of nodes  
        - Node names and their neighbors  
        - Start node  
        - Goal node
    * Builds the graph as a **Python dictionary**.  
    * Calls `bidirectional_search()` and prints the result.

## Sample Execution

### Example Input


This example uses a graph with **6 nodes** and **7 edges**.
![Image](https://github.com/user-attachments/assets/20d24326-ca45-43f2-a62d-719e4d7b6880)
### Explanation

*   The algorithm performs two simultaneous searches: one from node **0** and one from node **5**.
*   The searches meet at node **2** or **4**, indicating a path has been found.

## Complexity

*   **Time Complexity**: O(b^(d/2)), where b is the branching factor, and d is the depth of the search. Bidirectional search can significantly reduce the search space compared to unidirectional search.
*   **Space Complexity**: O(b^(d/2)), as the algorithm needs to store the nodes at each level.

## Applications

1.  **Graph Search**: Bidirectional search is used in graph search problems, such as finding the shortest path between two nodes.
2.  **Network Routing**: It is used in network routing protocols to find the optimal path for data transmission.
3.  **Game Playing**: Bidirectional search can be used in game-playing AI to evaluate game states and make moves.

## Advantages

1.  **Efficiency**: Bidirectional search can significantly reduce the search space, making it more efficient than unidirectional search.
2.  **Scalability**: It is suitable for large graphs or networks.

## Disadvantages

1.  **Complexity**: Implementing bidirectional search can be complex, especially for large graphs.
2.  **Meeting Point**: The algorithm may not always find the optimal meeting point.

## How it Works

1.  **Initialization**: The algorithm starts with two queues and two sets to track visited nodes.
2.  **Node Exploration**: The algorithm explores the neighbors of the current nodes in both searches.
3.  **Termination**: The algorithm terminates when the two searches meet in the middle.

## License

This project is open-source—feel free to use, modify, or distribute it.
