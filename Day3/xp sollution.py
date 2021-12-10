
## XP Excercise class sollution

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

class KNN:
    def __init__(self, k):
        self.k = k
        self.x_train = None
        self.y_train = None
    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train
    def __distance__(self, point1, point2):
        dist = np.linalg.norm(point1 - point2)
        return dist
    def predict(self, X_test):
        predictions = []
        for x in X_test:
            dst = [self.__distance__(x, x_t) for x_t in self.x_train]
            sorted_dst = np.argsort(dst)
            labels = sorted_dst[:self.k]
            predictions.append(self.y_train.iloc[labels].mode()[0])
        return predictions
data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
y = data['species']
X = data.drop(columns = ['species']).values
X_train, X_test, y_train, y_test = train_test_split(X,y)
knn = KNN(3)
knn.fit(X_train, y_train)
predictions = knn.predict(X_test)
error = ((len(y_test) - sum(y_test == predictions)) / len(y_test)) * 100
print(f"error for {len(y_test)} instances on the the x_test = {error} %")