from tkinter import *
from PIL import ImageTk, Image
import random
from tkinter import ttk

you_won=0
comp_won=0

def spin():
    global you_won,comp_won
    
    button_text=spinButton["text"]
    
    if(button_text=="Spin"):
        # generating random and displaying image according to it
        ran_num=random.randint(1,3)
        if ran_num==1:
            comp_label.config(image=rock)
        elif ran_num==2:
            comp_label.config(image=paper)
        elif ran_num==3:
            comp_label.config(image=scissor)
    
        #taking user input through entry box 
        if user_choice.get()=="Rock":
            user_num=1
        elif user_choice.get()=="Paper":
            user_num=2
        elif user_choice.get()=="Scissor":
            user_num=3
    
        if user_num==1:
            player_label.config(image=rock)
        elif user_num==2:
            player_label.config(image=paper)
        elif user_num==3:
            player_label.config(image=scissor)
    
        # building logic for game
        if ran_num==user_num:
            vs_label.config(image=equal)
        elif ran_num==1 and user_num==3:
            vs_label.config(image=you_loose)
            comp_won+=1
        elif ran_num==2 and user_num==1:
            vs_label.config(image=you_loose)
            comp_won+=1
        elif ran_num==3 and user_num==2:
            vs_label.config(image=you_loose)
            comp_won+=1
        else:
            vs_label.config(image=you_win)    
            you_won+=1
        player_label.config(text=f"You\n{you_won}")
        comp_label.config(text=f"Computer\n{comp_won}")
        spinButton.config(text="Play Again")
    else:
        player_label.config(image=player)
        comp_label.config(image=computer)
        vs_label.config(image=vs)
        spinButton.config(text="Spin")          

window = Tk()
window.title("Rock Paper Scissor")
window.geometry("650x500")

#adjusting images size
rock = ImageTk.PhotoImage(Image.open("rock.png").resize((200, 200)))
paper = ImageTk.PhotoImage(Image.open("paper.png").resize((200, 200)))
scissor = ImageTk.PhotoImage(Image.open("scissor.png").resize((200, 200)))
vs = ImageTk.PhotoImage(Image.open("vs.png").resize((200, 200)))
you_win = ImageTk.PhotoImage(Image.open("you_win.png").resize((200, 200)))
you_loose = ImageTk.PhotoImage(Image.open("you_loose.png").resize((200, 200)))
equal = ImageTk.PhotoImage(Image.open("equal.png").resize((200, 200)))
computer = ImageTk.PhotoImage(Image.open("computer.png").resize((200, 200)))
player = ImageTk.PhotoImage(Image.open("player.png").resize((200, 200)))


#all labels and button and combobox
comp_label = Label(image=computer,text=f"Computer\n {comp_won}",compound="top",font=("Helvectia",18,"bold"))
comp_label.grid(row=0, column=0)

vs_label = Label(image=vs)
vs_label.grid(row=0, column=1,padx=20)

player_label = Label(image=player,text=f"You\n{you_won}",compound="top",font=("Helvectia",18,"bold"))
player_label.grid(row=0, column=2)

user_choice=ttk.Combobox(window,values=("Rock","Paper","Scissor"),width=25)
user_choice.current(0)
user_choice.grid(row=3,column=1,pady=(60,30))

spinButton=Button(text="Spin",bg="#00ff00",font=("Helvectia",12,"bold"),activebackground="#00ff00",command=spin)
spinButton.grid(row=4,column=1)

window.mainloop()
