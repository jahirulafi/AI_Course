import tkinter as tk
from tkinter import messagebox
from random import randint

# ---------------- Game Variables ----------------
n = randint(20, 30)
stone_symbol = "🪨"

# ---------------- Minimax Algorithm ----------------
def minimax(stones, maximizing):
    if stones == 0:
        return -1 if maximizing else 1

    if maximizing:
        best = -999
        for take in range(1, min(3, stones) + 1):  # AI/player can take 1–3 stones
            score = minimax(stones - take, False)
            best = max(best, score)
        return best
    else:
        best = 999
        for take in range(1, min(3, stones) + 1):
            score = minimax(stones - take, True)
            best = min(best, score)
        return best


# ---------------- AI Move ----------------
def ai_move():
    global n
    best_score = -999
    best_take = 1

    # ✅ FIXED: AI will now consider taking 1, 2, or 3 stones
    for take in range(1, min(3, n) + 1):
        score = minimax(n - take, False)
        if score > best_score:
            best_score = score
            best_take = take

    n -= best_take
    update()

    if n == 0:
        messagebox.showinfo("Result", f"💻 AI took {best_take} stones.\n💻 AI Wins!")
        reset_game()
    else:
        status.config(text=f"AI took {best_take} stone{'s' if best_take > 1 else ''}. Your turn!")


# ---------------- GUI Functions ----------------
def update():
    lbl.config(text=f"Stones left: {n}\n" + stone_symbol * n)

def player_take(x):
    global n
    if x < 1 or x > min(3, n):
        return

    n -= x
    update()

    if n == 0:
        messagebox.showinfo("Result", "🎉 You Win!")
        reset_game()
        return

    root.after(500, ai_move)

def reset_game():
    global n
    n = randint(20, 30)
    update()
    status.config(text="Your turn!")


# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("The Final Pebble (Minimax AI)")
root.geometry("350x400")
root.config(bg="#2c3e50")

tk.Label(
    root,
    text="🪨 The Final Pebble",
    font=("Arial", 18, "bold"),
    bg="#2c3e50",
    fg="white"
).pack(pady=10)

lbl = tk.Label(
    root,
    font=("Consolas", 16),
    bg="#2c3e50",
    fg="#f1c40f"
)
lbl.pack(pady=10)

status = tk.Label(
    root,
    text="Your turn!",
    bg="#2c3e50",
    fg="#1abc9c",
    font=("Arial", 12)
)
status.pack(pady=5)

frame = tk.Frame(root, bg="#2c3e50")
frame.pack()

for i in range(1, 4):
    tk.Button(
        frame,
        text=f"Take {i}",
        font=("Arial", 12, "bold"),
        bg="#3498db",
        fg="white",
        width=8,
        command=lambda x=i: player_take(x)
    ).grid(row=0, column=i, padx=5)

update()
root.mainloop()
