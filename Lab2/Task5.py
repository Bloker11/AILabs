
# ----------- imports -----------

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report


# ---------------------------- Decision Tree -----------------------------------------

df = pd.read_csv('diabetes.csv')
print(df)

all_inputs = df[["pregnant-times", "glucose-concentr", "blood-pressure", "skin-thickness", "insulin", "mass-index", "pedigree-func", "age"]].values
all_classes = df["class"].values

(train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=51139)
scaler = StandardScaler()
scaler.fit(train_inputs)

train_inputs = scaler.transform(train_inputs)
test_inputs = scaler.transform(test_inputs)

clf = tree.DecisionTreeClassifier()

clf.fit(train_inputs, train_classes)
print(clf.score(test_inputs, test_classes)*100)

tree.plot_tree(clf)
plt.show()


# ---------------------------- KNN -----------------------------------------


print()

array = [1, 3, 5, 11]

for k in array:
    print("k=", k)
    classifier = KNeighborsClassifier(n_neighbors=k).fit(train_inputs, train_classes)

    y_pred = classifier.predict(test_inputs)

    print(classification_report(test_classes, y_pred))