import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

"""
0) Read dataset into pandas dataframe. Assume delimiter is ',' (CSV file).
"""

data = pd.read_csv(r"C:\Users\Bhumi's laptop\PycharmProjects\PythonwithAI\AI with python\Auto.csv")
print(data.head())

"""
1) Identify variables:
Typically, 50_Startups.csv has the following columns:
- R&D Spend
- Administration
- Marketing Spend
- State (categorical)
- Profit (target variable)
"""

print("\nDataset columns:", data.columns.tolist())

"""
2) Investigate correlation between variables.
We will use .corr() to check correlations between numerical variables.
"""

corr_matrix = data.corr(numeric_only=True)
print("\nCorrelation Matrix:\n", corr_matrix)

# Heatmap for visualization
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

"""
3) Choose appropriate variables to predict company profit.
- From correlation analysis, 'R&D Spend' is usually most correlated with Profit.
- 'Marketing Spend' also has a moderate correlation.
- 'Administration' has weak correlation.
- 'State' is categorical → encode if needed, but usually less predictive.
So, we choose: R&D Spend + Marketing Spend (and optionally Administration).
"""

# One-hot encode categorical 'State'
data_encoded = pd.get_dummies(data, columns=['State'], drop_first=True)

X = data_encoded.drop('Profit', axis=1)
y = data_encoded['Profit']

"""
4) Plot explanatory variables vs profit to confirm linear dependence.
"""

for col in ['R&D Spend', 'Administration', 'Marketing Spend']:
    plt.scatter(data[col], y)
    plt.xlabel(col)
    plt.ylabel("Profit")
    plt.title(f"Profit vs {col}")
    plt.show()

"""
5) Train-test split (80/20)
"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""
6) Train linear regression model
"""

model = LinearRegression()
model.fit(X_train, y_train)

"""
7) Compute RMSE and R² values for training and testing data separately
"""

# Training performance
y_train_pred = model.predict(X_train)
rmse_train = np.sqrt(mean_squared_error(y_train, y_train_pred))
r2_train = r2_score(y_train, y_train_pred)

# Testing performance
y_test_pred = model.predict(X_test)
rmse_test = np.sqrt(mean_squared_error(y_test, y_test_pred))
r2_test = r2_score(y_test, y_test_pred)

print("\nTraining RMSE:", rmse_train)
print("Training R²:", r2_train)
print("\nTesting RMSE:", rmse_test)
print("Testing R²:", r2_test)


