'''
Binary Cross Entropy / Log Loss:
L = - [y * (1 - log(y_pred)) + (1-y) * (log(1-y_pred))]

Equation of logistic regression:
z = Wx + b
y_pred = 1 / (1 + e^(-z))


dl/dw = (y_pred - y) X
dl/db = y_pred - y


'''

import numpy as np

class LogisticRegression:
    
    def __init__(self, lr = 0.001, iters = 1000):
        self.iters = iters
        self.lr = lr
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape

        self.weights = np.random.randn(n_features) * 0.01
        self.bias = 0

        for i in range(self.iters):
            y_pred = self.predict_proba(X)
            loss = self.get_loss(y, y_pred)

            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (1 / n_samples) * np.sum(y_pred - y)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

            if i % 100 == 0:  # Print every 100 iterations to avoid excessive output
                print(f"iter: {i}, loss: {loss}")
    
    def activation_sigmoid(self,z):
        return 1 / (1 + np.exp(-z))

    def predict_proba(self, X):
        y_pred = np.dot(self.weights, X.T) + self.bias
        y_pred_sigmoid = self.activation_sigmoid(y_pred)
        return y_pred_sigmoid


    
    def get_loss(self, y, y_pred):
        loss = -np.mean(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred))
        return loss


    def predict(self, X):
        """ Converts probability scores to binary labels. """
        y_pred_sigmoid = self.predict_proba(X)
        return np.array([1 if i > 0.5 else 0 for i in y_pred_sigmoid])


# Test the code:

if __name__ == "__main__":
    # Imports
    from sklearn.model_selection import train_test_split
    from sklearn import datasets

    def accuracy(y_true, y_pred):
        accuracy = np.sum(y_true == y_pred) / len(y_true)
        return accuracy

    X,y = datasets.make_classification(n_samples = 100, n_features=2, n_classes=2, n_informative=2, n_redundant=0, random_state=42)


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf = LogisticRegression(lr=0.0001, iters=1000)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)

    print("LR classification accuracy:", accuracy(y_test, predictions))