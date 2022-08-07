import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

#showing the points created by the RandomWalk class
plt.style.use('classic')
fig, ax = plt.subplots()
point_numbers = range(rw.num_points)
#ax.scatter(rw.x_values, rw.y_values, s=10, c=point_numbers, edgecolor='none')
ax.plot(rw.x_values, rw.y_values, linewidth = 1)
ax.scatter(0, 0, c='white', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='white', s=100)

ax.get_yaxis().set_visible(False)
ax.get_xaxis().set_visible(False)

plt.show()
