from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.iconbitmap("cog.ico")
root.title("Python Program")
root.geometry("400x400")

var = IntVar()

#creating a checkbox
#onvalue= and offvalue= set the values that the checkbox outputs in checked and unchecked states

c = Checkbutton(root, text="Check this box!", variable=var, onvalue="on", offvalue="off")
c.pack()






root.mainloop()