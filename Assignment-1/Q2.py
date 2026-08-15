import numpy as np

matrix = np.random.randint(1, 101, size=(5, 5))

print("5 × 5 Matrix:")
print(matrix)

print("\nSum:", np.sum(matrix))
print("Mean:", np.mean(matrix))
print("Median:", np.median(matrix))
print("Standard Deviation:", np.std(matrix))
print("Maximum:", np.max(matrix))
print("Minimum:", np.min(matrix))

one_d = matrix.reshape(-1)

print("\nOne-dimensional array:")
print(one_d)

mean = np.mean(matrix)
greater = one_d[one_d > mean]

print("\nElements greater than average:")
print(greater)