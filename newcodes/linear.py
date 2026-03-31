import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("house.csv")

X = df[["area"]]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,random_state=1)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Metrics
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)

# Graph
plt.scatter(X, y)
plt.plot(X, model.predict(X), color='red')
plt.title("Linear Regression")
plt.show()