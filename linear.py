import numpy as np
import matplotlib.pyplot as plt

# Step 1: Data
X = np.array([1, 2, 3, 4, 5])   # Hours studied
y = np.array([35, 48, 20, 69, 54])  # Exam scores

# Step 2: Calculate slope (b1) and intercept (b0)
mean_x = np.mean(X)
mean_y = np.mean(y)

b1 = np.sum((X - mean_x) * (y - mean_y)) / np.sum((X - mean_x)**2)
b0 = mean_y - b1 * mean_x

print(f"Intercept (b0): {b0}")
print(f"Slope (b1): {b1}")

# Step 3: Make predictions
y_pred = b0 + b1 * X

print("\nPredicted values:", y_pred)

# Step 4: Evaluate (Mean Squared Error)
mse = np.mean((y - y_pred)**2)
print("\nMean Squared Error (MSE):", mse)

# Step 5: Plot
plt.scatter(X, y, color='blue', label='Actual data')
plt.plot(X, y_pred, color='red', label='Best fit line')
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Linear Regression Example")
plt.legend()
plt.show()


#using pandas
import pandas as pd
data = {'Hours_Studied': [1, 2, 3, 4, 5],
        'Exam_Score': [10, 70, 55, 20, 99]}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)
print("\nDataFrame Description:\n", df.describe())
print("\nDataFrame Info:\n")
print(df.info())

# Step 6: Using pandas for data handling
X_pd = df['Hours_Studied'].values
y_pd = df['Exam_Score'].values
b1_pd = np.sum((X_pd - np.mean(X_pd)) * (y_pd - np.mean(y_pd))) / np.sum((X_pd - np.mean(X_pd))**2)
b0_pd = np.mean(y_pd) - b1_pd * np.mean(X_pd)
print(f"\nUsing pandas - Intercept (b0): {b0_pd}")
print(f"Using pandas - Slope (b1): {b1_pd}")
y_pred_pd = b0_pd + b1_pd * X_pd
mse_pd = np.mean((y_pd - y_pred_pd)**2)
print(f"Using pandas - Mean Squared Error (MSE): {mse_pd}")

# Step 7: Plot using pandas
plt.scatter(df['Hours_Studied'], df['Exam_Score'], color='green', label='Actual data (pandas)')
plt.plot(df['Hours_Studied'], y_pred_pd, color='orange', label='Best fit line (pandas)')
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Linear Regression Example (pandas)")
plt.legend()
plt.show()
