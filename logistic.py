import numpy as np
import matplotlib.pyplot as plt

# Data: hours studied vs pass/fail
X = np.array([[1], [2], [3], [4], [5], [6], [7]])
y = np.array([[0], [0], [0], [1], [1], [1], [1]])

# Add bias term (intercept)
X_bias = np.hstack([np.ones((X.shape[0], 1)), X])

# Sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Initialize parameters
theta = np.zeros((2, 1))  # [bias, weight]
learning_rate = 0.1
epochs = 1000

# Gradient Descent
for _ in range(epochs):
    z = np.dot(X_bias, theta)
    h = sigmoid(z)
    gradient = np.dot(X_bias.T, (h - y)) / y.size
    theta -= learning_rate * gradient

# Prediction for test data
X_test = np.linspace(0, 8, 100).reshape(-1, 1)
X_test_bias = np.hstack([np.ones((X_test.shape[0], 1)), X_test])
y_prob = sigmoid(np.dot(X_test_bias, theta))

# Plot
plt.scatter(X, y, color='red', label='Actual Data')
plt.plot(X_test, y_prob, color='blue', label='Logistic Curve')
plt.xlabel("Hours Studied")
plt.ylabel("Probability of Passing")
plt.legend()
plt.show()
