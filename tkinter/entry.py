from os import stat
from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=5)
e.pack()

#initial text in the entry widget
e.insert(0, "*Replace with your name*")


def click():

    #widget.get() allows you to get a value of an Entry widget
    hello = f"Hello {e.get()}"
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter Your Name!", command=click)
myButton.pack()


root.mainloop()