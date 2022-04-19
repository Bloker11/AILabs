from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv("iris.csv")

all_inputs = df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values
all_classes = df['variety'].values

(train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7,
random_state=51139)

array = [1, 3, 5, 11]

for k in array:
    classifier = KNeighborsClassifier(n_neighbors=k)
    classifier.fit(train_inputs, train_classes)

    y_pred = classifier.predict(test_inputs)

    print("k=", k)
    print(classification_report(test_classes, y_pred))



