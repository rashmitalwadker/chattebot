from tkinter import *
import random
root = Tk()
root.title("Chat Bot")
root.geometry('500x300+100+100')
botsay = StringVar()


hellow = ['hello','hi there','is there any one?']
bye = ['bye','see you later','good bye','thanks bye','have a good day']
howryou = ['how r u ?','how r u doing ?']
name = ['what is your name?','is there any other name of yours?','what shuld i call you from name?']
menu = ['what is in your menu list']
hours = ['what r u guys open ?','hours for operations ?','what is time now?']
print('***************************************************************************************\n')
userInput = str("")
def chat():

    if userInput.get().lower() in hellow:
        botan = ['hello','hi there','hi','welcome']
        botsay.set(random.choice(botan))

    elif userInput.get().lower() in bye:
        botan = ['sad in :)','bye','miss you']
        botsay.set(random.choice(botan))

    elif userInput.get().lower() in howryou:
        botan = ['fine','happy to see you:)','happy']
        botsay.set(random.choice(botan))


    elif userInput.get().lower() in name:
        botan = ['my name is Tv bot','you can call me Tv bot']
        botsay.set(random.choice(botan))

    else:
        botsay.set("sorry what say")

head= Label(root,text= "Chat Bot",background=("blue"),font=("times new roman",20))
head.place(x=200,y=10)

holder = Frame(root)
holder.place(x=80,y=100)

userText = Label(holder,text="Input -",font=("times new roman",15))
userText.grid(row=0,column=0)

userInput = Entry(holder,font=("times new roman",15))
userInput.grid(row=0,column=1)

submitBtn = Button(holder,text="submit",font=("times new roman",15),command=chat)
submitBtn.grid(row=0,column=2)

botText = Label(holder,text="Bot -",font=("times new roman",15))
botText.grid(row=1,column=0,pady=50)

botOutput = Entry(holder,textvariable=botsay,font=("times new roman",15))
botOutput.grid(row=1,column=1)


root.mainloop()