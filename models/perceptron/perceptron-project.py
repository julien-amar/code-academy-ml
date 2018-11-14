import codecademylib3_seaborn
from sklearn.linear_model import Perceptron
import matplotlib.pyplot as plt
import numpy as np
from itertools import product

data = [(0, 0), (0, 1), (1, 0), (1, 1)]
# AND
labels = [0, 0, 0, 1]
# OR
# labels = [0, 1, 1, 1]
# XOR
# labels = [0, 1, 1, 0]

x = [point[0] for point in data]
y = [point[1] for point in data]

classifier = Perceptron(max_iter = 40)
classifier.fit(data, labels)

print(classifier.score(data, labels))

x_values = np.linspace(0, 1, 100)
y_values = np.linspace(0, 1, 100)
point_grid = list(product(x_values, y_values))

distances = classifier.decision_function(point_grid)
abs_distances = [abs(distance) for distance in distances]

distances_matrix = np.reshape(abs_distances, (100, 100))

heatmap = plt.pcolormesh(x_values, y_values, distances_matrix)
plt.colorbar(heatmap)
plt.show()
