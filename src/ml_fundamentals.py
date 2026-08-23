# Machine Learning Fundamentals (Phase 3)

## Core Concepts
```python
# Classification Example (Iris Dataset)
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load data
data = datasets.load_iris()
x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2)

# Train model
model = LogisticRegression(max_iter=200)
model.fit(x_train, y_train)

# Predict & Evaluate
y_pred = model.predict(x_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))
```

## Regression Example
```python
# Synthetic Regression Problem
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression

y, X = make_regression(n_samples=100, n_features=1, noise=0.1)
model = LinearRegression().fit(X, y)
pred = model.predict([[5.0]])
print(f"Prediction: {pred[0]:.2f}, True: {y[5]} ")
```

## Key ML Concepts
- Supervised Learning: Labeled data for training
- Unsupervised Learning: Pattern discovery in unlabeled data
- Model Evaluation: Metrics vs Business Goals
- Overfitting: When model memorizes training data
- Bias-Variance Tradeoff

## Common ML Workflow
1. Problem Definition
2. Data Collection & Preprocessing
3. Feature Engineering
4. Model Selection & Training
5. Hyperparameter Tuning
6. Evaluation & Deployment

## Exercises
1. Implement k-NN classifier on Iris dataset
2. Create a regression model with polynomial features
3. Compare performance of different classifiers

**Goal**: Understand ML lifecycle and build predictive models