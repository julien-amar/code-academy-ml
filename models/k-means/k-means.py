import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets
from copy import deepcopy

iris = datasets.load_iris()

# Labels (0: Iris setosa, 1: Iris versicolor, 2: Iris virginica)
print(iris.target)

# Description
print(iris.DESCR)

# Store iris.datas
samples = iris.data

# Create x and y
x = samples[:, 0]
y = samples[:, 1]

sepal_length_width = np.array(list(zip(x, y)))

####################################
# Step 1: Place K random centroids #
####################################

# Number of clusters
k = 3

# Create x coordinates of k random centroids
centroids_x = np.random.uniform(min(x), max(x), size=k)

# Create y coordinates of k random centroids
centroids_y = np.random.uniform(min(y), max(y), size=k)

centroids = np.array(list(zip(centroids_x, centroids_y)))

##############################################
# Step 2: Assign samples to nearest centroid #
##############################################

# Distance formula
def distance(a, b):
  return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** .5

# To store the value of centroids when it updates
centroids_old = np.zeros(centroids.shape)

# Cluster labels for each point (either 0, 1, or 2)
labels = np.zeros(len(samples))

# Distances to each centroid
distances = np.zeros(k)

# Initialize error:
error = np.zeros(k)

error[0] = distance(centroids[0], centroids_old[0])
error[1] = distance(centroids[1], centroids_old[1])
error[2] = distance(centroids[2], centroids_old[2])

while error.all() != 0:

    for i in range(len(samples)):
        distances[0] = distance(sepal_length_width[i], centroids[0])
        distances[1] = distance(sepal_length_width[i], centroids[1])
        distances[2] = distance(sepal_length_width[i], centroids[2])

        # Assign to the closest centroid
        cluster = np.argmin(distances)

        labels[i] = cluster

    # Print labels
    print (labels)

    ############################
    # Step 3: Update centroids #
    ############################

    centroids_old = deepcopy(centroids)

    for i in range(k):
        points = []
        for j in range(len(sepal_length_width)):
            if labels[j] == i:
                points.append(sepal_length_width[j])
        centroids[i] = np.mean(points, axis=0)

    error[0] = distance(centroids[0], centroids_old[0])
    error[1] = distance(centroids[1], centroids_old[1])
    error[2] = distance(centroids[2], centroids_old[2])

    print(centroids)
    print(centroids_old)

# Make a scatter plot of the centroids
colors = ['r', 'g', 'b']

for i in range(k):
  points = np.array([sepal_length_width[j] for j in range(len(samples)) if labels[j] == i])
  plt.scatter(points[:, 0], points[:, 1], c=colors[i], alpha=0.5)
  
plt.scatter(centroids[:, 0], centroids[:, 1], marker='D', s=150)

plt.xlabel('sepal length (cm)')
plt.ylabel('petal length (cm)')

# Display plot
plt.show()