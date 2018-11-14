# Metrics

## How to split training & validation datasets ?

In general, putting 80% of your data in the training set, and 20% of your data in the validation set is a good place to start.

## How to evaluate validation metrics ?

Validation error might not be the only metric we’re interested in. A better way of judging the effectiveness of a machine learning algorithm is to compute its **precision**, **recall**, and **F1 score**.

## What is accuracy ?

Accuracy is calculated by finding the total number of correctly classified points and dividing by the total number of points.

Accuracy measures how many classifications your algorithm got correct out of every classification it made.

## What is recall ?

Recall measures the percentage of relevant items that your classifier found.

Our algorithm that always predicts False (on pretty rare occurences) might have a very high accuracy, but it never will find any True Positives, so its recall is 0.
This makes sense; recall should be very low for such an absurd classifier.

Recall measures the percentage of the relevant items your classifier was able to successfully find.

## What is precision ?

Unfortunately, recall isn’t a perfect statistic either. For example, we could create a snow day classifier that always returns True. This would have low accuracy, but its recall would be 1 because it would be able to accurately find every snow day. But this classifier is just as nonsensical as the one before! The statistic that will help demonstrate that this algorithm is flawed is precision.

Precision and recall are statistics that are on opposite ends of a scale. If one goes down, the other will go up.

Precision measures how the percentage of items that your classifier found that were actually relevent.

## What is F1 score ?

F1 score is the harmonic mean of precision and recall.

The F1 score combines both precision and recall into a single statistic. We use the harmonic mean rather than the traditional arithmetic mean because we want the F1 score to have a low value when either precision or recall is 0.

F1 score will be low if either precision or recall is low.

## How to validate small dataset ?

Using N-Fold Cross-Validation. Sometimes your dataset is so small, that splitting it 80/20 will still result in a large amount of variance. One solution to this is to perform N-Fold Cross-Validation. The central idea here is that we’re going to do this entire process N times and average the accuracy.

# Overfitting

Overfitting occurs when we have fit our model's parameters too closely to the training data. (regression score, too close to 1.0)

When we overfit, we are assuming that everything we see in the training data is exactly how it will appear in the real world. Instead, we want to be modeling trends that show us the general behavior of a variable

Machine Learning algorithms always must introduce a bias as a function of being programs that are trying to make assumptions and rules by looking at data.

# Code sample (from scratch)

```python
labels = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
guesses = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]

true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0

for i in range(len(guesses)):
  #True Positives
  if labels[i] == 1 and guesses[i] == 1:
    true_positives += 1
  #True Negatives
  if labels[i] == 0 and guesses[i] == 0:
    true_negatives += 1
  #False Positives
  if labels[i] == 0 and guesses[i] == 1:
    false_positives += 1
  #False Negatives
  if labels[i] == 1 and guesses[i] == 0:
    false_negatives += 1
    
accuracy = (true_positives + true_negatives) / len(guesses)
recall = true_positives / (true_positives + false_negatives)
precision = true_positives / (true_positives + false_positives)
f_1 = 2 * ((precision * recall) / (precision + recall))

print('Accuracy:', accuracy) # 0.3
print('Recall:', recall) # 0.42857142857142855
print('Precision:', precision) # 0.5
print('F1-Score:', f_1) # 0.4615384615384615
```

# Code sample (with scikit-learn)

```python
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

labels = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
guesses = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]

accuracy = accuracy_score(labels, guesses)
recall = recall_score(labels, guesses)
precision = precision_score(labels, guesses)
f1 = f1_score(labels, guesses)

print('Accuracy:', accuracy) # 0.3
print('Recall:', recall) # 0.428571428571
print('Precision:', precision) # 0.5
print('F1-Score:', f1) # 0.461538461538
```
