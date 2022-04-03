import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("iris.csv")

(train_set, test_set) = train_test_split(df.values, train_size=0.7,
random_state=51139)

def classify_iris(sl, sw, pl, pw):
    if 4.5 <= sl <= 5.8 and 0.1 <= pw <= 0.6 and 1.9 >= pl >= 1.1 and 2.9 <= sw <= 3.9:
        return("Setosa")
    elif 4.8 <= pl <= 6.9 and 2.5 <= sw <= 4.8 and 5.9 <= sl <= 7.7 and 1.5 <= pw <= 2.5:
        return("Virgnica")
    else:
        return("Versicolor")

good_predictions = 0
leng = test_set.shape[0]

print(leng)

for i in range(leng):
    my_predicted_answer = classify_iris(test_set[i, 0], test_set[i, 1], test_set[i, 2], test_set[i, 3])
    real_answer = test_set[i, 4]
    if my_predicted_answer == real_answer:
        good_predictions = good_predictions + 1

print(good_predictions)
print(good_predictions/leng*100, "%")