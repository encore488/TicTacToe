import tkinter as tk
from tkinter import messagebox
import random

menu_win = tk.Tk()        # Create an instance of tkinter for the main menu
menu_win.geometry('800x500')
menu_win.resizable(False, False)
menu_win.title("Main Menu")
menu_win.config(bg="#2b8e99")

x_click = True    # Initialize variables to make sure x always goes first...
turn_count = 0     # Number of turns taken is reset when game window is closed
x_score = 0        # Scores for X and O are updated and do not change with window being closed
o_score = 0

# Create main menu buttons and place them with pack()
med_play_btn = tk.Button(menu_win, text="Medium", font=("Helvetica", 40), width=36, bg="#b38878",
                       command=lambda: s_game("Medium")) # Play against "random" AI
med_play_btn.pack(side="top", pady=20)

impos_play_btn = tk.Button(menu_win, text="Impossible", font=("Helvetica", 40), width=36, bg="#b38878",
                       command=lambda: s_game("Impossible")) # Play against min/max AI
impos_play_btn.pack(side="top", pady=20)

mult_play_btn = tk.Button(menu_win, text="Multiplayer", font=("Helvetica", 40), width=36, bg="#b38878",
                       command=lambda: s_game("Multiplayer"))  # Play against friend. Take turns
mult_play_btn.pack(side="top", pady=20)

def s_game(gamev):
    global window
    window = tk.Toplevel(menu_win)
# window must be global so it can be destroyed by another function
    window.geometry('800x800')
    window.resizable(False,False)
    window.title("Tic Tac Toe")
    window.config(bg="#2b8e99")

    global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9
# Create buttons and labels for the window
# Padding to keep the grid centered in the window
    pad_1 = tk.Label(window, text=" ", width=8, bg="#2b8e99", fg="#2b8e99")
    menu_btn = tk.Button(window, text="Menu", font=("New Century Schoolbook", 20), width=8, bg="#99662b", command=lambda: main_m(window))
    reset_btn = tk.Button(window, text=" Clear Board ", font=("New Century Schoolbook", 15), width=10, bg="#99662b", command=lambda: reset_game(window))
    score_lbl = tk.Label(window, text=f" X: {x_score}    O: {o_score} ", font=("New Century Schoolbook", 25), bg="#2b8e99")

# When one of these 9 buttons are clicked these 4 commands are executed in the order they are listed
    btn1 = tk.Button(window, text=" ", font=("Helvetica", 40), height=3, width=6, bg="#994a2b",
                     command=lambda: [btn_click(btn1), checkifwon(gamev), play_ai(gamev), checkifwon(gamev)])
# Players click is processed, then check for win/tie, then any AI actions are processed, then check for win/tie

    btn2 = tk.Button(window, text=" ", font=("Helvetica", 40), height=3, width=6, bg="#994a2b",
                     command=lambda: [btn_click(btn2), checkifwon(gamev), play_ai(gamev), checkifwon(gamev)])
    btn3 = tk.Button(window, text=" ", font=("Helvetica", 40), height=3, width=6, bg="#994a2b",
                     command=lambda: [btn_click(btn3), checkifwon(gamev), play_ai(gamev), checkifwon(gamev)])
    btn4 = tk.Button(window, text=" ", font=("Helvetica", 40), height=3, width=6, bg="#994a2b",
                     command=lambda: [btn_click(btn4), checkifwon(gamev), play_ai(gamev), checkifwon(gamev)])
    btn5 = tk.Button(window, text=" ", font=("Helvetica", 40), height=3, width=6, bg="#994a2b",
                     command=lambda: [btn_click(btn5), checkifwon(gamev), play_ai(gamev), checkifwon(gamev)])
    btn6 = tk.Button(window, text=" ", font=("Helvetica", 40), height=3, width=6, bg="#994a2b",
                     command=lambda: [btn_click(btn6), checkifwon(gamev), play_ai(gamev), checkifwon(gamev)])
    btn7 = tk.Button(window, text=" ", font=("Helvetica", 40), height=3, width=6, bg="#994a2b",
                     command=lambda: [btn_click(btn7), checkifwon(gamev), play_ai(gamev), checkifwon(gamev)])
    btn8 = tk.Button(window, text=" ", font=("Helvetica", 40), height=3, width=6, bg="#994a2b",
                     command=lambda: [btn_click(btn8), checkifwon(gamev), play_ai(gamev), checkifwon(gamev)])
    btn9 = tk.Button(window, text=" ", font=("Helvetica", 40), height=3, width=6, bg="#994a2b",
                     command=lambda: [btn_click(btn9), checkifwon(gamev), play_ai(gamev), checkifwon(gamev)])

