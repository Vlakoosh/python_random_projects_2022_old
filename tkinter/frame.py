from tkinter import *
from tkinter.ttk import Labelframe

root = Tk()
root.title('Python Program')
root.iconbitmap("cog.ico")

frame = LabelFrame(root, text="This is a frame",padx=5,pady=5)
frame.pack(padx=10,pady=10)

b  = Button(frame, text="Button")
b.pack()



root.mainloop()