import sklearn
from sklearn.model_selection import train_test_split
import pandas as pd

data = {
    'Temperature': [30, 25, 28, 22, 24, 26, 31, 29, 20, 18, 35, 15, 27, 33, 21, 19, 32, 23, 34, 17],
    'Humidity': [70, 80, 65, 90, 85, 60, 55, 75, 95, 88, 40, 92, 68, 50, 89, 93, 45, 77, 38, 97],
    'WindSpeed': [5, 3, 7, 2, 4, 6, 8, 10, 1, 3, 12, 2, 9, 15, 4, 3, 11, 5, 14, 2],
    'Pressure': [1012, 1015, 1010, 1020, 1018, 1011, 1009, 1013, 1022, 1017, 1005, 1024, 1012, 1007, 1019, 1021, 1006, 1016, 1003, 1025],
    'Weather': ['Cloudy', 'Stormy', 'Cloudy', 'Rainy', 'Stormy', 'Cloudy', 'Cloudy', 'Cloudy', 'Rainy', 'Rainy', 'Sunny', 'Rainy', 'Cloudy', 'Stormy', 'Rainy', 'Rainy', 'Stormy', 'Cloudy', 'Sunny', 'Rainy']
}

df = pd.DataFrame(data)

X = df[['Temperature', 'Humidity', 'WindSpeed', 'Pressure']]
y = df['Weather']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = sklearn.tree.DecisionTreeClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = sklearn.metrics.accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
precision = sklearn.metrics.precision_score(y_test, y_pred, average='micro')
print("Precision", precision)
recall = sklearn.metrics.recall_score(y_test, y_pred, average='micro')
print("Recall:", recall)
f1 = sklearn.metrics.f1_score(y_test, y_pred, average='micro')
print("F1:", f1)
confusion_matrix = sklearn.metrics.confusion_matrix(y_test, y_pred)
print("Confusion Matrix:", confusion_matrix)
