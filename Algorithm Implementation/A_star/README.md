![astar](https://github.com/user-attachments/assets/babbc876-0536-4613-81db-dc0089bb65dc)

# A* Search Algorithm Implementation in Python

## Overview

This program implements the **A* Search** algorithm in Python, a popular pathfinding method that finds the shortest path from a start node to a goal node in a weighted graph. It combines Dijkstra's algorithm with heuristics to efficiently guide the search toward the goal.

## What is A* Search?

A* is an informed search algorithm that uses:

* **g(n)**: The actual cost from the start node to the current node `n`.
* **h(n)**: A heuristic estimate of the cost from `n` to the goal (must be admissible, i.e., never overestimate).
* **f(n) = g(n) + h(n)**: The total estimated cost, used to prioritize nodes.

The algorithm explores nodes with the lowest `f(n)` first and stops when the goal is reached or no path exists.

## Code Structure

### Variables

1. `graph`: Dictionary to store adjacency list with edge costs.
2. `heuristic`: Dictionary to store heuristic values for each node.
3. `open_list`: List of nodes to explore along with their current g-cost.
4. `visited`: Dictionary to track visited nodes and their g-costs.

### Main Execution

* Input the number of nodes, their neighbors with edge costs, and heuristic values.
* Input the start and goal nodes.
* Use a loop to implement A* search, selecting the node with the lowest `f(n)` at each step.
* Print the nodes in the order they are visited.

## How it Works

1. **Initialization**: Start with the open list containing the start node with g-cost 0.
2. **Node Selection**: Choose the node with the smallest `f(n) = g(n) + h(n)` from the open list.
3. **Goal Check**: If the selected node is the goal, stop the search.
4. **Neighbor Exploration**: For each neighbor, calculate the new g-cost and add it to the open list if it hasn't been visited.

## Complexity

* **Time Complexity**: O(b^d), where b is the branching factor and d is the depth of the search.
* **Space Complexity**: O(b^d), as all nodes may need to be stored in the worst case.

## Applications

1. **Pathfinding**: Used in video games, robotics, and logistics.
2. **Network Routing**: Finds optimal paths in networks.
3. **Resource Allocation**: Optimizes resource usage in complex systems.

## Advantages

1. **Optimality**: Guarantees the shortest path if the heuristic is admissible.
2. **Efficiency**: More efficient than uninformed searches like BFS and DFS.

## Disadvantages

1. **Heuristic Quality**: Performance depends on the accuracy of the heuristic.
2. **Computational Cost**: Can be expensive for large graphs.

## Example Use Cases

1. **Video Games**: Pathfinding for characters and NPCs.
2. **Autonomous Vehicles**: Planning routes and avoiding obstacles.
3. **Logistics and Supply Chain**: Optimizing delivery routes.

## License

This project is open-source — feel free to use, modify, or distribute it.
