from tkinter import *
import random
from tkinter import messagebox
import datetime as dt
import unittest as unit


window = Tk()

window.config(background="yellow")
window.geometry("690x500")




#  making function for random numbers


def gettingNumbers():

    num1.insert(0,(random.sample(range(1, 49), 1)))
    num2.insert(0,(random.sample(range(1, 49), 1)))
    num3.insert(0,(random.sample(range(1, 49), 1)))
    num4.insert(0,(random.sample(range(1, 49), 1)))
    num5.insert(0,(random.sample(range(1, 49), 1)))
    num6.insert(0,(random.sample(range(1, 49), 1)))




# resetting the number sequence


def resetting():

    num1Ent.delete(0,END)
    num2Ent.delete(0,END)
    num3Ent.delete(0,END)
    num4Ent.delete(0,END)
    num5Ent.delete(0,END)
    num6Ent.delete(0,END)
    num1.delete(0,END)
    num2.delete(0,END)
    num3.delete(0,END)
    num4.delete(0,END)
    num5.delete(0,END)
    num6.delete(0,END)
    numberGenerate.configure(state="disabled")  # Makes te button unable to use











window = Tk()
window.title("Live Lotto Draw")
window.config(background="yellow")
window.geometry("700x400")

# making the entries for the numbers
num1 = Entry(window, relief='groove', width = 5, bd=4,  fg='white', bg='black')
num1.grid(row = 1, column = 1, padx = 5, pady = 7)
num2 = Entry(window, relief='groove', width = 5, bd=4, fg='white', bg='black')
num2.grid(row = 1, column = 2, padx = 5, pady = 7)
num3 = Entry(window, relief='groove', width = 5, bd=4,  fg='white', bg='black')
num3.grid(row = 1, column = 3, padx = 5, pady = 7)
num4 = Entry(window, relief='groove', width = 5, bd=4,  fg='white', bg='black')
num4.grid(row = 1, column = 4, padx = 5, pady = 7)
num5 = Entry(window, relief='groove', width = 5, bd=4,  fg='white', bg='black')
num5.grid(row = 1, column = 5, padx = 5, pady = 7)
num6 = Entry(window, relief='groove', width = 5, bd=4,  fg='white', bg='black')
num6.grid(row = 1, column = 6, padx = 5, pady = 7)

# making more entries for numbers

num1Ent = Entry(window, relief='groove', width = 5, bd=4,  fg='white', bg='orange')
num1Ent.grid(row = 5, column = 1, padx = 5, pady = 7)
num2Ent = Entry(window, relief='groove', width = 5, bd=4, fg='white', bg='orange')
num2Ent.grid(row = 5, column = 2, padx = 5, pady = 7)
num3Ent = Entry(window, relief='groove', width = 5, bd=4,  fg='white', bg='orange')
num3Ent.grid(row = 5, column = 3, padx = 5, pady = 7)
num4Ent = Entry(window, relief='groove', width = 5, bd=4,  fg='white', bg='orange')
num4Ent.grid(row = 5, column = 4, padx = 5, pady = 7)
num5Ent = Entry(window, relief='groove', width = 5, bd=4,  fg='white', bg='orange')
num5Ent.grid(row = 5, column = 5, padx = 5, pady = 7)
num6Ent = Entry(window, relief='groove', width = 5, bd=4,  fg='white', bg='orange')
num6Ent.grid(row = 5, column = 6, padx = 5, pady = 7)
w = Label(window, text=f"{dt.datetime.now():%a, %b %d %Y}", fg="white", bg="black", font=("helvetica", 11))
w.place(x=500, y=13)


# label to type in

EnterValue=Label(window,text="Enter your  number", relief="groove")
EnterValue.place(x=500, y=315)

# mde the close button
closeButton = Button(window)
closeButton.configure(text = "CLOSE", fg = 'white', bg = 'green')
closeButton.grid(row = 3, column = 1, columnspan = 5, pady = 2)


# number  button and command for making random numbers appear
numberGenerate = Button(window, width=20, text="Generate Numbers", command=gettingNumbers)
numberGenerate.configure(state="disabled",fg = "White" ,bg = "Green")
numberGenerate.grid(row = 2, column = 6, padx = 5, pady = 100)

# reset button and also the command for resetting everything
reset = Button(window, width=10, text="Reset", command =resetting)
reset.configure(fg = "White" ,bg = "Green")
reset.grid(row = 2, column = 2, padx = 5, pady = 100)

# to make the generate number unclickable but only click able once you  entered numbers
def enter():
    numberGenerate.configure(state="normal")

Enter_B=Button(window,text="Finish enter numbers click here" ,command=enter,bg="green",fg="white").place(x=61,y=200)

















def close():
    window.destroy()
    quit()










def compare():
    #lg =generated le=entered
    le=[num1Ent.get(),num2Ent.get(),num3Ent.get(),num4Ent.get(),num5Ent.get(),num6Ent.get()]
    lg=[num1.get(),num2.get(),num3.get(),num4.get(),num5.get(),num6.get()]
    correct=set(le)&set(lg)

    print(len(correct))
    print(str(correct))
    if len(correct) ==0:

        messagebox.showinfo("Hi","you got"+str(len(correct))+ " absolutely nothing")
        file = open('/home/user/Desktop/lotto.txt', 'a')
        file.write(
            "Ampont:" + "absolutley nothing"

        )
    elif len(correct) ==1:
        messagebox.showinfo("Hi","you got"+str(len(correct))+ " try again")
        file=open('/home/user/Desktop/lotto.txt','a')
        file.write( "Amountt:"+"zero " )


    elif len(correct) == 2:
        messagebox.showinfo("Hi","you got"+str(len(correct))+ " one more time")
        file = open('/home/user/Desktop/lotto.txt', 'a')
        file.write( "Amount:" + "R0")

    elif len(correct) == 3:
        messagebox.showinfo("Hi","you got"+str(len(correct))+ " R300")
        file = open('/home/user/Desktop/lotto.txt', 'a')
        file.write( "Amount:" + "R300")

    elif len(correct) == 4:
        messagebox.showinfo("i","you got"+str(len(correct))+ " R800")
        file = open('/home/user/Desktop/lotto.txt', 'a')
        file.write("Amount:" + "R800" )

    elif len(correct) == 5:
        messagebox.showinfo("Hi","you got"+str(len(correct))+ " R19000")
        file = open('/home/user/Desktop/lotto.txt', 'a')
        file.write("Amount:" + "R19000")

    elif len(correct) == 6:
        messagebox.showinfo("Hi","you got"+str(len(correct))+ " R100000")
        file = open('/home/user/Desktop/lotto.txt', 'a')
        file.write( "Amount:" + "R100000" )




check= Button(window, text="See Result",command=compare,bg="green",fg="white").place(x=400, y=280)
closeButton.configure(command = close)

file = open("lottoPract.txt",'r')
file.read(200)
file.read()

window.mainloop()


