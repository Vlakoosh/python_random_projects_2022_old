from email.mime import image
from sqlite3 import Row
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Photo Viewer')
root.iconbitmap("camera.ico")

img1 = ImageTk.PhotoImage(Image.open("photos/crab.png"))
img2 = ImageTk.PhotoImage(Image.open("photos/glass.png"))
img3 = ImageTk.PhotoImage(Image.open("photos/melon.png"))
img4 = ImageTk.PhotoImage(Image.open("photos/ball.png"))

image_list = [img1,img2,img3,img4]

status = Label(root, text=f"Image 1 of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)


def forward(image_number):
    global image_label
    global button_forward
    global button_back



    image_label.grid_forget()
    image_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == len(image_list):
        button_forward = Button(root,text=">>", state=DISABLED)

    image_label.grid(row=0,column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1,column=2)

    status = Label(root, text=f"Image {image_number} of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2,column=0,columnspan=3, sticky=W+E)

def back(image_number):
    global image_label
    global button_forward
    global button_back

    image_label.grid_forget()
    image_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text="<<", command=lambda: back(), state=DISABLED)

    image_label.grid(row=0,column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1,column=2)

    status = Label(root, text=f"Image {image_number} of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2,column=0,columnspan=3, sticky=W+E)


image_label = Label(root, image=img1)
button_back = Button(root, text="<<", command=lambda: back(), state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

image_label.grid(row=0,column=0,columnspan=3)
button_exit.grid(row=1, column=1, pady=10)
button_back.grid(row=1, column=0)
button_forward.grid(row=1, column=2)
status.grid(row=2,column=0,columnspan=3, sticky=W+E)









root.mainloop()