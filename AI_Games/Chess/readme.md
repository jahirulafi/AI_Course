# **Chess Game with Minimax AI**

A classic Chess game implemented in Python using Pygame, where you can play against an AI opponent powered by the Minimax algorithm with Alpha-Beta pruning.

---

## **i. How to Run the Game**

### **Navigate to the Game Folder**
```sh
cd AI-Course/AI_Games/Chess
```

### **Run the Game**
Execute the Python script:
```sh
python chess_game.py
```

---

## **ii. Software/Library/Framework Requirements**

- **Python**: Version 3.8 or higher
- **Pygame**: For rendering the game UI
  ```sh
  pip install pygame
  ```
- **Python-Chess**: For chess logic and rules
  ```sh
  pip install chess
  ```

---

## **iii. How to Play the Game**

### **Game Setup**
- The game starts with the standard chess board setup
- **Player (White)**: Moves first (human player)
- **Computer (Black)**: Uses Minimax AI to make moves

### **Game Controls**
- **Selecting Pieces**:
  - Click on a white piece to select it
  - Valid moves will be highlighted in green
- **Making Moves**:
  - Click on a highlighted square to move your piece
- **Special Moves**:
  - Pawn promotion is handled automatically (promotes to Queen by default)
  - Castling, en passant, and other special moves are supported

### **Game Rules**
- Standard chess rules apply
- The game detects and handles:
  - Checkmate
  - Stalemate
  - Insufficient material
  - 75-move rule
  - Fivefold repetition

### **Game Over Conditions**
- When the game ends, a result screen will show:
  - Who won (Player or Computer)
  - Or if it was a draw (and the reason)
- The game will automatically exit after showing the result

---

## **iv. Screenshots of the Game**

Here are some visuals of the game:
### **Game Board**
![Image](https://github.com/user-attachments/assets/59f9660e-68cf-4465-87e9-a7ec53b39e94)
### **Player's Turn (White)**
![Image](https://github.com/user-attachments/assets/d53720c9-2e42-413b-897c-70371346e6ef)
### **Computer's Turn (Black)**
![Image](https://github.com/user-attachments/assets/96861084-7547-4b09-a967-598667d0c33a)
### **Checkmate **
![Image](https://github.com/user-attachments/assets/e76e18f8-be57-42d5-bc20-45eaacf53738)
### **After compelteting game (Computer/AI_Wins)Screen**
![Image](https://github.com/user-attachments/assets/54b1b599-cba2-4819-a85d-a3ab0ae79dc9)

---

## **v. Algorithm Used**

The AI opponent in this game uses the **Minimax Algorithm with Alpha-Beta Pruning**.

### **How Minimax Works**:
- **Maximizing Player (Computer)**: Tries to maximize its score
- **Minimizing Player (Human)**: Tries to minimize the computer's score
- **Depth-Limited Search**: The AI looks ahead 2 moves (`depth = 2`)
- **Evaluation Function**: Scores the board based on:
  - Piece values (Pawn=1, Knight=3, Bishop=3, Rook=5, Queen=9)
  - Board control
  - Checkmate detection
- **Alpha-Beta Pruning**: Optimizes the search by skipping irrelevant branches

### **Key Functions**:
- `minimax(board, depth, alpha, beta, maximizing)`: Implements the Minimax logic
- `evaluate_board(board)`: Evaluates the board's state
- `ai_move(board)`: Makes the computer's move using Minimax

### **Piece Values**:
| Piece | Value |
|-------|-------|
| Pawn | 1 |
| Knight | 3 |
| Bishop | 3 |
| Rook | 5 |
| Queen | 9 |
| King | 0 (special handling) |

---

## **vi. Game Features**

- **Complete Chess Rules Implementation**:
  - All standard chess moves and special moves
  - Check/checkmate detection
  - Draw conditions (stalemate, insufficient material, etc.)

- **Visual Indicators**:
  - Selected pieces are highlighted
  - Valid moves are shown with green circles
  - Clear board with alternating colors

- **AI Difficulty**:
  - The AI uses depth 2 search which provides a good balance between challenge and performance
  - Alpha-Beta pruning makes the AI efficient

---

**Enjoy playing Chess against the AI!** ♟️
```
