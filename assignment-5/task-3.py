import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge, Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score

"""
1) Read the data into pandas dataframe
We assume Auto.csv has columns including 'mpg', 'name', 'origin', etc.
"""

data = pd.read_csv(r"C:\Users\Bhumi's laptop\PycharmProjects\PythonwithAI\AI with python\Auto.csv")
print(data.head())

"""
2) Setup regression problem: X (features), y (target)
Exclude 'mpg' (target), 'name' (string, non-numeric), 'origin' (categorical code).
We keep only numeric explanatory variables.
"""

X = data.drop(columns=["mpg", "name", "origin"])
y = data["mpg"]

# Ensure no missing values
X = X.dropna()
y = y.loc[X.index]

# Standardize features for Ridge and LASSO
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

"""
3) Split data into training and testing sets (80/20)
"""

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

"""
4 & 5) Ridge and LASSO regression across several alphas
We search optimal alpha based on R² score on test data.
"""

alphas = np.logspace(-3, 3, 50)  # alphas from 0.001 to 1000
ridge_scores = []
lasso_scores = []

for alpha in alphas:
    ridge = Ridge(alpha=alpha)
    ridge.fit(X_train, y_train)
    ridge_scores.append(r2_score(y_test, ridge.predict(X_test)))

    lasso = Lasso(alpha=alpha, max_iter=10000)
    lasso.fit(X_train, y_train)
    lasso_scores.append(r2_score(y_test, lasso.predict(X_test)))

"""
6) Plot R² scores vs alpha for both regressors
"""

plt.figure(figsize=(8,6))
plt.semilogx(alphas, ridge_scores, label="Ridge", marker='o')
plt.semilogx(alphas, lasso_scores, label="Lasso", marker='x')
plt.xlabel("Alpha (log scale)")
plt.ylabel("R² Score (Test Data)")
plt.title("Ridge vs Lasso Regression Performance")
plt.legend()
plt.show()

"""
7) Identify alpha with best score
"""

best_ridge_alpha = alphas[np.argmax(ridge_scores)]
best_ridge_score = max(ridge_scores)

best_lasso_alpha = alphas[np.argmax(lasso_scores)]
best_lasso_score = max(lasso_scores)

print("Best Ridge: alpha=", best_ridge_alpha, "R²=", best_ridge_score)
print("Best Lasso: alpha=", best_lasso_alpha, "R²=", best_lasso_score)
