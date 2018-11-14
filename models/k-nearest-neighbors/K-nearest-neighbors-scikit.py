##############
# KNN sample #
##############

import numpy as np

from sklearn.neighbors import KNeighborsClassifier

X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]

# Create k-nearest neighbors object
neigh = KNeighborsClassifier(n_neighbors=3)

# Train the model using the training sets
neigh.fit(X, y) 

# Make predictions using the testing set
print(neigh.predict([[1.1]])) # 0
print(neigh.predict_proba([[0.9]])) # [[ 0.66666667  0.33333333]]