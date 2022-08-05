import matplotlib.pyplot as plt

x_values = range(1,10)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Blues)

#Defining the title and axis labels
ax.set_title("Squares", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squares", fontsize=14)

#Defining label size
ax.tick_params(axis='both', which='major', labelsize=14)

ax.axis([0, 1000, 0 , 1100000])

plt.show()