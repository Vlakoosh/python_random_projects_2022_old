from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Test Program')
root.iconbitmap("cog.ico")

my_image = ImageTk.PhotoImage(Image.open("python.png"))

my_label = Label(root, image=my_image)
my_label.pack()











exit_button = Button(root, text= 'Exit Program', command=root.quit)
exit_button.pack()





root.mainloop()