#Importing needed library
from tkinter import *
import random as r
 
#Function to define buttons
def CellButton(frame):
    b=Button(frame,padx=1,bg="#8fece9",width=3,text="   ",font=('Nunito',60,'bold'),relief="sunken",bd=5)
    return b

#Defining window
root=Tk()

#Setting title for window
root.title("Tic-Tac-Toe")

#Setting the icon of the window
root.iconbitmap("icon.ico")

#Setting width and height for game window
root.geometry("800x600")

#Setting background color
root["bg"]="#1593c4"

#Declaring variables
firstPlayer=StringVar()
secondPlayer=StringVar()

#Label for first player X
Label(root,text="First Player [X] :",bg="#1593c4",fg="white",font=("Nunito",15,"bold")).place(x=520,y=20)

#Textbox for first player X
Entry(root,font=("Nunito",15,"bold"),textvariable=firstPlayer).place(x=520,y=55)

#Label for second player O
Label(root,text="Second Player [O] :",bg="#1593c4",fg="white",font=("Nunito",15,"bold")).place(x=520,y=90)

#Textbox for second player O
Entry(root,font=("Nunito",15,"bold"),textvariable=secondPlayer).place(x=520,y=125)

#Label for displaying game result
lblMesage=Label(root,bg="#1593c4",fg="yellow",font=("Nunito",15,"bold"))
lblMesage.place(x=550,y=185)

#Defining Two operators
a=r.choice(['O','X'])

#Setting color for operators X & O
colour={'O':"Black",'X':"Violet"}

#Variable for creating board
board=[[],[],[]]
for i in range(3):
        for j in range(3):
                board[i].append(CellButton(root))
                board[i][j].config(command= lambda row=i,col=j:click(row,col))
                board[i][j].grid(row=i,column=j)
#label for displaying player's turn
label=Label(text="Welcome To Tic-Tac-Toe",font=('Nunito',15,'bold'),bg="#03151C",fg="white")
label.place(x=520,y=450)


#changing operator for the next player
def changeLetter():
    global a
    for i in ['O','X']:
        if not(i==a):
            a=i
            break


#Reset the gameboard
def resetBoard():
    global a
    for i in range(3):
        for j in range(3):
                board[i][j]["text"]=" "
                board[i][j]["state"]=NORMAL
    a=r.choice(['O','X'])


#Check for winning
def checkWinning():
    for i in range(3):
            if(board[i][0]["text"]==board[i][1]["text"]==board[i][2]["text"]==a or board[0][i]["text"]==board[1][i]["text"]==board[2][i]["text"]==a):
                if a == 'X':
                    lblMesage.config(text="'" + firstPlayer.get() + "' is the Winner")
                else:
                    lblMesage.config(text="'" + secondPlayer.get() + "' is the Winner")
                resetBoard()
    if(board[0][0]["text"]==board[1][1]["text"]==board[2][2]["text"]==a or board[0][2]["text"]==board[1][1]["text"]==board[2][0]["text"]==a):
        if a =='X':
         lblMesage.config(text="'"+firstPlayer.get()+"' is the Winner")
        else:
            lblMesage.config(text="'" + secondPlayer.get() + "' is the Winner")
        resetBoard()
    elif(board[0][0]["state"]==board[0][1]["state"]==board[0][2]["state"]==board[1][0]["state"]==board[1][1]["state"]==board[1][2]["state"]==board[2][0]["state"]==board[2][1]["state"]==board[2][2]["state"]==DISABLED):
        lblMesage.config(text="The match is Tied!")
        resetBoard()

def click(row,col):
        board[row][col].config(text=a,state=DISABLED,disabledforeground=colour[a])
        lblMesage.config(text="")
        checkWinning()
        changeLetter()
        if a=='X':
         label.config(text=firstPlayer.get()+"'s Chance")
        else:
         label.config(text=secondPlayer.get() + "'s Chance")


#Run Application
root.mainloop()
