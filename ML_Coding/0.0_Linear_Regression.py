'''
Mean Squared Error (MSE) Loss:
Loss = (y - y_pred)^2 -> Taking the mean over all samples

Prediction:
y_pred = wX + b

Gradient of Loss w.r.t. Weight (w):
dL/dw = 2 * (y - y_pred) * (-Xi)  
      = 2 * (y_pred - y) * Xi  # Rewriting for consistency

Gradient of Loss w.r.t. Bias (b):
dL/db = 2 * (y - y_pred) * (-1)  
      = 2 * (y_pred - y)

Gradient Descent Updates:
W = W - alpha * dL/dw
  = W - alpha * (2 * (y_pred - y) * Xi)

Since alpha (learning rate) already scales the step, we can absorb the factor of 2:
W = W - alpha * (y_pred - y) * Xi
'''



import numpy as np

class LinearRegression:
    def __init__(self, lr = 0.001, iters = 1000):
        self.lr = lr
        self.iters = iters
        self.weight = None
        self.bias = None


    def fit(self, X, y):
        n_samples, n_features = X.shape

        self.weight = np.random.randn(n_features)  * 0.01
        self.bias = 0

        for i in range(self.iters):
            y_pred = self.predict(X)
            loss = self.get_loss(y,y_pred)

            dw = (1/n_samples) * np.dot(X.T,(y_pred-y))
            db = 1/n_samples * np.sum(y_pred-y)

            self.weight -= self.lr * dw
            self.bias -= self.lr * db

            print(f"iter: {i}, loss: {loss}")


    def predict(self, X):
        y_pred = np.dot(X, self.weight,) + self.bias
        return y_pred

    def get_loss(self,y, y_pred):
        loss = np.mean(np.square(y - y_pred))
        return loss


# Test the code:
def mean_squared_error(y_true,y_pred):
    return np.mean(np.square(y_true - y_pred))

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import datasets

X,y = datasets.make_regression(n_samples=100, n_features=1, random_state=42, noise=20)
X_train, X_test, y_train, y_test = train_test_split(X,y, shuffle= True, test_size=0.15, random_state = 42)

reg = LinearRegression()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print("MSE:", mse)

y_pred_line = reg.predict(X)
cmap = plt.get_cmap("viridis")
fig = plt.figure(figsize=(8, 6))
m1 = plt.scatter(X_train, y_train, color=cmap(0.9), s=10)
m2 = plt.scatter(X_test, y_test, color=cmap(0.5), s=10)
plt.plot(X, y_pred_line, color="black", linewidth=2, label="Prediction")
plt.show()