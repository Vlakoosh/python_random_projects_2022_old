from re import X
from sqlite3 import SQLITE_DENY
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
values = [1, 2, 3, 4, 5]

plt.style.use('seaborn')
fis, ax = plt.subplots()
ax.plot(values, squares, linewidth=3)

#Deifining the witle and labels for the axis
ax.set_title("Squares of numbers")
ax.set_xlabel("Number", fontsize=14)
ax.set_ylabel("Square of number", fontsize= 14)

#Defining the size of the labels
ax.tick_params(axis='both', labelsize=14)

plt.show()