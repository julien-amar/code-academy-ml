from reviews import neg_list, pos_list
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

review = "This crib was amazing"

# Vectorize & count words gathering both positive & negative words
counter = CountVectorizer()
counter.fit(neg_list + pos_list)

print(counter.vocabulary_)

# Get occurence of words
training_counts = counter.transform(neg_list + pos_list)
review_counts = counter.transform([review])

print(review_counts)

# Prepare labels for classifications (100 * negative + 1000 * positive)
training_labels = [0] * 1000 + [1] * 1000

classifier = MultinomialNB()

# Train by associating words with labels
classifier.fit(training_counts, training_labels)

# Perdict is review is positive or negative (which label it correspond to) 
print(classifier.predict(review_counts))

# Show prediction score for all labels
print(classifier.predict_proba(review_counts))