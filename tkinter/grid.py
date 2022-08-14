from tkinter import *

root = Tk()


# Creating a label widget
myLabel1 = Label(root, text = "Hello World!!")
myLabel2 = Label(root, text = "My name is Szymon Walkusz")

#shoving a label widget onto the screen
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=0)


root.mainloop()