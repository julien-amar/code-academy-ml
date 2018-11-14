import codecademylib

from matplotlib import pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y1 = [0, 1, 4, 9, 16, 25]
y2 = [0, 1, 8, 27, 64, 125]

# Plot y1 & y2 vs x axis
plt.plot(x, y1, color='pink', marker='o',label='square')
plt.plot(x, y2, color='gray', marker='o',label='cubic')

# Define titles for graph & axis
plt.title('Two Lines on One Graph')
plt.xlabel('Amazing X-axis')
plt.ylabel('Incredible Y-axis')

# Display legend (see: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html)
plt.legend(loc=4)

plt.show()