from secrets import choice
from tkinter import *
import random
import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD

# GAME OPERATION

def new_game():
    global player 

    label.config(text="Vez de - "+ player)

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#3b3b3b")


def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True
    

def check_winner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="forestgreen")
            buttons[row][1].config(bg="forestgreen")
            buttons[row][2].config(bg="forestgreen")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="forestgreen")
            buttons[1][column].config(bg="forestgreen")
            buttons[2][column].config(bg="forestgreen")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="forestgreen")
        buttons[1][1].config(bg="forestgreen")
        buttons[2][2].config(bg="forestgreen")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="forestgreen")
        buttons[1][1].config(bg="forestgreen")
        buttons[2][0].config(bg="forestgreen")
        return True

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="gold")
        return "Empate"

    else:
        return False


# DIFFICULTIES

def human_player(row, column):

    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=("Vez de - "+players[1]), foreground="mediumblue")

            elif check_winner() is True:
                label.config(text=(players[0]+" - Venceu"), foreground="forestgreen")

            elif check_winner() == "Empate":
                label.config(text="Empate!", foreground="gold")

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=("Vez de - "+players[0]), foreground="red")

            elif check_winner() is True:
                label.config(text=(players[1]+" - Venceu"), foreground="forestgreen")

            elif check_winner() == "Empate":
                label.config(text="Empate!", foreground="gold")

def easy():
    new_game()
     
def medium():
    new_game()

def hard():
    new_game()


# MAINFRAME

window = Tk()
window.title("TicTacToe")
players = ["X", "O"]
player = "X"
bot = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]


label = Label(text="Vez de - "+ player, font=('Sans-serif', 30), foreground="red")
label.grid(row=1, pady=70)

reset_button = Button(window, text="Restart", font=(
    'Sans-serif', 10), command=new_game)
reset_button.place(x=50, y=137)

frame = Frame(window)
frame.grid()

# DROPDOWN

tkvar = StringVar(window)
choices = ["Fácil", "Médio", "Difícil", "Jogar contra um amigo"]
tkvar.set(choices[0]) # SET THE DEFAULT OPTION
popupMenu = OptionMenu(window, tkvar, *choices)
Label(window, text="Escolha a dificuldade:").place(x=120, y=140)
popupMenu.place(x=280, y=136)

def change_dropdown(*choices):
    
    choices = tkvar.get()
    
    if choices == "Fácil":
        easy()
    elif choices == "Médio":
        medium()
    elif choices == "Difícil":
        hard()
    elif choices == "Jogar contra um amigo":
        human_player(row, column)
        new_game()
           
    
tkvar.trace('w', change_dropdown)
        
# CHOOSE O BUTTON 

Label(window, text="Escolha o jogador:", font=(
    'Sans-serif')).place(x=70, y=30)
score_o = Label(window, text="0", font=(
    'Sans-serif')).place(x=327, y=30)  
score_x = Label(window, text="0", font=(
    'Sans-serif')).place(x=428, y=30)  
    
def clicked_o():  
    
    if player == players[0]:
        label.config(text=("Vez de "+players[1]), foreground="mediumblue")
        human_player(row, column)
        new_game()

icon_o = tk.PhotoImage(file='./assets/o.png')
button_o = ttk.Button(
    window,
    image=icon_o,
    command=clicked_o
    
)

button_o.place(x=260, y=15)

# CHOOSE X BUTTON
        
def clicked_x():
    
    if player == players[1]:
        label.config(text=("Vez de "+players[0]), foreground="red")
        human_player(row, column)
        new_game()

icon_x = tk.PhotoImage(file='./assets/x.png')
button_x = ttk.Button(
    window,
    image=icon_x,
    command=clicked_x
)

button_x.place(x=360, y=15)


# BOARD (BUTTONS)

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('Sans-serif', 40), width=5, height=2,
                                      command=lambda row=row, column=column: human_player(row, column), bg="#3b3b3b", foreground="white")
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
