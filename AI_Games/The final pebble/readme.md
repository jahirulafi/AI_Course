# 🪨 **The Final Pebble (Minimax AI Game)**

A strategic stone-removal game built in **Python (Tkinter GUI)**, where you play against an **AI opponent powered by the Minimax algorithm**.  
Both you and the AI take turns removing stones — the player who takes the **last stone wins!**

---

## **i. How to Run Your File**

### **Navigate to the Game Folder**
```bash
cd AI-Course/AI_Games/The_Final_Pebble
```

### **Run the Game**
Execute the Python script:
```bash
python final_pebble.py
```

---

## **ii. Software/Library/Framework Requirements**

- **Python**: Version 3.8 or higher  
- **Tkinter**: Comes pre-installed with Python (no need to install separately)  

Optional (for better emoji rendering on some systems):  
- **Windows Terminal or UTF-8 enabled console**

---

## **iii. How to Play the Game**

### 🎮 **Start the Game**
Run the script as described above.  
A simple and clean GUI will open showing a pile of stones.

### **Gameplay Rules**
- The game starts with **20–30 stones** (randomly chosen each round).  
- On your turn, you can take **1, 2, or 3 stones** from the pile by pressing the corresponding button.  
- After your move, the **AI (computer)** will automatically make its move.  
- The player who **takes the last stone wins**.

### **Buttons**
- **Take 1 / Take 2 / Take 3:** Removes the selected number of stones.  
- **New Game:** Automatically appears after each round ends.

---

## **iv. Screenshots of the Game**

### **Game Interface**
*(Example look – replace these links with your screenshots)*




#### **Game Interface**

![Game Interface](https://github.com/user-attachments/assets/971a9830-a100-4cf8-ac70-016506fb50b1)

#### **Player’s Turn**

![Player's Turn](https://github.com/user-attachments/assets/d2d8dc56-8532-44d2-9cec-2b2d976bf5ec)

#### **AI’s Turn**

![AI Turn](https://github.com/user-attachments/assets/b78ecc64-1da0-4b27-a759-936a83fca264)




---

## **v. Algorithm Used**

The AI in this game uses the **Minimax Algorithm**, which is a common decision-making algorithm used in turn-based games.

### 🧠 **How the Algorithm Works:**
1. **Player (Human)** → Tries to *maximize* their chance of winning.  
2. **AI (Computer)** → Tries to *minimize* the player’s chances.  
3. The AI simulates all possible outcomes for the next few turns and chooses the move that guarantees the best final result (win or block player’s win).  

---

### **Key Functions**
- `minimax(stones, maximizing)`: Recursively checks all possible moves and returns the optimal score.  
- `ai_move()`: Uses the Minimax function to determine the best move (taking 1–3 stones).  
- `player_take(x)`: Handles player’s turn and checks if the player has won.  
- `update()`: Updates the stone count and display in the GUI.  

---

## **vi. Features**

✅ Simple and interactive **Tkinter GUI**  
✅ **Dynamic gameplay** — random stone count each round  
✅ **Smart AI** — uses minimax to decide best move  
✅ Displays **AI’s move** and **who wins**  
✅ Option to **restart the game** after finishing  

---

## **vii. Example Gameplay**

| Turn | Action | Stones Left |
|------|---------|--------------|
| Start | 24 stones | 🪨🪨🪨🪨... |
| Player takes 2 | 22 stones left |  |
| AI takes 3 | 19 stones left |  |
| ... | ... | ... |
| AI takes last stone | **AI Wins! 💻** |

---

## **viii. Future Improvements**

- Add **difficulty levels** (Easy / Medium / Hard)  
- Add **sound effects** for each move  
- Add **dark mode / light mode** themes  
- Multiplayer (human vs human) version  

---

## **ix. Developer Notes**

**Language:** Python  
**GUI Framework:** Tkinter  
**AI Algorithm:** Minimax (without Alpha-Beta pruning, since search space is small)  
**Author:** *Md Jahirul Islam*  
**Project Type:** AI Game — Part of AI-Course Mini Projects  
