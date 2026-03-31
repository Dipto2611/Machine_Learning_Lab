import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv("play.csv")

X = df.drop("play", axis=1)
y = df["play"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,random_state=1)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

print("Prediction:", model.predict(pd.DataFrame([[1,29,70,0]], columns=X.columns)))