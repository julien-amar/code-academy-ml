from movies import movie_dataset, movie_labels, training_set, training_labels, validation_set, validation_labels

release_dates = [1897, 1998, 2000, 1948, 1962, 1950, 1975, 1960, 2017, 1937, 1968, 1996, 1944, 1891, 1995, 1948, 2011, 1965, 1891, 1978]

# Normalization is important as it equalize features proportions
def min_max_normalize (lst):
  minimum = min(lst)
  maximum = max(lst)
  normalized = []
  for value in lst:
    normalized.append((value - minimum) / (maximum - minimum))
  return normalized

print(min_max_normalize(release_dates))

# Euclydian distance
def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance

# Get "K" closest titles(from "unknown") in "dataset"
def classify(unknown, dataset, k):
  # find closest titles based on distance
  distances = []
  for title in dataset:
    distance_to_point = distance(unknown, dataset[title])
    distances.append([distance_to_point, title])
  distances.sort()
  # Get "k" neighbors
  neighbors = distances[0:k]
  # Count positive & negative over neighbors
  num_good = 0
  num_bad = 0
  for neighbor in neighbors:
    title = neighbor[1]
    if labels[title] == 0:
      num_bad += 1
    elif labels[title] == 1:
      num_good += 1
  # Return positive is most neightbors are positive, if not return negative
  if num_good > num_bad:
    return 1
  else:
    return 0

print("Call Me By Your Name" in movie_dataset) # False

# Normalize dataset
my_movie = [350000, 132, 2017]
normalized_my_movie = min_max_normalize(my_movie)

# Classify "Bee Movie" according to training data set
guess = classify(validation_set["Bee Movie"], training_set, training_labels, 5)
print(guess) # 0

if validation_labels["Bee Movie"] == guess:
  print ('Good movie!')
else:
    print ('Bad movie!')

# Evaluate accuracy 
def find_validation_accuracy(training_set, training_labels, validation_set, validation_labels, k):
  num_correct = 0.0
  for title in validation_set:
    guess = classify(validation_set[title], training_set, training_labels, k)
    if validation_labels[title] == guess:
      num_correct += 1
  return num_correct / len(validation_set)

print (find_validation_accuracy (training_set, training_labels, validation_set, validation_labels, 3)) # 0.6639344262295082

