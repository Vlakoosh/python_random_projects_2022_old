from ssl import VerifyFlags
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.iconbitmap("cog.ico")
root.title("Python Program")
root.geometry("400x400")

def update(v):
    root.geometry(str(horizontal.get())+"x"+str(vertical.get()))


vertical = Scale(root, from_=100, to=600, command=update)
vertical.set(400)
vertical.grid(row=0,column=0,sticky="NW")

horizontal = Scale(root, from_=100, to=1000, orient=HORIZONTAL, command=update)
horizontal.set(400)
horizontal.grid(row=1,column=0, sticky="NW")







root.mainloop()