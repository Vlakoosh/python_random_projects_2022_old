from tkinter import *

root = Tk()
root.iconbitmap("cog.ico")

frame = LabelFrame(root)
frame.pack(padx=30,pady=30)

#frame.title(text) changes the window title
root.title("Simple Calculator")

e = Entry(frame, width=35, borderwidth=5)
e.grid(row=0,column=0,columnspan=3, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    
    e.insert(0, f"{current}{number}")

def clear_button():
    e.delete(0,END)

def equal_button():
    second_number = e.get()
    e.delete(0,END)

    #f_num + int(second_number)

    if math == 'add':
        answer = f_num + int(second_number)
    elif math == 'sub':
        answer = f_num - int(second_number)
    elif math == 'mul':
        answer = f_num * int(second_number)
    elif math == 'div':
        answer = f_num / int(second_number)

    e.insert(0, answer)

def add_button():
    first_number = e.get()
    global f_num
    global math
    math = "add"
    f_num = int(first_number)
    e.delete(0,END)

def subtract_button():
    first_number = e.get()
    global f_num
    global math
    math = "sub"
    f_num = int(first_number)
    e.delete(0,END)

def multiply_button():
    first_number = e.get()
    global f_num
    global math
    math = "mul"
    f_num = int(first_number)
    e.delete(0,END)

def divide_button():
    first_number = e.get()
    global f_num
    global math
    math = "div"
    f_num = int(first_number)
    e.delete(0,END)

#define the buttons

button_0 = Button(frame, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_1 = Button(frame, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(frame, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(frame, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(frame, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(frame, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(frame, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(frame, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(frame, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(frame, text="9", padx=40, pady=20, command=lambda: button_click(9))

button_add = Button(frame, text="+", padx=39, pady=20, command=add_button)
button_equal = Button(frame, text="=", padx=86, pady=20, command=lambda: equal_button())
button_clear = Button(frame, text="Clear", padx=77, pady=20, command=clear_button)

button_subtract = Button(frame, text="-", padx=40, pady=20, command=subtract_button)
button_multiply = Button(frame, text="x", padx=40, pady=20, command=multiply_button)
button_divide = Button(frame, text="/", padx=40, pady=20, command=divide_button)

#put the buttons on the screen

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_clear.grid(row=4,column=1, columnspan=2)
button_equal.grid(row=5,column=1, columnspan=2)

button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)


root.mainloop()