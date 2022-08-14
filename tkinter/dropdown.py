from select import select
from tkinter import *
from unittest import BaseTestSuite
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.iconbitmap("cog.ico")
root.title("Python Program")


def update():
    label = Label(root,text=selection.get()).pack()

#Drop Down Boxes

selection = StringVar()
selection.set("Monday")

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

#you can put "*listname" instead of typing out multiple options in the definition
drop = OptionMenu(root, selection, *options)
#drop = OptionMenu(root, variable, "Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturday","Sunday")

drop.pack()


button = Button(root,text="Save Day", command=update).pack()


root.mainloop()