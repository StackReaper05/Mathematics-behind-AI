import numpy as np

A=np.array([
    [2,1,3],
    [4,5,2],
    [1,2,4]
])

B=np.array([
    [1,2,1],
    [3,1,2],
    [2,4,3]
])

addition=A+B

subtraction=A-B

matrix_product=A@B

element_product=A*B

transpose=A.T

trace=np.trace(A)

print("Matrix A: \n",A)
print("Matrix B: \n",B)
print("Matrix addition: \n",addition)
print("Matrix subtraction: \n",subtraction)
print("Matrix product: \n",matrix_product)
print("Element wise product: \n",element_product)
print("`Transpose of A: \n",transpose)
print("Trace of A: \n",trace)