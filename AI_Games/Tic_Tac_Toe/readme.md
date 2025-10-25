


# **Tic-Tac-Toe with Minimax AI**

A classic Tic-Tac-Toe game implemented in Python using Tkinter, where you can play against an AI opponent powered by the Minimax algorithm.

---

## **i. How to Run the Game**

### **Prerequisites**
- Python 3.x installed on your system

### **Run the Game**
1. Navigate to the game folder:

         cd AI-Course/AI_Games/TicTacToe


2. Execute the Python script:

         python tic_tac_toe.py


---

## **ii. Software Requirements**

- **Python**: Version 3.x or higher
- **Tkinter**: Comes pre-installed with Python (no additional installation needed)

---

## **iii. How to Play the Game**

### **Game Setup**
- You play as **X**
- The computer plays as **O**
- The game starts with an empty 3×3 grid

### **Game Controls**
- Click on any empty square to place your **X**
- The computer will automatically respond with its **O** move
- The game alternates turns until there's a winner or draw

### **Game Rules**
- The first player to get 3 of their marks in a row (horizontally, vertically, or diagonally) wins
- If all squares are filled without a winner, the game ends in a draw

### **Game Outcomes**
- **You win**: When you get 3 X's in a row
- **Computer wins**: When the computer gets 3 O's in a row
- **Draw**: When all squares are filled with no winner

After each game, a message box will appear showing the result, and the board will reset automatically.

---

## **iv. Screenshots**

Here are some visuals of the game:

### **Game Board**
![Image](https://github.com/user-attachments/assets/74c3126c-cd69-4a65-be06-9a722919c0b1)

### **Player's Turn**
![Image](https://github.com/user-attachments/assets/f3559259-c3f8-4179-8337-eca9df881b9e)
### **Computer's Turn**
![Image](https://github.com/user-attachments/assets/aed4246e-9206-4b1f-9a99-70881cc23e50)
### **after compelete game with multiple moves**
![Image](https://github.com/user-attachments/assets/eefa65e4-2816-4f12-a3ad-0b7fac1e98d6)
### **Draw Screen**
![Image](https://github.com/user-attachments/assets/d92f71cd-a685-4b5e-8ad4-2e0e016434ba)
### **New game with multiple moves**
![Image](https://github.com/user-attachments/assets/4e8d4690-dece-4f52-96d2-70430165a2ba)
### **Winning Screen (Player/Computer Wins)**
![Image](https://github.com/user-attachments/assets/0aef7239-dba7-492f-b9cc-0c5b8c20d16c)

---

## **v. Algorithm Used**

The AI opponent uses the **Minimax Algorithm** to make optimal moves.

### **How Minimax Works**:
- **Maximizing Player (Computer)**: Tries to maximize its score (find winning moves)
- **Minimizing Player (Human)**: Tries to minimize the computer's score (block winning moves)
- **Recursive Evaluation**: The algorithm evaluates all possible moves and counter-moves
- **Scoring System**:
  - Computer win: +1
  - Player win: -1
  - Draw: 0

### **Key Functions**:
- `minimax(depth, is_maximizing)`: The core algorithm that evaluates board positions
- `computer_move()`: Determines the best move for the computer
- `check_winner(player)`: Checks if the specified player has won
- `available_moves()`: Returns list of available moves on the board

### **AI Behavior**:
- The computer will always make the optimal move
- It will never lose (can only win or draw)
- Uses depth-first search to evaluate all possible game states

---

## **vi. Game Features**

✅ **Clean GUI Interface** using Tkinter
✅ **Optimal AI Opponent** using Minimax algorithm
✅ **Automatic Game Reset** after each match
✅ **Win/Draw Detection** with pop-up notifications
✅ **Simple Controls** - just click to play
✅ **Responsive Design** that works on all screen sizes

---

**Enjoy playing Tic-Tac-Toe against the unbeatable AI!** 🎮
```
