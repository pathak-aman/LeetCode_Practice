from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets

app = FastAPI()

# Load and train the model
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
    
# Generate dataset
X,y = datasets.make_classification(n_samples = 100, n_features=2, n_classes=2, n_informative=2, n_redundant=0, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_test[0], y_test[0])

clf = LogisticRegression(lr=0.0001, iters=1000)

# Train
clf.fit(X_train, y_train)

# Define request body schema
class InputFeatures(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(features: InputFeatures):
    X_input = np.array(features.features).reshape(1, -1)
    prediction = clf.predict(X_input)
    return {"prediction": int(prediction[0])}

@app.get("/")
def root():
    return {"message": "FastAPI Logistic Regression is running!"}
