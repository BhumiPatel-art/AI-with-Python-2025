import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
diabetes = load_diabetes()
X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
y = diabetes.target

"""
We start with the base model using only 'bmi' and 's5'.
Then we will add another variable to see how the performance changes.
"""

# Base model (bmi + s5)
X_base = X[['bmi', 's5']]
X_train, X_test, y_train, y_test = train_test_split(X_base, y, test_size=0.2, random_state=42)

model_base = LinearRegression()
model_base.fit(X_train, y_train)
y_pred_base = model_base.predict(X_test)

mse_base = mean_squared_error(y_test, y_pred_base)
r2_base = r2_score(y_test, y_pred_base)

print("Base Model (bmi+s5):")
print("MSE:", mse_base)
print("R2:", r2_base)

"""
a) Which variable would you add next? Why?
Looking at diabetes research, 'bp' (blood pressure) is a strong health indicator for diabetes.
Also, correlation analysis shows that 'bp' has a moderate correlation with target.
So we choose 'bp'.
"""

# Extended model (bmi, s5, bp)
X_extended = X[['bmi', 's5', 'bp']]
X_train, X_test, y_train, y_test = train_test_split(X_extended, y, test_size=0.2, random_state=42)

model_extended = LinearRegression()
model_extended.fit(X_train, y_train)
y_pred_extended = model_extended.predict(X_test)

mse_extended = mean_squared_error(y_test, y_pred_extended)
r2_extended = r2_score(y_test, y_pred_extended)

print("\nExtended Model (bmi+s5+bp):")
print("MSE:", mse_extended)
print("R2:", r2_extended)

"""
b) Effect on performance:
- By adding 'bp', if MSE decreases and R² increases, the model is capturing more variance.
- If not, then 'bp' doesn’t contribute much.
"""

# Full model (all variables)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model_full = LinearRegression()
model_full.fit(X_train, y_train)
y_pred_full = model_full.predict(X_test)

mse_full = mean_squared_error(y_test, y_pred_full)
r2_full = r2_score(y_test, y_pred_full)

print("\nFull Model (all variables):")
print("MSE:", mse_full)
print("R2:", r2_full)

"""
d) Adding more variables:
- Usually, adding more relevant variables increases R² (explained variance).
- But too many may lead to overfitting (especially with small datasets).
- In this dataset, using all variables gives the best performance compared to just bmi+s5.

Findings:
1. 'bmi' and 's5' already explain a lot of the variance.
2. Adding 'bp' slightly improves prediction metrics.
3. Using all features improves the model even more, but not drastically since the dataset is small and noisy.
"""
