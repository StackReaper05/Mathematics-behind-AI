import numpy as np
X=np.array([
    [2,3],
    [4,5],
    [6,7],
    [8,9]
])
w=np.array([0.5,1.2])
b=2
y=X@w+b
print("Matrix X: ",X)
print("Weight factor w: ",w)
print("Bias Factor: ",b)
print("Predictions: ")

for i in range(len(y)):
  print("Sample ", i+1, "Prediction: ", y[i])

new_w=np.array([1.2,0.5])
new_y=X@new_w+b
print("New weight factor w: ",new_w)
print("New predictions: ")

for i in range(len(new_y)):
  print("Sample ", i+1, "Prediction: ", new_y[i])