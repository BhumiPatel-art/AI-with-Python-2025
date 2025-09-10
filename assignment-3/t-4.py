import numpy as np

# define matrix A
A = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])

# find inverse
A_inv = np.linalg.inv(A)

# multiply A * A_inv and A_inv * A
prod1 = A.dot(A_inv)
prod2 = A_inv.dot(A)

# print results
print("Matrix A:")
print(A)

print("\nInverse of A:")
print(A_inv)

print("\nA * A_inv:")
print(prod1)

print("\nA_inv * A:")
print(prod2)
