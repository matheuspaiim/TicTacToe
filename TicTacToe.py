from tkinter import *
import random
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont



# GAME OPERATION

def new_game():
    
    global players

    label.config(text="Vez de "+player)
    if player == players[0]:
        label.config(text=("Vez de "+players[0]), foreground="#e85151")
    else:
        label.config(text=("Vez de "+players[1]), foreground="#3297a8")
    

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
    
    global player, bot, score_o, score_x, score_x_label, score_o_label

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player
            
            if check_winner() is False:
                player = players[1]
                label.config(text=("Vez de "+players[1]), foreground="#3297a8")

            elif check_winner() is True:
                label.config(text=(players[0]+" Venceu"), foreground="forestgreen")
                score_x+=1
                score_x_label['text'] = score_x
                
            elif check_winner() == "Empate":
                label.config(text="Empate!", foreground="gold")

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=("Vez de "+players[0]), foreground="#e85151")

            elif check_winner() is True:
                label.config(text=(players[1]+" Venceu"), foreground="forestgreen")
                score_o+=1
                score_o_label['text'] = score_o
                                          
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
bot = "O"
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
label = Label(text="Vez de "+ player, font=('Sans-serif', 20, 'bold'), foreground="#e85151")
label.grid(pady=70)


reset_button = Button(window, text="Restart", font=(
    'Sans-serif', 10, 'bold'), padx=5, pady=3 , command=new_game)
reset_button.place(x=215, y=29)

frame = Frame(window)
frame.grid()

# DROPDOWN

tkvar = StringVar(window)
choices = ["Fácil", "Médio", "Difícil", "Jogar com um amigo"]
tkvar.set(choices[3]) # SET THE DEFAULT OPTION

sans_serif = tkFont.Font(family='Sans-serif', size=10, weight="bold")

popupMenu = OptionMenu(window, tkvar, *choices)
popupMenu.config(font=sans_serif, padx=6, pady=6)
popupMenu.place(x=30, y=27)



def change_dropdown(*choices):
    
    choices = tkvar.get()
    
    if choices == "Fácil":
        easy()
    elif choices == "Médio":
        medium()
    elif choices == "Difícil":
        hard()
    elif choices == "Jogar com um amigo":
        human_player(row, column)
        new_game()
           
    
tkvar.trace('w', change_dropdown)
        
# CHOOSE O BUTTON 

score_o = 0
score_x = 0

score_o_label = Label(window, text="0", font=(
    'Sans-serif', 20, 'bold'))
score_o_label.place(x=120, y=120)  
score_x_label = Label(window, text="0", font=(
    'Sans-serif', 20, 'bold'))
score_x_label.place(x=173, y=120)   
score_break = Label(window, text=":", font=(
    'Sans-serif', 20, 'bold'))
score_break.place(x=149, y=118)  
  
  
def clicked_o():  
    global score_o, score_x, score_x_label, score_o_label
    
    if player == players[0]:
        human_player(row, column)
        new_game()
        label.config(text=("Vez de "+players[1]), foreground="#3297a8")
        score_o = 0
        score_x = 0
        score_o_label['text'] = 0
        score_x_label['text'] = 0
    else:
        human_player(row, column)
        new_game()    
        label.config(text=("Vez de "+players[1]), foreground="#3297a8")    
        score_o = 0
        score_x = 0
        score_o_label['text'] = 0
        score_x_label['text'] = 0
        
        

icon_o = tk.PhotoImage(file='./assets/o.png')
button_o = ttk.Button(
    window,
    image=icon_o,
    command=clicked_o
)

button_o.place(x=40, y=110)

# CHOOSE X BUTTON
        
def clicked_x():
    global score_o, score_x, score_x_label, score_o_label
    
    if player == players[1]:
        human_player(row, column)
        new_game()
        label.config(text=("Vez de "+players[0]), foreground="#e85151")
        score_o = 0
        score_x = 0
        score_o_label['text'] = 0
        score_x_label['text'] = 0
    else:      
        human_player(row, column)
        new_game()  
        label.config(text=("Vez de "+players[0]), foreground="#e85151") 
        score_o = 0
        score_x = 0
        score_o_label['text'] = 0
        score_x_label['text'] = 0
        

icon_x = tk.PhotoImage(file='./assets/x.png')
button_x = ttk.Button(
    window,
    image=icon_x,
    command=clicked_x
)

button_x.place(x=210, y=110)


# BOARD (BUTTONS)

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('Sans-serif', 40, "bold"), width=3, height=1,
                                      command=lambda row=row, column=column: human_player(row, column), bg="#3b3b3b", foreground="white")
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
