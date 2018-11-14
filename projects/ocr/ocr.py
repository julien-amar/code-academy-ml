import codecademylib3_seaborn
import numpy as np

from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

# Get Optical Recognition of Handwritten Digits Data Set
digits = datasets.load_digits()

# Get data set description
print (digits.DESCR)

# Get data set pixels
print (digits.data)

# Get data set labels
print (digits.target)

# Define 10 clusters (as we have 10 digits (0 to 9))
model = KMeans(n_clusters=10, random_state=42)

# Cluster the data
model.fit(digits.data)

# Figure size (width, height)
fig = plt.figure(figsize=(8, 3))
fig.suptitle('Cluser Center Images', fontsize=14, fontweight='bold')
for i in range(10):
  # Initialize subplots in a grid of 2X5, at i+1th position
  ax = fig.add_subplot(2, 5, 1 + i)
  # Display images
  ax.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)
plt.show()

# Adjust the subplots 
fig = plt.figure(figsize=(6, 6))
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

# For each of the 64 images
for i in range(64):
    # Initialize the subplots: add a subplot in the grid of 8 by 8, at the i+1-th position
    ax = fig.add_subplot(8, 8, i+1, xticks=[], yticks=[])

    # Display an image at the i-th position
    ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')

    # Label the image with the target value
    ax.text(0, 7, str(digits.target[i]))

plt.show()

# Try text recognition by drawing digits
new_samples = np.array([
[0.08,2.27,4.19,6.17,5.03,0.15,0.00,0.00,4.17,7.62,7.39,6.47,7.62,7.00,1.83,0.00,6.69,5.55,0.30,0.08,2.57,7.30,4.26,0.00,6.85,4.49,0.00,0.00,0.00,7.23,4.18,0.00,5.49,6.86,0.30,0.00,0.91,7.62,2.82,0.00,2.21,7.61,2.58,0.00,3.57,7.62,1.67,0.00,0.31,7.09,7.62,7.07,7.62,5.93,0.07,0.00,0.00,1.05,3.50,3.81,2.96,0.15,0.00,0.00],
[0.00,0.23,3.87,6.09,4.95,0.46,0.00,0.00,0.00,3.58,7.62,6.00,7.62,3.88,0.00,0.00,0.00,0.68,1.82,0.00,5.93,5.32,0.00,0.00,0.00,0.00,0.00,1.52,7.15,5.25,0.00,0.00,0.00,0.00,0.38,6.78,6.93,1.82,0.00,0.00,0.00,0.00,4.77,7.60,3.57,0.45,0.00,0.00,0.00,0.00,7.46,7.62,7.61,7.62,1.83,0.00,0.00,0.00,1.13,1.52,2.27,3.04,0.46,0.00],
[0.00,0.83,6.46,6.85,6.86,7.39,3.36,0.00,0.00,1.45,7.62,5.02,3.81,3.80,1.06,0.00,0.00,0.46,7.61,5.33,3.81,3.81,2.59,0.23,0.00,0.00,7.16,7.62,6.86,7.17,7.62,6.55,0.00,0.00,0.00,0.00,0.00,0.23,4.63,7.61,0.00,0.00,1.14,1.67,4.02,6.92,7.62,7.61,0.00,0.00,7.47,7.62,7.62,5.62,2.72,0.37,0.00,0.00,1.14,1.52,0.90,0.00,0.00,0.00],
[0.00,0.91,4.57,4.57,4.48,1.52,0.00,0.00,0.00,1.37,6.09,6.09,7.30,5.09,0.00,0.00,0.00,0.00,0.00,0.60,6.84,5.25,0.00,0.00,0.00,0.00,0.00,7.15,7.62,6.77,2.97,0.00,0.00,0.00,0.00,2.58,3.42,6.46,6.85,0.00,0.00,0.07,2.89,4.26,4.57,6.69,6.77,0.00,0.00,0.54,7.39,7.31,6.24,5.86,2.04,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00]
])

new_labels = model.predict(new_samples)

print (new_labels)

for i in range(len(new_labels)):
  if new_labels[i] == 0:
    print(0, end='')
  elif new_labels[i] == 1:
    print(9, end='')
  elif new_labels[i] == 2:
    print(2, end='')
  elif new_labels[i] == 3:
    print(1, end='')
  elif new_labels[i] == 4:
    print(6, end='')
  elif new_labels[i] == 5:
    print(8, end='')
  elif new_labels[i] == 6:
    print(4, end='')
  elif new_labels[i] == 7:
    print(5, end='')
  elif new_labels[i] == 8:
    print(7, end='')
  elif new_labels[i] == 9:
    print(3, end='')
