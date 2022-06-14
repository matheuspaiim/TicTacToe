from tkinter import *
import random
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
from zoneinfo import available_timezones



# ____________________GAME OPERATION______________________

def new_game():
    
    global player

    if player == players[0]:
        label_x()
    else:
        label_o()

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#3b3b3b")


def empty_spaces():
    
    global spaces   
    
    spaces = 9
    while spaces >= 0 and spaces <= 9:
        for row in range(3):
            for column in range(3):
                if buttons[row][column]['text'] != "":
                    spaces -= 1
        break            
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


# __________________REUSABLE FUNCTIONS_____________________

def label_x():    
    
   label.config(text=("Vez de "+players[0]), foreground="#e85151")
   
    
def label_o():    
    
    label.config(text=("Vez de "+players[1]), foreground="#3297a8")     
    
    
def bot_move():  
      
    global player
    
    player = players[1]
    label.config(text=("Vez de "+bot), foreground="#3297a8")
    

def player_move(): 
       
    global player
    
    player = players[0]
    label.config(text=("Vez de "+player), foreground="#e85151")    


def bot_win():  
      
    global player, score_o
    
    label.config(text=(bot+" Venceu"), foreground="forestgreen")
    score_o+=1
    score_o_label['text'] = score_o        
 
 
def player_win():   
    
    global player, score_x  
      
    label.config(text=(player+" Venceu"), foreground="forestgreen")
    score_x+=1
    score_x_label['text'] = score_x    


def click():
    human_player(row, column)
    new_game()
    label_x() 
    restarting_score()



def tie():
    
    label.config(text="Empate!", foreground="gold")   
  
     
        
# ___________________DIFFICULTIES_______________________

def human_player(row, column):
    
    
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player
            
            if check_winner() is False:
                bot_move()

            elif check_winner() is True:
                player_win()
                
            elif check_winner() == "Empate":
                tie()

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player_move()
    
            elif check_winner() is True:
                bot_win()
                                          
            elif check_winner() == "Empate":
                tie()

def easy():
    
    new_game()
    
    global player, spaces
    
    while check_winner() is False:
        
        if buttons[row][column]['text'] == "" and check_winner() is False:

            if player == players[0]:

                buttons[random.randrange(3)][random.randrange(3)]['text'] = bots[0]           
                    
                if spaces % 2 == 0:
                    buttons[random.randrange(3)][random.randrange(3)]['text'] = bots[0]
                    print(spaces)
                else:
                    bot_move() 
                    print(spaces)
                           
                if check_winner() is True:
                    player_win()
                    
                elif check_winner() == "Empate":
                    tie()
                    
            else:

                buttons[random.randrange(3)][random.randrange(3)]['text'] = bots[1]
                player_move()            
                
                if player_move():
                    buttons[random.randrange(3)][random.randrange(3)]['text'] = bots[1]
                    print(spaces)
                    
                else:
                    player_move()
                    print(spaces)

                
                if check_winner() is False:
                    player_move()
        
                elif check_winner() is True:
                    bot_win()
                                            
                elif check_winner() == "Empate":
                    tie()
        break
               
def medium():
    new_game()

def hard():
    new_game()

     
# ______________________MAINFRAME______________________

window = Tk()
window.title("TicTacToe")
space = 2
players = ["X", "O"]
bots = ["X", "O"]
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


# ______________________DROPDOWN________________________

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
      
        
# ______________________SCORE__________________________

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
   
def restarting_score():
    
    global score_o, score_x
    score_o = 0
    score_x = 0
    score_o_label['text'] = 0
    score_x_label['text'] = 0   
  
  
# _________________CHOOSE "O" BUTTON_____________________

def clicked_o():  
        
    if player == players[0]:
        click()
    else:
        click()   

icon_o = tk.PhotoImage(file='./assets/o.png')
button_o = ttk.Button(
    window,
    image=icon_o,
    command=clicked_o
)

button_o.place(x=40, y=110)


# ___________________CHOOSE "X" BUTTON_____________________
        
def clicked_x():
        
    if player == players[1]:
        click()
    else:   
        click()

icon_x = tk.PhotoImage(file='./assets/x.png')
button_x = ttk.Button(
    window,
    image=icon_x,
    command=clicked_x
)

button_x.place(x=210, y=110)


# ______________________BOARD(BUTTONS)_______________________

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('Sans-serif', 40, "bold"), width=3, height=1,
                                      command=lambda row=row, column=column: human_player(row, column), bg="#3b3b3b", foreground="white")
        buttons[row][column].grid(row=row, column=column)

window.mainloop()