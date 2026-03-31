import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load CSV
df = pd.read_csv("house.csv")

X = df[["area"]]
y = df["price"]

# Model
model = LinearRegression()
model.fit(X, y)

# Prediction
pred = model.predict(X)

# Graph
plt.scatter(X, y)
plt.plot(X, pred, color='red')
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("House Price Prediction")
print("Predicted price for 900 (area):", model.predict([[900]]))
plt.show()

