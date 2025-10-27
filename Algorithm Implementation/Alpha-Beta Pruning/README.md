![alphabeta](https://github.com/user-attachments/assets/c1849ae6-343b-4d5f-909f-d10041e334b6)
# Alpha-Beta Pruning Algorithm Implementation in Python

## Overview

This program implements the **Alpha-Beta Pruning** algorithm in Python, an optimization of the Minimax algorithm for searching game trees. It reduces the number of nodes evaluated by "pruning" branches that cannot impact the final decision, making the search more efficient.

## What is Alpha-Beta Pruning?

Alpha-Beta pruning is a search algorithm that minimizes redundant computations in the Minimax algorithm (used for turn-based games). It uses two values:

* **alpha**: The best (highest) value the maximizing player can guarantee at the current level or above.
* **beta**: The best (lowest) value the minimizing player can guarantee at the current level or above.

If `beta ≤ alpha` at any node, the current branch is pruned, as it cannot improve the final result.

## Code Structure

### Variables

1. `tree`: Dictionary to represent the game tree (nodes and their children).
2. `utilities`: Dictionary storing utility values for leaf nodes.
3. `pruned_nodes`: List to track nodes that were pruned.
4. `prune_count`: Counter for the number of prunings.

### Functions

1. `alphabeta(node, depth, alpha, beta, path)`:
   * Recursively traverses the game tree and applies Alpha-Beta pruning.
   * `node`: Current node being evaluated.
   * `depth`: Current depth in the tree.
   * `alpha`, `beta`: Current alpha and beta values.
   * `path`: Tracks the decision path.
   * Returns the optimal value and path from the root to the evaluated node.

### Main Execution

* Inputs number of nodes, node names, their children, and utility values for leaves.
* Prompts for root node of the game tree.
* Calls `alphabeta()` to compute the optimal value.
* Prints the optimal value, decision path, total prunings, and pruned nodes.

## How it Works

1. **Initialization**: Start with alpha = -∞, beta = ∞.
2. **Node Evaluation**: Evaluate each node recursively.
3. **Pruning**: If `beta ≤ alpha`, remaining child nodes of the current branch are skipped.
4. **Recursion**: Continue until leaf nodes are reached, propagating optimal values upward.

## Complexity

* **Time Complexity**: O(b^(h/2)), where b is the branching factor and h is the height of the tree. Alpha-Beta pruning reduces the number of nodes evaluated compared to Minimax.
* **Space Complexity**: O(h), due to recursion stack.

## Applications

1. **Game Playing**: Chess, checkers, tic-tac-toe, and other turn-based games.
2. **Decision Making**: Optimize choices in decision-making systems.
3. **Resource Allocation**: Efficient exploration of possible actions in complex systems.

## Advantages

1. **Efficiency**: Reduces number of nodes evaluated.
2. **Optimality**: Finds the optimal solution if the evaluation function is accurate.

## Disadvantages

1. **Implementation Complexity**: More complex to implement than basic Minimax.
2. **Evaluation Dependence**: Performance depends on the quality of utility values.

## Example Use Cases

1. **Game AI**: Implementing AI opponents in board games.
2. **Simulation**: Exploring optimal strategies in simulations.
3. **Optimization Problems**: Efficiently pruning non-beneficial options.

## License

This project is open-source — feel free to use, modify, or distribute it.
