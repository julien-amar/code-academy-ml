import numpy as np

# Create an array
cupcakes = np.array([2, 0.75, 3, 1, 0.5])

# Generate an array from parsed data
recipes = np.genfromtxt('recipes.csv', delimiter=',')

print recipes

# Extract second column information for each rows.
eggs = recipes[:, 2]

print eggs
print eggs == 1

# Extract second row from dataset
cookies = recipes[2]

print cookies

# Create a new array, containing cupcakes values * 2 
double_batch = cupcakes * 2

print double_batch

# Create a new array, containing the sum of both array's values.
grocery_list = double_batch + cookies

print grocery_list