from reviews import neg_counter, pos_counter

review = "This cribb was amazing"

# % of positive and negative reviews
percent_pos = 0.5
percent_neg = 0.5

# Number of positive/negative words
total_pos = sum(pos_counter.values())
total_neg = sum(neg_counter.values())

# Split the words
review_words = review.split()

# Calculate the global probability that the sentence is positive or negative
pos_probability = 1
neg_probability = 1

for word in review_words:
  word_in_pos = pos_counter[word]
  word_in_neg = neg_counter[word]
  
  pos_probability *= (word_in_pos + 1) / (total_pos + len(pos_counter))
  neg_probability *= (word_in_neg + 1) / (total_neg + len(neg_counter))

final_pos = pos_probability * percent_pos
final_neg = neg_probability * percent_neg

print ('Positive probability:', final_pos)
print ('Negative probability:', final_neg)

if final_pos < final_neg:
  print('The review is negative')
else:
  print('The review is positive')
