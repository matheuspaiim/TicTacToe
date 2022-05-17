from tkinter import *
import random
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from numpy import pad

def next_turn(row, column):

    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=("Vez de "+players[1]))

            elif check_winner() is True:
                label.config(text=(players[0]+" Venceu"))

            elif check_winner() == "Empate":
                label.config(text="Empate!")

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=("Vez de "+players[0]))

            elif check_winner() is True:
                label.config(text=(players[1]+" Venceu"))

            elif check_winner() == "Empate":
                label.config(text="Empate!")


def check_winner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Empate"

    else:
        return False


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


def new_game():

    global player

    player = random.choice(players)

    label.config(text="Vez de "+player)

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")


window = Tk()
window.title("TicTacToe")
players = ["X", "O"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text="Vez de "+player, font=('consolas', 40))
label.grid(row=1, pady=60)

reset_button = Button(window, text="restart", font=(
    'consolas', 10), command=new_game)
reset_button.place(x=50, y=137)



tkvar = StringVar(window)
choices = ['Fácil','Médio','Difícil', 'Jogar contra um amigo']
tkvar.set('Fácil') # set the default option

popupMenu = OptionMenu(window, tkvar, *choices)
Label(window, text="Escolha a dificuldade:").place(x=140, y=140)
popupMenu.place(x=280, y=135)

def change_dropdown(*args):
    print( tkvar.get() )
    
tkvar.trace('w', change_dropdown)
        
    
def download_clicked_o():
    pass
        
def download_clicked_x():
    pass
    
Label(window, text="Escolha o jogador:").place(x=100, y=30)

download_icon_o = tk.PhotoImage(file='./assets/o.png')
download_button_o = ttk.Button(
    window,
    image=download_icon_o,
    command=download_clicked_o
)


download_button_o.place(x=250, y=15)

download_icon_x = tk.PhotoImage(file='./assets/x.png')
download_button_x = ttk.Button(
    window,
    image=download_icon_x,
    command=download_clicked_x
)

download_button_x.place(x=330, y=15)


frame = Frame(window)
frame.grid()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
