import matplotlib.pyplot as plt
import numpy as np



def one(x,y):
    return (0., 0.16*y)
def two(x,y):
    return (0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6)
def three(x,y):
    return (0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6)
def four(x,y):
    return (-0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44)
functions = [one, two, three, four]

points = 1000000
x, y = 0, 0
x_list = []
y_list = []
for i in range(points):
    function = np.random.choice(functions, p=[0.01, 0.85, 0.07, 0.07])
    x, y = function(x,y)
    x_list.append(x)
    y_list.append(y)


plt.scatter(x_list, y_list, s=0.01, color='green')
plt.show()