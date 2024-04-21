# IMPORTING MODULES
from tkinter import *
from random import *

def update_names():
    if not player_name_entry.get() or not opponent_name_entry.get():
        error_label.config(text="Please enter both player and opponent names", fg="red")
    else:
        error_label.config(text="")
        player.config(text=playername())
        opponent.config(text=opponentname())


def playername():
    return f"{player_name_entry.get()}'s score"

def opponentname():
    return f"{opponent_name_entry.get()}'s score"

# SETTING UP GUI FOR ROCK PAPER SCISSOR GAME
root = Tk()
root.title("Rock Paper Scissor Game")
root.geometry("1100x1000")

# FIRST FRAME FOR GAME HEADING
frame1 = Frame(root, bg="#1E2761", borderwidth=6, relief=SUNKEN)
frame1.pack(side=TOP, fill=X)

h = PhotoImage(file="h1.png")
hh = Label(frame1, image=h, bg="#1E2761")
hh.place(x=0, y=10)

heading = Label(frame1, text=" ROCK PAPER SCISSOR GAME ", fg="#E3867D", bg="#1E2761",font=("Arial Black", 26, "bold"))
heading.pack(anchor=CENTER, padx=20, pady=20)

# SECOND FRAME FOR ASKING FOR PLAYING GAME
frame2 = Frame(root, borderwidth=6, relief=SUNKEN, bg="#7A2048")
frame2.pack(side=LEFT, fill=Y)

welcoming = Label(frame2, text="WELCOME TO THE GAME! ", fg="#E3867D", bg="#7A2048",font=("Arial Black", 22, "bold"))
welcoming.pack(anchor=CENTER, padx=40, pady=40)

player_name = Label(frame2, text="ENTER NAME FOR PLAYER ", fg="#E3867D", bg="#7A2048",font=("Arial Black", 14, "bold"))
player_name.pack(padx=40, pady=10)

player_value = StringVar()
player_name_entry = Entry(frame2, textvariable=player_value, fg="#330000", bg="#E3867D",font=("Arial Black", 12, "bold"))
player_name_entry.pack(padx=20, pady=20)

opponent_name = Label(frame2, text="ENTER NAME FOR OPPONENT ", fg="#E3867D", bg="#7A2048",font=("Arial Black", 14, "bold"))
opponent_name.pack(padx=40, pady=10)

opponent_value = StringVar()
opponent_name_entry = Entry(frame2, textvariable=opponent_value, fg="#330000", bg="#E3867D",font=("Arial Black", 12, "bold"))
opponent_name_entry.pack(padx=20, pady=20)

error_label = Label(frame2, text="", fg="red", bg="#7A2048", font=("Arial", 12))
error_label.pack(padx=40, pady=10)

colour1 = "#E3867D"
colour2 = "#408EC6"
colour3 = "#7A2048"

play_button = Button(frame2, fg=colour3,bg=colour1,activebackground=colour2,activeforeground=colour3,highlightthickness=2,
                     highlightbackground=colour2,width=18,height=1,border=2,cursor="hand1",text="CLICK HERE TO PLAY",
                     font=("arial", 18, "bold"),command=update_names)
play_button.pack(pady=60, side=BOTTOM)


# THIRD FRAME FOR ACTUAL GAME IMPLEMENTATION
frame3 = Frame(root, bg="#E3867D", borderwidth=6, relief=SUNKEN)
frame3.pack(side=RIGHT, fill=BOTH, expand=True)

rock_img = PhotoImage(file="rockuser.png")
paper_img = PhotoImage(file="paperuser.png")
scissor_img = PhotoImage(file="scissoruser.png")
rockcomp_img = PhotoImage(file="rock.png")
papercomp_img = PhotoImage(file="paper.png")
scissorcomp_img = PhotoImage(file="scissor.png")

user_label = Label(frame3, image=paper_img, bg="#E3867D")
user_label.grid(row=3, column=0)
computer_label = Label(frame3, image=papercomp_img, bg="#E3867D")
computer_label.grid(row=3, column=2)

player_score = Label(frame3, text=0, font=("Arial Black", 60, "bold"), fg="#1E2761", bg="#E3867D")
player_score.grid(row=4, column=0)
opponent_score = Label(frame3, text=0, font=("Arial Black", 60, "bold"), fg="#1E2761", bg="#E3867D")
opponent_score.grid(row=4, column=2)

# PLAYERS SCORECARD
player = Label(frame3, text="", font=("Arial Black", 14, "bold"), fg="#1E2761", bg="#E3867D")
player.grid(row=0, column=0)
opponent = Label(frame3, text="", font=("Arial Black", 14, "bold"), fg="#1E2761", bg="#E3867D")
opponent.grid(row=0, column=2)

msg = Label(frame3, font=("Arial Black", 18, "bold"), fg="#1E2761", bg="#E3867D")
msg.grid(row=9, column=1,padx=50)


def message(icon):
    msg["text"] = icon

def playerscore():
    score = int(player_score["text"])
    score = score + 1
    player_score["text"] = str(score)

def opponentscore():
    score = int(opponent_score["text"])
    score = score + 1
    opponent_score["text"] = str(score)


def checkwin(player, computer):
    if player == computer:
        message("ITS A TIE")
    elif player == "rock":
        if computer == "paper":
            message("YOU LOOSE")
            opponentscore()
        else:
            message("YOU WIN")
            playerscore()
    elif player == "paper":
        if computer == "scissor":
            message("YOU LOOSE")
            opponentscore()
        else:
            message("YOU WIN")
            playerscore()
    elif player == "scissor":
        if computer == "rock":
            message("YOU LOOSE")
            opponentscore()
        else:
            message("YOU WIN")
            playerscore()
    else:
        pass


choose = ['rock', 'paper', 'scissor']

def choices(icon):
    compchoice = choose[randint(0, 2)]
    if compchoice == "rock":
        computer_label.config(image=rockcomp_img)
    elif compchoice == "paper":
        computer_label.config(image=papercomp_img)
    else:
        computer_label.config(image=scissorcomp_img)

    if icon == "rock":
        user_label.config(image=rock_img)
    elif icon == "paper":
        user_label.config(image=paper_img)
    else:
        user_label.config(image=scissor_img)
    checkwin(icon, compchoice)


rock_button = Button(frame3, bg=colour3,fg=colour1,activebackground=colour3,activeforeground=colour3,highlightthickness=2,
    highlightbackground=colour1,width=10,height=1,border=2,cursor="hand1",text="ROCK",font=("arial", 18, "bold"),
    command=lambda: choices("rock"))
rock_button.grid(row=7, column=0, pady=(100, 0),padx=(20, 0))

paper_button = Button(frame3, bg=colour3,fg=colour1,activebackground=colour3,activeforeground=colour3,highlightthickness=2,
    highlightbackground=colour1,width=10,height=1,border=2,cursor="hand1",text="PAPER",font=("arial", 18, "bold"),
    command=lambda: choices("paper"))
paper_button.grid(row=7, column=1, pady=(100, 0), padx=(20, 20))

scissor_button = Button(frame3, bg=colour3,fg=colour1,activebackground=colour3,activeforeground=colour3,highlightthickness=2,
    highlightbackground=colour1,width=10,height=1,border=2,cursor="hand1",text="SCISSOR",font=("arial", 18, "bold"),
    command=lambda: choices("scissor"))
scissor_button.grid(row=7, column=2, pady=(100, 0))

root.mainloop()
