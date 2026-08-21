import sympy as sp
x,y=sp.symbols('x y')
f=x**2*y + 3*x*y**2

#1
df_dx=sp.diff(f,x)
df_dy=sp.diff(f,y)
print("Function: ",f)
print(f"\n∂f/∂x = {df_dx}")
print(f"∂f/∂y = {df_dy}")

#2
gradient=sp.Matrix([df_dx,df_dy])
print("\nGradient Vector: ",gradient)

#3
point={x:2,y:1}
gradient_at_point=gradient.subs(point)
print(f"\nGradient at ({point[x]},{point[y]}) = {gradient_at_point}")

#4
magnitude=sp.sqrt(gradient_at_point[0]**2 + gradient_at_point[1]**2)
print("\nMagnitude of gradient: ",magnitude, magnitude.evalf())
