![beam ](https://github.com/user-attachments/assets/a589e2b3-c064-4946-81af-a394c08021d4)
# Beam Search Algorithm Implementation in C++

This program implements the **Beam Search** algorithm, a heuristic search method that explores a graph level by level, keeping only a limited number of the most promising nodes (defined by the "beam width") at each step. It uses heuristics to prioritize nodes and is useful for finding paths in large search spaces where exhaustive search is impractical.


## What is Beam Search?
Beam Search is a variant of Best-First Search that limits the number of nodes expanded at each level to a fixed "beam width." It:
- Explores the graph breadth-first.
- At each level, sorts candidate nodes by their heuristic value (lower is better in this implementation).
- Retains only the top `beam_width` nodes for further expansion.
- Stops if the goal is reached or no more nodes are available.

This reduces memory usage and computation but may not guarantee the optimal path (it's a heuristic approximation).

### How It Works
1. Initialize a queue with the start node.
2. While the queue is not empty:
   - Dequeue all nodes at the current level and collect their successors.
   - If the goal is among them, return it as found.
   - Sort the successors by heuristic value (ascending, assuming lower is better).
   - Select the top `beam_width` (or fewer) successors and enqueue them for the next level.
3. Repeat until the goal is found or no paths remain.
4. The algorithm prunes low-potential branches early, focusing on promising paths guided by heuristics.

This makes it efficient for large or infinite search spaces but incomplete (may miss solutions if beam width is too small).

## Sample Execution
This example uses a graph with 6 nodes (0 to 5), 7 directed edges, and a beam width of 2.

![Image](https://github.com/user-attachments/assets/ace4faa5-e470-47c6-8da0-2dd8a50804a8)


## Time Complexity
- **Worst Case**: O(d * k * b * log(k * b)), where `d` is the depth of the search (levels explored), `k` is the beam width, and `b` is the average branching factor (neighbors per node). This accounts for generating (k * b) successors per level, sorting them (O((k*b) log (k*b))), and doing this for d levels.
- **Average Case**: Often closer to O(d * k * b) in practice if sorting is efficient, making it much faster than BFS (O(b^d)) for large graphs by limiting expansion to k nodes per level.
- **Space Complexity**: O(k * d) in the worst case for storing the queue and paths (this code uses O(k) per level via the queue).


## Applications
- **Natural Language Processing (NLP)**: Used in machine translation (e.g., Google Translate) and speech recognition to generate the most likely sequences while limiting beam width for efficiency.
- **Pathfinding in Large Graphs**: In AI for games or robotics, where full BFS is too slow, to find approximate shortest paths.
- **Puzzle Solving**: For problems like the traveling salesman or scheduling, where exploring all paths is infeasible.
- **Bioinformatics**: Sequence alignment or protein folding predictions, pruning unlikely configurations.
- **Recommendation Systems**: Generating top-k recommendations by beaming through user-item graphs.


## Code Structure
Functions

beam_search(graph, heuristic, start_node, goal_node, beam_width):

Performs Beam Search using a queue and heuristic evaluation.

Parameters:

graph: adjacency list of the graph

heuristic: dictionary of node heuristics

start_node: node to start search from

goal_node: target node to reach

beam_width: maximum nodes to keep at each level

Prints nodes visited in order.

main (top-level script):

Inputs number of nodes, neighbors, heuristic values, start node, goal node, and beam width.

Calls beam_search() to execute the search.


### Steps
1. Save the code as `beam_search.py`.
2. Open a terminal/command prompt and navigate to the directory where the file is saved.
3. Compile the code:
   ```bash
   g++ beam_search.py -o beam_search
   ```
4. Run the executable:
   ```bash
   ./beam_search
   ```

### Explanation
- Nodes: 0 (start) to 5 (goal).
- Heuristics: [10, 8, 5, 7, 2, 0] for nodes 0 to 5 (lower values indicate closer to goal).
- The algorithm explores levels, pruning to the top 2 nodes per level based on heuristics.
- It reaches the goal (node 5) via a path like 0 → 2 → 4 → 5 or similar, depending on sorting and edges.


## Notes
- Nodes are 0-indexed (0 to n-1).
- The graph is directed (edges are one-way: u → v).
- Heuristics should be provided in order for nodes 0 to n-1.
- The algorithm does not reconstruct the full path; it only checks if the goal is reachable and prints it if found.
- Beam width controls exploration: smaller values are faster but may miss paths; larger values approach BFS.


## License
This project is open-source—feel free to use, modify, or distribute it.
