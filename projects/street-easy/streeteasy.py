from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression

import codecademylib3_seaborn
import matplotlib.pyplot as plt
import pandas as pd

# Extract data from CSV file
streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv")

# Create a data frame from data
df = pd.DataFrame(streeteasy)

# Extract useful features
features = ['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway', 'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher', 'has_patio', 'has_gym']
x = df[features]
y = df[['rent']]

# Split 80% (training) / 20% (validation)
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=6)

# Create multiple linear regression model
mlr = LinearRegression()

# Training
model = mlr.fit(x_train, y_train)

print(model.coef_)

# Predict using validation data set
y_predict = mlr.predict(x_test)

# Graph "Predicted price" vs "Actual price"
plt.scatter(y_test, y_predict, alpha=0.4)
plt.xlabel("Prices: $Y_i$")
plt.ylabel("Predicted prices: $\hat{Y}_i$")
plt.title("Actual Rent vs Predicted Rent")
plt.show()

# Process a Residual Analysis. R² is the percentage variation in "y" explained by all the "x" variables together.
# The goal is reaching a threshold of > 70% 
print("Train score:")
print(mlr.score(x_train, y_train))

print("Test score:")
print(mlr.score(x_test, y_test))