import numpy as np
A=np.array([
    [3,1],
    [2,4]
])
b1=([10,12])
b2=([7,14])
solution1 = np.linalg.solve(A, b1)
solution2 = np.linalg.solve(A, b2)

print("Matrix A: ",A)

print("\nb1: ",b1)
print("AX+b1= ",solution1)

print("\nb2: ",b2)
print("AX+b2= ",solution2)