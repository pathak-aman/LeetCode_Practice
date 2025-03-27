"""

Forward pass:
y_pred = np.dot(X, weights) + bias

Loss:
l = np.mean(np.square(y_true - y_pred))

Gradient Descent:
dw = np.mean(np.dot(X, (y_pred - y)))
db = np.mean(np.sum(y_pred - y))

Weight updates:
w = w - lr * dw
b = b - lr * db


"""

import numpy as np

class MiniBatchGD_Linear_Regression:
    def __init__(self, lr = 0.001, max_iters = 1000, batch_size = 32):
        self.lr = lr
        self.max_iters = max_iters
        self.weights = None
        self.bias = None
        self.batch_size = batch_size

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.random.randn(n_features) * 0.01
        self.bias = 0

        for _ in range(self.max_iters):
            loss = []

            for idx in range(0, n_samples, self.batch_size):
                x_batch = X[idx: idx+self.batch_size]
                y_batch = y[idx: idx+self.batch_size]

                y_pred = self.predict(x_batch)

                loss_batch = self.get_loss(y_batch, y_pred)
                loss.append(loss_batch)

                dw = (1/self.batch_size) * np.dot(x_batch.T, (y_pred - y_batch))
                db = (1/self.batch_size) * np.sum(y_pred - y_batch)

                self.weights -= self.lr * dw
                self.bias -= self.lr * db

            
            if _ % 100 == 0:
                loss = np.array(loss)
                print(f"Loss : {np.mean(loss)}, iteration: {_}")

    def predict(self, X):
        y_pred = np.dot(X, self.weights) + self.bias
        return y_pred

    def get_loss(self, y_true, y_pred):
        loss = np.mean(np.square(y_true - y_pred))
        return loss


# Test the code:
def mean_squared_error(y_true,y_pred):
    return np.mean(np.square(y_true - y_pred))

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import datasets

X,y = datasets.make_regression(n_samples=1000, n_features=10, n_informative=4, noise=5)
X_train, X_test, y_train, y_test = train_test_split(X,y, shuffle= True, test_size=0.15, random_state = 42)

reg = MiniBatchGD_Linear_Regression(batch_size=32)
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print("MSE:", mse)