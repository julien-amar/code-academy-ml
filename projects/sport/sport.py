import codecademylib3_seaborn
import matplotlib.pyplot as plt

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from svm_visualization import draw_boundary
from players import aaron_judge, jose_altuve, david_ortiz

# Graph strike zone for a specific baseball player
def graph_player(index, player_name, player):
  fig, ax = plt.subplots()
  
  plt.title(player_name)

  # Standardize type column (using Strike & Ball)
  player['type'] = player['type'].map({'S':1, 'B':0})
  player = player.dropna(subset=['plate_x', 'plate_z', 'type'])

  # Split data set
  training_set, validation_set = train_test_split(player, random_state=1)

  # Create SVM classifier (RFB kernel)
  classifier = SVC(kernel='rbf', gamma=3, C=1)

  # Train model using learn data set
  classifier.fit(training_set[['plate_x', 'plate_z']], training_set['type'])

  # Get Score using validation data set
  score = classifier.score(validation_set[['plate_x', 'plate_z']], validation_set['type'])

  print ('Score:', score)

  # Graph plate_x vs plate_z (Strike are in red, Ball in blue)
  ax.set_ylim(-2, 6)
  ax.set_xlim(-3, 3)
  plt.scatter(player.plate_x, player.plate_z, c=player.type, cmap=plt.cm.coolwarm, alpha=0.5)

  # Draw SVM boundries
  draw_boundary (ax, classifier)

  plt.show()

# Graph several players
graph_player(0, 'Aaron Judge', aaron_judge)
graph_player(1, 'Jose Altuve', jose_altuve)
graph_player(2, 'David Ortiz', david_ortiz)

