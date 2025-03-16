'''
KNN: Simple, lazy Loading algo. No training, Only predict

Notion: Datapoints that are closer to each other, don't differ much in terms of the 
class labels (classification) or or values (Regression)
Distance: Euclidean
Pros: Simple, Intuitive.
Cons: Memory and computation heavy, as for each new point, distance from all the distance has to be calculated.

'''

import numpy as np
from collections import Counter

def euclidean(p,q):
    ''' 
    Finds Eulicidean distance between p,q
    '''
    return np.sum(np.square(p-q))


class KNN:
    def __init__(self, k = 5):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
    
    def predict_single(self, X):
        distances = []
        for x_train in self.X_train:
            distances.append(euclidean(X, x_train))
        distances = np.array(distances)
        k_indices = np.argsort(distances)[:self.k]

        k_class_lables = self.y_train[k_indices]

        most_common = Counter(k_class_lables).most_common()
        return most_common[0][0]


    def predict(self, X):
        return [self.predict_single(x) for x in X]
    

# Test the code:

if __name__ == "__main__":
    # Imports
    from sklearn.model_selection import train_test_split
    from sklearn import datasets

    def accuracy(y_true, y_pred):
        accuracy = np.sum(y_true == y_pred) / len(y_true)
        return accuracy

    X,y = datasets.make_classification(n_samples = 1000, n_features=5, n_classes=3, n_informative=4, 
                                       n_redundant=0, random_state=42)


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


    # print(euclidean(X_test[0],X_train[1]))

    clf = KNN(k = 3)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)

    print("KNN classification accuracy:", accuracy(y_test, predictions))