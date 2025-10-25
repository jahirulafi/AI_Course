# Algorithm Implementations Repository

This repository contains C++ implementations of various classic search and game theory algorithms. Each algorithm is in its own folder, including source code, a sample execution image, and a dedicated README.md with details on functionality, complexity, applications, and usage.

These implementations are designed for educational purposes, demonstrating key concepts in AI, graph traversal, and decision-making. They assume basic graph structures (adjacency lists or matrices) and handle inputs via stdin.

## List of Algorithms

| Algorithm | Description | Folder |
|-----------|-------------|--------|
| **A* Search** | Informed search using heuristics for optimal pathfinding in weighted graphs. | [A* Algorithm](./AO%20Algorithm) / [A star](./A%20star) |
| **Alpha-Beta Pruning** | Optimized Minimax for game trees, pruning unnecessary branches. | [Alpha-Beta Pruning](./Alpha-Beta%20Pruning) |
| **Beam Search** | Heuristic search limiting expansion to a "beam width" for efficiency in large spaces. | [BEAM search](./BEAM%20search) |
| **Best-First Search** | Greedy search prioritizing nodes by heuristic for approximate solutions. | [Best_First_Search](./Best_First_Search) |
| **Bidirectional Search** | Dual BFS from start and goal to meet in the middle for faster path detection. | [Bidirectional Search](./Bidirectional%20Search) |
| **Breadth-First Search (BFS)** | Level-order traversal for shortest paths in unweighted graphs. | [Breadth_First_Search (BFS)](./Breadth_First_Search%20(BFS)) |
| **Depth-First Search (DFS)** | Depth-oriented traversal using recursion for path exploration. | [Depth_First_Search](./Depth_First_Search) |
| **Depth-Limited Search (DLS)** | DFS with a depth bound to prevent infinite recursion. | [Depth_Limited_Search](./Depth_Limited_Search) |
| **Iterative Deepening DFS (IDDFS)** | Incremental DLS for optimal depth-first search with low memory. | [Iterative_Deepening_DFS (IDDFS)](./Iterative_Deepening_DFS%20(IDDFS)) |
| **Minimax** | Decision-making for two-player games, alternating min and max values. | [MINI_MAX_algorithm](./MINI_MAX_algorithm) |

Each folder includes:
- **Source Code**: A `.py` file with the algorithm implementation.
- **Sample Image**: A screenshot of input/output for a test case.
- **README.md**: Detailed explanation, including how it works, time/space complexity, applications, compilation instructions, and notes.

## How to Use
1. Clone the repository: `git clone <repo-url>`.
2. Navigate to a specific algorithm's folder.
3. Compile the C++ file: `g++ <filename>.py -o <output>`.
4. Run: `./<output>` and provide inputs as prompted.
5. Refer to the folder's README for sample inputs/outputs and explanations.

## Prerequisites
- python compiler
- Basic understanding of graphs and search algorithms.

## Contributing
Feel free to submit pull requests for improvements, bug fixes, or additional algorithms. Ensure new additions follow the structure (code + README + sample image).

## License
This project is open-source under the MIT License—feel free to use, modify, or distribute.
