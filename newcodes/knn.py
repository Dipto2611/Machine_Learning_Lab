import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("knn.csv") #iris dataset

# Convert categorical → numeric (SAFE METHOD)
le = LabelEncoder()
df["species"] = le.fit_transform(df["species"])

# Features and target
X = df[["sepal_length","sepal_width","petal_length","petal_width"]] #input features
y = df["species"] #output labels

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1 )

# Create and train model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# New prediction (NO WARNING)
new_data = pd.DataFrame([[5.0,3.4,1.5,0.2]], columns=X.columns)
pred = model.predict(new_data)

# Convert back to label
print("Prediction:", le.inverse_transform(pred)[0])