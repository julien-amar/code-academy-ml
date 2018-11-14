###############
# Naive bayes #
###############

import numpy as np

from sklearn.naive_bayes import MultinomialNB

x = np.random.randint(5, size=(6, 100))
y = np.array([1, 2, 3, 4, 5, 6])

# Create multinomial object
clf = MultinomialNB()

# Train the model using the training sets
clf.fit(x, y)

# Make predictions using the testing set
print(clf.predict(X[2:3])) # 3
