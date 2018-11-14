# Regression

Regression is used to predict outputs that are continuous. The outputs are quantities that can be flexibly determined based on the inputs of the model rather than being confined to a set of possible labels.

Linear regression is the most popular regression algorithm. It is often underrated because of its relative simplicity. In a business setting, it could be used to predict the likelihood that a customer will churn or the revenue a customer will generate. More complex models may fit this data better, at the cost of losing simplicity.

## Linear regression

This implementation is based on Gradient descent algorithm (used by scikit-learn for linear regression).
Its goal is to find best fit using linear regression (by finding slope & intercept).

## Scikit-learn

Scikit-learn is a library in Python that provides many unsupervised and supervised learning algorithms:

* Regression, including Linear and Logistic Regression

# Classification

Classification is used to predict a discrete label. The outputs fall under a finite set of possible outcomes. Many situations have only two possible outcomes. This is called **binary classification**.

Multi-label classification is when there are multiple possible outcomes. It is useful for customer segmentation, image categorization, and sentiment analysis for understanding text. To perform these classifications, we use models like **Naive Bayes**, **K-Nearest Neighbors**, and **SVMs**

## Scikit-learn

Scikit-learn is a library in Python that provides many unsupervised and supervised learning algorithms:

* Classification, including K-Nearest Neighbors
* Clustering, including K-Means and K-Means++
