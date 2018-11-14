import codecademylib3_seaborn
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

points, labels = make_circles(n_samples=300, factor=.2, noise=.05, random_state = 1)

training_data, validation_data, training_labels, validation_labels = train_test_split(points, labels, train_size = 0.8, test_size = 0.2, random_state = 100)

# SVM using polynomial kernel
classifier = SVC(kernel='poly', degree=2)

classifier.fit(training_data, training_labels)

print(classifier.score(validation_data, validation_labels)) # 1.0

# Equivalent using linear kernel
classifier = SVC(kernel = "linear", random_state = 1)

classifier.fit(training_data, training_labels)

print(classifier.score(validation_data, validation_labels)) # 0.56
