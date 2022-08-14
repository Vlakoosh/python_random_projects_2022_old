from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.iconbitmap("cog.ico")
root.title("Python Program")

#r = IntVar()
#r.get() to get current value of the variable
#r.set() to set current value of the variable

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Ham", "Ham"),
    ("Pineapple", "Pineapple"),
    ("Onion", "Onion"),
    ("Mozzarella", "Mozzarella")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
    label = Label(root, text=value).pack()


#Radiobutton(root, text="Option 1", variable=r, value=1, command= lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command= lambda: clicked(r.get())).pack()

button = Button(root, text="Click me!", command= lambda: clicked(pizza.get())).pack()



root.mainloop()