# Use grid to place buttons on the screen
    pad_1.grid(row=0, column=0)  # Invisible. Pushes all other buttons to the left
    menu_btn.grid(row=0, column=1, pady=20, padx=20)
    reset_btn.grid(row=0, column=3, padx=20, pady=20)
    score_lbl.grid(row=4, column=2, pady=15)
    btn1.grid(row=1, column=1)
    btn2.grid(row=1, column=2)
    btn3.grid(row=1, column=3)
    btn4.grid(row=2, column=1)
    btn5.grid(row=2, column=2)
    btn6.grid(row=2, column=3)
    btn7.grid(row=3, column=1)
    btn8.grid(row=3, column=2)
    btn9.grid(row=3, column=3)

def change_clr(button, color):
    button.configure(background=color)

def btn_click(button):
    global x_click, turn_count
    if button["text"] == " " and x_click == True:   # If button is not taken, assign it an X or O, depending on x_click
        button["text"] = "X"
        x_click = False
        turn_count += 1        # Increment turn to help determine when a tie has occured
    elif button["text"] == " " and x_click == False:
        button["text"] = "O"
        x_click = True
        turn_count += 1
    else:
        change_clr(button, "red")      # Flash red if player clicks a taken button
        button.after(1500, lambda: change_clr(button, "#994a2b"))

def play_ai(gamev):
    if gamev == "Multiplayer":
        pass
    elif gamev == "Medium":
        button_list = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]
        possible_btns = []
        for btn in button_list:
            if btn["text"] == " ":
                possible_btns.append(btn)
        btn_click(random.choice(possible_btns))
    else:
        pass
def checkifwon(gamev):
    global turn_count, x_score, o_score
                        # Has X won?
    if ((btn1["text"] == "X" and btn2["text"] == "X" and btn3["text"] == "X") or
        (btn4["text"] == "X" and btn5["text"] == "X" and btn6["text"] == "X") or
        (btn7["text"] == "X" and btn8["text"] == "X" and btn9["text"] == "X") or
        (btn1["text"] == "X" and btn4["text"] == "X" and btn7["text"] == "X") or
        (btn2["text"] == "X" and btn5["text"] == "X" and btn8["text"] == "X") or
        (btn3["text"] == "X" and btn6["text"] == "X" and btn9["text"] == "X") or
        (btn1["text"] == "X" and btn5["text"] == "X" and btn9["text"] == "X") or
        (btn3["text"] == "X" and btn5["text"] == "X" and btn7["text"] == "X")):
            x_score += 1
            messagebox.showinfo("Tic Tac Toe", "We have a winner! \n X Has Prevailed!")
            reset_game(window)

                        # Has O won?
    elif ((btn1["text"] == "O" and btn2["text"] == "O" and btn3["text"] == "O") or
        (btn4["text"] == "O" and btn5["text"] == "O" and btn6["text"] == "O") or
        (btn7["text"] == "O" and btn8["text"] == "O" and btn9["text"] == "O") or
        (btn1["text"] == "O" and btn4["text"] == "O" and btn7["text"] == "O") or
        (btn2["text"] == "O" and btn5["text"] == "O" and btn8["text"] == "O") or
        (btn3["text"] == "O" and btn6["text"] == "O" and btn9["text"] == "O") or
        (btn1["text"] == "O" and btn5["text"] == "O" and btn9["text"] == "O") or
        (btn3["text"] == "O" and btn5["text"] == "O" and btn7["text"] == "O")):
            o_score += 1
            messagebox.showinfo("Tic Tac Toe", "We have a winner! \n O Is The Victor!")
            reset_game(window)

                    # Or is it a tie?
    elif turn_count == 9:
        messagebox.showinfo("Tic Tac Toe", "It's a tie.\n Nobody Wins This Time")
        reset_game(window)
    else:
        return
    s_game(gamev)  # Start a new game of this type if there is a winner or a tie

def reset_game(window):
    global x_click, turn_count
    window.destroy()
    x_click = True
    turn_count = 0

def main_m(window):
    global x_click, turn_count
    window.destroy()
    x_click = True
    turn_count = 0

def run():
    menu_win.mainloop()

if __name__ == '__main__':
    run()