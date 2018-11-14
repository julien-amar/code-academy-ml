import codecademylib3_seaborn

import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier 

breast_cancer_data  = load_breast_cancer()

# Get Feature names
print (breast_cancer_data.feature_names)
# Get First row of input dataset
print (breast_cancer_data.data[0])

# Get labels
print (breast_cancer_data.target_names)
# Get label for first row of input dataset
print (breast_cancer_data.target)

# Extract learning and validation dataset
training_data, validation_data, training_labels, validation_labels = train_test_split(breast_cancer_data.data, breast_cancer_data.target, test_size = 0.2, random_state = 100)

k_list = range(1, 101)
accuracies = []
for k in k_list:
    # Create a K-Neighbor Classifier
    classifier = KNeighborsClassifier (n_neighbors = k)

    # Train using training dataset
    classifier.fit(training_data, training_labels)

    # Get score using validation dataset
    accuracies.append(classifier.score(validation_data, validation_labels))

# Plot "k" vs "accuracy"
plt.plot(k_list, accuracies)
plt.xlabel('k')
plt.ylabel('Validation Accuracy')
plt.title('Breast Cancer Classifier Accuracy')
plt.show()
