import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# read CSV with headers
df = pd.read_csv(r"C:\Users\Bhumi's laptop\PycharmProjects\PythonwithAI\assignment-3\weight-height.csv")

# cut into variables
length = df["Height"].values * 2.54        # inches → cm
weight = df["Weight"].values * 0.453592    # pounds → kg

# calculate means
print("Mean length (cm):", np.mean(length))
print("Mean weight (kg):", np.mean(weight))

# histogram
plt.hist(length, bins=10, color="lightblue", edgecolor="black")
plt.xlabel("Length (cm)")
plt.ylabel("Frequency")
plt.title("Histogram of Student Lengths (cm)")
plt.show()
