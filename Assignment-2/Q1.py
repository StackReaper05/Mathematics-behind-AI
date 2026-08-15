import numpy as np
a=np.array([2,4,6,8])
b=np.array([1,3,5,7])

addition=a+b

subtraction=a-b

dot_product=np.dot(a,b)

normal_a=np.linalg.norm(a)
normal_b=np.linalg.norm(b)
 
cosine_similarity=(dot_product)/(normal_a*normal_b)

print("Vector a: ", a)
print("Vector b: ", b)

print("Vector addition: ", addition)
print("Vector subtraction: ", subtraction)

print("Dot product of a & b: ", dot_product)

print("Normal form of a: ",normal_a)
print("Normal form of b: ",normal_b)