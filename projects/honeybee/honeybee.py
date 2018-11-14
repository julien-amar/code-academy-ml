import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn import linear_model

# Extract data from data set
df = pd.read_csv("https://s3.amazonaws.com/codecademy-content/programs/data-science-path/linear_regression/honeyproduction.csv")

# Print top lines
print(df.head())

# Get production per year
prod_per_year = df.groupby('year')['totalprod'].mean().reset_index()

print (prod_per_year)

# Plot production per year
X = prod_per_year.year.values.reshape(-1, 1)
y = prod_per_year.totalprod.values.reshape(-1, 1)

plt.scatter(X, y, alpha=0.4)

# Train using production per year
regr = linear_model.LinearRegression()
model = regr.fit(X, y)

print(model.coef_)
print(model.intercept_)

# Plot linear regression
y_predict = regr.predict(X)

plt.plot(X, y_predict)

# Plot predicted value for the next years (up to 2050).
X_future = np.array(range(2013, 2050))
X_future = X_future.reshape(-1, 1)

future_predict = regr.predict(X_future)

plt.plot(X_future, future_predict)

plt.show()
