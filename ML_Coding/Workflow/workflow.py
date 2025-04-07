# -*- coding: utf-8 -*-
"""
Toy Example: Basic End-to-End ML Workflow (Classification)

Demonstrates the key steps for a timed ML technical interview scenario:
1. Load & Inspect Data
1b. Univariate Visualization (NEW)
2. Basic EDA & Preprocessing Strategy
3. Train/Test Split
4. Preprocessing (Imputation, Encoding, Scaling) using Pipelines
5. Train Baseline Model with Cross-Validation (UPDATED)
6. Evaluate Model on Test Set
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder, PolynomialFeatures
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
# Set plot style
sns.set_style("whitegrid")

 
# --- 1. Create & Load Toy Dataset ---
df = pd.read_csv("../data/kaggle_toy.csv")

 
print("--- Initial Data ---")
print(df.head())
print("\n--- Data Info ---")
print(df.info())
print("\n--- Basic Statistics (Numerical) ---")
print(df.describe())
print("\n--- Basic Statistics (Categorical) ---")
print(df.describe(include='object'))
print("\n--- Missing Values ---")
print(df.isnull().sum())
print("Duplicated:")
print(df.duplicated().sum())



 

# Identify feature types for ColumnTransformer
numerical_features = ['Guest_Popularity_percentage', 'Host_Popularity_percentage', "Number_of_Ads", "Episode_Length_minutes"]
nominal_features = ['Genre', 'Publication_Day', 'Publication_Time']
ordinal_features = ['Episode_Sentiment']
experience_order = ['Negative', 'Neutral', 'Positive']
remove_features = ["id","Podcast_Name","Episode_Title"]
target = "Listening_Time_minutes"

# --- 2. Define Features and Target (for modeling) ---
X = df.drop([target] + remove_features, axis=1)
y = df[target]

 
# --- 1b. Univariate Visualization (NEW SECTION) ---
print("\n--- Generating Univariate Visualizations ---")


# Plot numerical features
print("Plotting numerical feature distributions...")
for col in numerical_features:
    sns.histplot(df[col], kde=True)
    plt.show()

# Plot categorical features
print("Plotting categorical feature distributions...")
for col in nominal_features + ordinal_features:
    sns.countplot(data=df, x=col, order=df[col].value_counts().index) # Order bars by frequency
    plt.show()

 
# --- 3. Train/Test Split ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)
print(f"\n--- Data Split ---")
print(f"Training set shape: {X_train.shape}")
print(f"Test set shape: {X_test.shape}")

 
# --- 4. Preprocessing Pipelines ---
numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler()),

])

nominal_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(sparse_output= False, drop = "first", handle_unknown='ignore'))
])

ordinal_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('ordinal', OrdinalEncoder(categories=[experience_order]))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),
        ('nom', nominal_transformer, nominal_features),
        ('ord', ordinal_transformer, ordinal_features)
    ],
    remainder='passthrough'
).set_output(transform="pandas")

X_train_tr = preprocessor.fit_transform(X_train)
X_train_tr

 
X_train_tr.columns

 
from sklearn.linear_model import LinearRegression, HuberRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.dummy import DummyRegressor

from sklearn.metrics import mean_squared_error


# --- 5. Create Full Pipeline & Train with Cross-Validation (UPDATED SECTION) ---
selector_estimator = DecisionTreeRegressor(random_state=42, max_depth=3)


models = {
    "dummy" : DummyRegressor(),
    "lr" : LinearRegression(),
    "hub" : HuberRegressor(),
    "rf" : RandomForestRegressor(random_state=42),
    "SVR" : SVR(),
}
scoring = "neg_root_mean_squared_error"

for name, model in models.items():
    full_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('selector', SelectFromModel(estimator=selector_estimator)),
        ('classifier', model)
    ])
    print("="*20, name, "="*20)
    print("\nStarting CV")
    cv_scores = cross_val_score(full_pipeline, X_train, y_train, cv=3, scoring=scoring)

    print(f"CV Scores: {cv_scores}")
    print(f"Mean CV: {np.mean(cv_scores):.4f}")
    print(f"Std CV Accuracy: {np.std(cv_scores):.4f}")


    print(f"\n Fit Model on Entire Training Set ---")
    full_pipeline.fit(X_train, y_train)

    print("\nEvaluation")
    y_pred = full_pipeline.predict(X_test)
    print(mean_squared_error(y_true=y_test, y_pred=y_pred))
    # y_pred_proba = full_pipeline.predict_proba(X_test)[:, 1]

    # accuracy = accuracy_score(y_test, y_pred)
    # print(f"Accuracy on Test Set: {accuracy:.4f}")

    # print("\nClassification Report:")
    # print(classification_report(y_test, y_pred, zero_division=0))

    # print("\nConfusion Matrix:")
    # print(confusion_matrix(y_test, y_pred))



 
# --- 7. Interpretation & Next Steps (Simulated) ---
print("\n--- Summary & Next Steps ---")
print(f"Successfully trained and evaluated a baseline Logistic Regression model.")
print(f"Cross-validation on the training set yielded a mean accuracy of ___.")
print(f"Achieved an accuracy of ____ on the unseen test data.")
print("Next steps if more time allowed:")
print("- More detailed EDA (bivariate analysis, correlations).")
print("- Experiment with different imputation strategies.")
print("- Feature engineering.")
print("- Try more complex models & hyperparameter tuning (guided by CV results).")
print("- Deeper error analysis.")


 



