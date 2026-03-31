import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# Load data
df = pd.read_csv("stud.csv")

# Convert labels
le = LabelEncoder()
df["result"] = le.fit_transform(df["result"])

# Features & target
X = df[["hours","marks"]] #input for 2 features
y = df["result"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=1)

# Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Metrics
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# New input
new_data = pd.DataFrame([[4,50]], columns=X.columns)
pred = model.predict(new_data)

# Convert back to label
print("Prediction:", le.inverse_transform(pred)[0]) #takes the first prediction of the array and converts it back to label