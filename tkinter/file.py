from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.iconbitmap("cog.ico")
root.title("Python Program")

root.filename = filedialog.askopenfilename(initialdir="/Szymon/Python/tkinter",title="Select a file!", filetypes=(("png files", "*.png"),("python files", "*.py")))
my_label = Label(root, text=root.filename).pack()





root.mainloop()