from movies import movie_dataset, movie_ratings

# Euclydian distance
def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance

# Get "K" closest titles (from "unknown") in "dataset", then do a regression using "movie_ratings"
def predict(unknown, dataset, movie_ratings, k):
  # find closest titles based on distance
  distances = []

  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    distances.append([distance_to_point, title])

  distances.sort()

  # Get "k" neighbors
  neighbors = distances[0:k]

  # Estimate movie rating based doing a weighted regression
  numerator = 0
  denominator = 0

  for neighbor in neighbors:
    numerator += movie_ratings[neighbor[1]] / neighbor[0]
    denominator += 1 / neighbor[0]

  return numerator / denominator

print (predict([0.016, 0.300, 1.022], movie_dataset, movie_ratings, 5))