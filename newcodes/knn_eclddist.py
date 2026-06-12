from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import math

iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=1)

def euclidean_distance(a,b):

    sum = 0

    for i in range(len(a)):
        sum = sum + (a[i] - b[i])**2

    return math.sqrt(sum)

print("Euclidean Distance = ",euclidean_distance(X_train[0],X_train[1]))

for k in [1,3,5,7]:

    model = KNeighborsClassifier(n_neighbors=k)

    model.fit(X_train,y_train)

    y_pred = model.predict(X_test)

    print("K =",k)

    print("Accuracy =",accuracy_score(y_test,y_pred))