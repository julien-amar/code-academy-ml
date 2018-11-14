from sklearn.svm import SVC
from graph import points, labels

# SVM using Linear kernel
classifier = SVC(kernel = 'linear')

classifier.fit(points, labels)

print(classifier.predict([[3, 4],[6, 7]]))
print(classifier.support_vectors_)
