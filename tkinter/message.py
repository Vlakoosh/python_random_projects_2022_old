from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


root = Tk()
root.iconbitmap("cog.ico")
root.title("Python Program")

#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askyesno("This is my popup!", "Hello World!")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You said Yes!").pack()
    else:
        Label(root, text="You said No!").pack()



Button(root, text="Click me!",command=popup).pack()





root.mainloop()