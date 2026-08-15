import numpy as np

A=np.array([
    [2,1,1],
    [1,3,2],
    [1,2,4]
])

B=np.array([10,13,18])

print("Matrix A \n: ", A)
print("Vector ", B)

solution=np.linalg.solve(A,B)
print("AX=B: ",solution)

x,y,z=solution

print("\nx: ",x)
print("y: ",y)
print("z: ",z)

eq1=2*x+y+z
eq2=x+3*y+2*z
eq3=x+2*y+4*z

print("\n Verification: ")
print("Equation 1: ",eq1)
print("Equation 2: ",eq2)
print("Equation 3: ",eq3)

det_A=np.linalg.det(A)
print("\n Determinant of A: ",det_A)

if not np.isclose(det_A, 0):
    print("Since determinant is not zero, the system has a unique solution.")
else:
    print("Since determinant is zero, the system does not have a unique solution.")