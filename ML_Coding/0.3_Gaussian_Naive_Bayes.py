"""
Naïve Bayes Classifier (Gaussian)

### Theory:
Naïve Bayes is a probabilistic classifier** based on Bayes' Theorem**, which states:

    P(y | X) = ( P(X | y) * P(y) ) / P(X)

Where:
- `P(y | X)`: Posterior probability of class `y` given features `X`
- `P(X | y)`: Likelihood of features `X` given class `y`
- `P(y)`: Prior probability of class `y`
- `P(X)`: Probability of features `X` (acts as a normalizing constant)

#### **Naïve Assumption:**
Naïve Bayes assumes that all features are **conditionally independent** given the class. 
This simplifies probability calculations significantly.

#### **Gaussian Naïve Bayes (GNB)**
For continuous data, we assume that each feature follows a **Gaussian (Normal) distribution**:

    P(x_i | y) = (1 / sqrt(2 * pi * var)) * exp( - (x_i - mean)^2 / (2 * var) )

where `mean` and `var` are computed from training data for each class.

#### **Final Classification Rule**
We compute the **log-posterior** for each class and choose the one with the highest probability:

    log P(y | X) = log P(y) + Σ log P(x_i | y)

Using logarithms prevents **underflow** when multiplying small probabilities.

### **Advantages:**
- **Fast & Efficient** (performs well even on small datasets)
- **Interpretable & Simple**
- **Works well for high-dimensional data**
- **Effective with limited training data**

### **Limitations:**
- **Strong Independence Assumption** (often unrealistic in real-world data)
- **Struggles with Correlated Features**
- **Zero Probability Issue** (fixed using Laplace smoothing)

### **Common Applications:**
- Spam Detection (Email Classification)
- Sentiment Analysis (Positive/Negative Reviews)
- Medical Diagnosis (Probability of Disease Given Symptoms)
- Text Classification (News Categorization, Topic Modeling)

"""


import numpy as np

class NB:
    def __init__(self):
        self.mean = None
        self.var = None
        self.prior = None
    
    def fit(self, X, y):
        self.n_samples, self.n_features = X.shape
        self.classes = np.unique(y)
        self.n_classes = len(self.classes)

        # Intialize
        self.mean = np.zeros((self.n_classes, self.n_features))
        self.var = np.zeros((self.n_classes, self.n_features))
        self.prior = np.zeros(self.n_classes)


        # Fill up mean, std, prior
        for idx, cls in enumerate(self.classes):
            X_class = X[y == cls]
            self.mean[idx, :] = np.mean(X_class, axis = 0)
            self.var[idx, :] = np.var(X_class, axis = 0)
            self.prior[idx] = X_class.shape[0] / self.n_samples
        
        # print(self.mean)

    def gaussian_pdf(self, mean, var, x):
        epsilon=1e-9
        var = var + epsilon  # Avoids division by zero
        numerator = np.exp(-(np.square(x - mean) / (2*var)))
        denominator = np.sqrt(2 * np.pi * var)

        return numerator/denominator
        
    def predict_single(self,x):
        posterior_class_prob = []

        # calculate posterior probability for each class
        for idx, cls in enumerate(self.classes):
            # Find log(p(y))
            prior = self.prior[idx]
            log_prior = np.log(prior)

            # Find sum (log(p(y|xi)))
            mean = self.mean[idx]
            var = self.var[idx]
            pdf = self.gaussian_pdf(mean, var, x)
            log_pdf = np.log(pdf)
            sum_log_pdf = np.sum(log_pdf)

            posterior = log_prior + sum_log_pdf
            posterior_class_prob.append(posterior)
        
        posterior_class_prob = np.array(posterior_class_prob)
        prob_class_index = np.argmax(posterior_class_prob)
        return self.classes[prob_class_index]


    def predict(self, X):
        return np.array([self.predict_single(x) for x in X])


# Test the code:

if __name__ == "__main__":
    # Imports
    from sklearn.model_selection import train_test_split
    from sklearn import datasets

    def accuracy(y_true, y_pred):
        accuracy = np.sum(y_true == y_pred) / len(y_true)
        return accuracy

    X,y = datasets.make_classification(n_samples = 100, n_features=3, n_classes=2, n_informative=2, n_redundant=0, random_state=42)


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf = NB()
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    print("NB classification accuracy:", accuracy(y_test, predictions))