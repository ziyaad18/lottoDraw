from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Log in")
window.geometry("500x220")
window.config(background="yellow")

valueLab = Label(window, text="Enter age", bg="yellow")
valueLab.pack()
value = Entry(window)
value.pack()
userLab = Label(window, text="Username", bg="yellow")
userLab.pack()

userEnt = Entry(window, textvariable="Username")
userEnt.pack()
passLab = Label(window, text="Password", bg="yellow")
passLab.pack()
passEnt = Entry(window, textvariable="Password", show="*")
passEnt.pack()


def check():
    amount = int(value.get())
    try:
        if amount < 18:
            raise ValueError(messagebox.showinfo('Message', "Get out Adults only"))
        file=open('/home/user/Desktop/lotto.txt','a')
        file.write("Player:" + str(userEnt.get()) + "\n" +
                   "age:" + str(value.get()) + "\n" )

    except ValueError:
        print(ValueError)
        value.delete(0, END)

    else:
        (messagebox.showinfo('Message', "You may enter"))

    logInfo = {"kratos": "god of war", "uncharted": "nathan", "spiderman": "ps5", "Ziyaad": "1234"}
    theuser = userEnt.get()
    password = passEnt.get()
    ageCheck = value.get()

    if (theuser, password) in logInfo.items():
        messagebox.showinfo("INFO", "Correct Login")
        window.withdraw()
        import LottoPract2
        LottoPract2.verify()
        LottoPract2.verify()

    else:
        messagebox.showinfo("Correct info", "Incorrect Login")
        userEnt.delete(0, END)
        passEnt.delete(0, END)


'''def adultsOnly():
'''
'''
verify_age=Button(window,text="Check age", command=adultsOnly,bg="green")
verify_age.pack()
'''

button1 = Button(window, text="Login ", bg="green", command=check, ).pack()
window.mainloop()