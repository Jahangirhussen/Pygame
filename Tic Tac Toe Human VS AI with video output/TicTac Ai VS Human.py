import tkinter as tk
import random

# উইন্ডো তৈরি
root = tk.Tk()
root.title("Tic-Tac-Toe")

# বোর্ড ডাটা
board = [" "] * 9
buttons = []

# বোর্ড আপডেট ফাংশন
def update_board():
    for i in range(9):
        buttons[i].config(text=board[i], fg="black" if board[i] == "X" else "red")

# জয় চেক ফাংশন
def check_winner():
    win_combinations = [(0,1,2), (3,4,5), (6,7,8),
                        (0,3,6), (1,4,7), (2,5,8),
                        (0,4,8), (2,4,6)]
    for a, b, c in win_combinations:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    if " " not in board:
        return "Draw"
    return None

# বাটন ক্লিক ফাংশন
def on_click(index):
    if board[index] == " ":
        board[index] = "X"
        update_board()
        winner = check_winner()
        if winner:
            show_result(winner)
            return
        computer_move()

# কম্পিউটারের চাল
def computer_move():
    empty_cells = [i for i in range(9) if board[i] == " "]
    if empty_cells:
        move = random.choice(empty_cells)
        board[move] = "O"
        update_board()
        winner = check_winner()
        if winner:
            show_result(winner)

# রেজাল্ট দেখানো
def show_result(winner):
    msg = "Draw!" if winner == "Draw" else f"{winner} Wins!"
    result_label.config(text=msg)
    root.after(2000, reset_board)

# বোর্ড রিসেট
def reset_board():
    global board
    board = [" "] * 9
    update_board()
    result_label.config(text="")

# বোর্ড ডিজাইন
frame = tk.Frame(root)
frame.pack()

for i in range(9):
    btn = tk.Button(frame, text=" ", font=("Arial", 24), width=5, height=2, 
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# রেজাল্ট লেবেল
result_label = tk.Label(root, text="", font=("Arial", 20))
result_label.pack()

root.mainloop()
