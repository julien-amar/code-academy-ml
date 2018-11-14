from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

# Define which categories we will compare
categories = ['comp.sys.ibm.pc.hardware','rec.sport.hockey']

# Extract our training & testing data set
train_emails = fetch_20newsgroups(categories=categories, subset='train', shuffle = True, random_state = 108)
test_emails = fetch_20newsgroups(categories=categories, subset='test', shuffle = True, random_state = 108)

# Print 6th mail content & associated category
print (train_emails.data[5])
print (train_emails.target_names[train_emails.target[5]])

# Training using all wording data set
counter = CountVectorizer()
counter.fit(test_emails.data + train_emails.data)

# Count word occurence for each training & testing data set
train_counts = counter.transform(train_emails.data)
test_counts = counter.transform(test_emails.data)

# Create classifier
classifier = MultinomialNB()

# Learn
classifier.fit(train_counts, train_emails.target)

# Evalutate score based on testing data set
score = classifier.score(test_counts, test_emails.target)

print (score) # 0.997471554994
