
# Step 1: Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

# Step 2: Read the dataset (note the delimiter is ';')
df = pd.read_csv("bank.csv", delimiter=';')
print("Dataset loaded successfully!\n")
print(df.head())
print(df.info())

# Step 3: Select relevant columns for analysis
df2 = df[['y', 'job', 'marital', 'default', 'housing', 'poutcome']]
print("\nSelected columns:\n", df2.head())

# Step 4: Convert categorical columns into dummy variables
df3 = pd.get_dummies(df2, columns=['job', 'marital', 'default', 'housing', 'poutcome'])
print("\nAfter converting categorical variables to dummy variables:\n", df3.head())

# Convert target column 'y' to numeric before correlation
df3['y'] = df3['y'].apply(lambda x: 1 if x == 'yes' else 0)

# Step 5: Produce a heatmap of correlation coefficients
plt.figure(figsize=(12, 8))
sns.heatmap(df3.corr(), cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

"""
Observation:
Most dummy variables have very low correlation with each other.
Some 'poutcome_success' or 'poutcome_failure' categories might show mild correlation with target 'y'.
Overall, variables are fairly independent.
"""

# Step 6: Prepare target and explanatory variables
X = df3.drop('y', axis=1)
y = df3['y']

# Step 7: Split into training and testing sets (75/25)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
print("\nData split complete:")
print(f"Training samples: {X_train.shape[0]}, Testing samples: {X_test.shape[0]}")

# Step 8: Logistic Regression Model
log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(X_train, y_train)
y_pred_log = log_reg.predict(X_test)

# Evaluate Logistic Regression
cm_log = confusion_matrix(y_test, y_pred_log)
acc_log = accuracy_score(y_test, y_pred_log)
print("\nLogistic Regression Results:")
print("Confusion Matrix:\n", cm_log)
print("Accuracy:", acc_log)

sns.heatmap(cm_log, annot=True, fmt='d', cmap='Blues')
plt.title("Logistic Regression Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Step 9: K-Nearest Neighbors (KNN)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)

# Evaluate KNN
cm_knn = confusion_matrix(y_test, y_pred_knn)
acc_knn = accuracy_score(y_test, y_pred_knn)
print("\nK-Nearest Neighbors (k=3) Results:")
print("Confusion Matrix:\n", cm_knn)
print("Accuracy:", acc_knn)

sns.heatmap(cm_knn, annot=True, fmt='d', cmap='Greens')
plt.title("KNN Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Step 10: Compare results
print("\nModel Comparison:")
print(f"Logistic Regression Accuracy: {acc_log:.4f}")
print(f"KNN (k=3) Accuracy: {acc_knn:.4f}")
