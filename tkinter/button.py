from os import stat
from tkinter import *

root = Tk()

# text= is self-explanatory
# state= DISABLED disables the button
# padx= and pady= change the button size
# command= function() makes a button run a function.

def click():
    myLabel = Label(root, text="You clicked a button!")
    myLabel.pack()



# button widget with a disabled state; can't be clicked
disabledButton = Button(root, text="You can't click me!", state=DISABLED)

# defining a button
myButton = Button(root, text="Click me!", padx=50, pady=30, command=click)

# packing stuff on the screen
disabledButton.pack()
myButton.pack()


root.mainloop()