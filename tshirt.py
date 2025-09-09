import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier


df = pd.read_csv('tshirt.csv')


X = df.iloc[:, :-1]   
y = df.iloc[:, -1]   


print("Features (X):")
print(X)
print("\nLabels (y):")
print(y)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)


y_pred = knn.predict(X_test)
print("\nAccuracy:", metrics.accuracy_score(y_test, y_pred))


h = int(input('\nEnter height (cm): '))
w = int(input('Enter weight (kg): '))


sample = pd.DataFrame({'Height': [h], 'Weight': [w]})
predicted_size = knn.predict(sample)
print("Predicted T-shirt size:", predicted_size[0])

