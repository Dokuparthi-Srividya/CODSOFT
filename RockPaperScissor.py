import random
import tkinter as tk
window=tk.Tk()
window.geometry("400x350")
window.title("Rock Paper Scissor")

user_score=0
comp_score=0
user_choice=""
comp_choice=""

def choice_to_number(choice):
    rps={"rock":0,"paper":1,"scissor":2}
    return rps[choice]
def number_to_choice(number):
    rps={0:"rock",1:"paper",2:"scissor"}
    return rps[number]


def random_computer_choice():
    return random.choice(["rock","paper","scissor"])

def result(human_choice,comp_choice):
    global user_score
    global comp_score
    user=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)
    if (user==comp):
        print("Tie")
    elif((user-comp)%3==1):
        print("You Win!!")
        user_score +=1
    else:
        print("Computer Wins")
        comp_score +=1
    text_area=tk.Text(master=window,width=30,height=12,bg="#FFFF99")
    text_area.grid(row=6,column=2)
    answer="Your choice:{uc} \n Computer choice:{cc} \n your score:{u}" \
           "\n comp score:{c}".format(uc=user_choice,cc=comp_choice
                                      ,u=user_score,c=comp_score)
    text_area.insert(tk.END,answer)


def Rock():
    global user_choice
    global comp_choice
    user_choice="rock"
    comp_choice=random_computer_choice()
    result(user_choice,comp_choice)
def Paper():
    global user_choice
    global comp_choice
    user_choice = "paper"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)

def Scissor():
    global user_choice
    global comp_choice
    user_choice = "scissor"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)



btn1=tk.Button(text="  Rock  ",width=8,height=2,bg="skyblue",command=Rock)
btn1.grid(row=1,column=0,padx=3,pady=3)
btn2=tk.Button(text="  Paper  ",width=8,height=2,bg="pink",command=Paper)
btn2.grid(row=2,column=0,padx=3,pady=3)
btn3=tk.Button(text="  Scissor  ",width=8,height=2,bg="green",command=Scissor)
btn3.grid(row=3,column=0,padx=3,pady=3)
window.mainloop()
