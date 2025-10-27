![best](https://github.com/user-attachments/assets/066df600-8a56-48aa-b52a-003158fdd596)
# Best-First Search (BFS with Heuristic) Implementation

## Overview

**Best-First Search (BFS with heuristic)** is a graph traversal algorithm that selects nodes to explore based on a heuristic value, representing the estimated cost to reach the goal.  
It is a **greedy search** algorithm that always expands the most promising node first.

## How it Works

1. Start from the given start node.  
2. Use an **open list** to store nodes to explore.  
3. Sort the open list based on heuristic values and pick the node with the lowest heuristic.  
4. Track visited nodes to avoid revisiting.  
5. Stop when the goal node is reached or no nodes are left to explore.

## Code Structure

### Functions

1. `best_first_search(graph, heuristic, start, goal)`:
    * Performs Best-First Search using a heuristic.
    * Parameters:
        - `graph`: adjacency list of the graph  
        - `heuristic`: dictionary of heuristic values  
        - `start`: starting node  
        - `goal`: goal node  
    * Returns: prints the nodes visited in order until the goal is reached.

2. `main` (top-level script):
    * Input graph nodes, neighbors, and heuristic values.  
    * Call `best_first_search()` to execute the search.

## Sample Execution

### Example Input


This example uses a graph with **6 nodes** and **7 edges**, with a beam width of **2**.

![Image](https://github.com/user-attachments/assets/8b445290-b582-4e04-8f71-e87871ead8c5)

### Explanation

*   The heuristic values guide the search: lower values are preferred.
*   The beam width of 2 limits exploration to the top 2 candidates at each step.
*   The algorithm finds the goal node **5** efficiently by pruning less promising paths.

## Complexity

*   **Time Complexity**: O(b^L), where b is the branching factor, and L is the depth of the search. The beam width can significantly reduce the number of nodes evaluated.
*   **Space Complexity**: O(b*L), as the algorithm needs to store the nodes at each level.

## Applications

1.  **Machine Translation**: Beam search is used in machine translation systems to find the best translation by exploring multiple possible translations.
2.  **Speech Recognition**: It is used in speech recognition systems to find the most likely transcription of a spoken sentence.
3.  **Natural Language Processing**: Beam search can be used in NLP tasks such as parsing, named entity recognition, and text summarization.

## Advantages

1.  **Efficiency**: Beam search is more efficient than exhaustive search algorithms, making it suitable for large graphs or trees.
2.  **Flexibility**: It can be used with different heuristics and beam widths to trade off between efficiency and accuracy.

## Disadvantages

1.  **Completeness**: Beam search does not guarantee finding the optimal solution, as it prunes less promising paths.
2.  **Heuristic Quality**: The performance of beam search depends on the quality of the heuristic function.

## How it Works

1.  **Initialization**: The algorithm starts with an initial node and a beam width.
2.  **Node Evaluation**: The algorithm evaluates all possible next nodes based on a heuristic.
3.  **Beam Selection**: The algorithm selects the top `beam_width` nodes to continue exploring.
4.  **Iteration**: The algorithm repeats steps 2-3 until the goal is reached or no more nodes can be explored.

## License

This project is open-source—feel free to use, modify, or distribute it.
