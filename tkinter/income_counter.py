from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

try:
    with open('cash_amount.txt', 'r') as file:
        cash = int(file.readline())
except:
    with open('cash_amount.txt', 'w') as file:
        file.write("0")
        cash = 0



root = Tk()
root.title("Money counter")

def change_amount(amount):
    global cash
    cash += amount
    money_label = Label(text=str(cash), font=("Times New Roman", 40, "italic"))
    money_label.grid(row=1, column=0, columnspan=2)
    with open('cash_amount.txt', 'w') as file:
        file.write(str(cash))

def reset():
    global cash
    cash = 0
    with open('cash_amount.txt', 'w') as file:
        file.write(str("0"))

add_one_button = Button(root, text="+1", padx=40, command=lambda:change_amount(1))
add_ten_button = Button(root, text="+10",padx=38, command=lambda:change_amount(10))

remove_one_button = Button(root, text="-1", padx=42, command=lambda:change_amount(-1))
remove_ten_button = Button(root, text="-10",padx=40, command=lambda:change_amount(-10))

reset_button = Button(root, text="Reset", padx=70, command=reset)

money_label = Label(text=str(cash), font=("Times New Roman", 40, "italic"))

add_one_button.grid(row=0, column=0)
add_ten_button.grid(row=0, column=1)

remove_one_button.grid(row=2, column=0)
remove_ten_button.grid(row=2, column=1)

money_label.grid(row=1, column=0, columnspan=2)
reset_button.grid(row=3, column=0, columnspan=2)



root.mainloop()