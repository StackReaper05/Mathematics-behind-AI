import numpy as np

A=np.array([
    [4,2,1],
    [2,5,3],
    [1,3,6]
])

print("Matrix A: \n",A)

det_A=np.linalg.det(A)
print("Determinant of A: ",det_A)	

if det_A==0:
  print("Matrix is singular")
else:
  print("Matrix is not singular")

inverse_A=np.linalg.inv(A)
print("Inverse of A: \n",inverse_A)

result=A@inverse_A
print("Result: \n",result)