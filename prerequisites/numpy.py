import numpy as np

# Generate an array from parsed data
temperatures = np.genfromtxt('temperature_data.csv', delimiter=',')

# Create a new array, adding an offset (+ 3) to all temperature values 
temperatures_fixed = temperatures + 3.0

# Extract first row in dataset
monday_temperatures = temperatures_fixed[0]

# Extract 3rd & 4th rows of dataset, selecting only the first columns. 
thursday_friday_morning = temperatures_fixed[3:5, 1]

# Extract all values in dataset that are out of bound.
temperature_extremes = temperatures_fixed[(temperatures_fixed < 50) | (temperatures_fixed > 60)]

print temperature_extremes