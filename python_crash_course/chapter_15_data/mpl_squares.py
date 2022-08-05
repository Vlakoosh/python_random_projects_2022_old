from re import X
from sqlite3 import SQLITE_DENY
import matplotlib.pyplot as plt

squares = []

for i in range(5):
    squares.append(i ** 2)

fis, ax = plt.subplots()
ax.plot(squares)

plt.show()