import numpy as np

#NumPy provides the ufuncs sinh(), cosh() and tanh() that take values in radians and produce the corresponding sinh, cosh and tanh values..

print()
print("convert radians to sinh() values")
print(np.sinh(np.pi/2))
print()

print("converting radians to cosh values.")
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.cosh(arr)
print(x)
print()

#Numpy provides ufuncs arcsinh(), arccosh() and arctanh() that produce radian values for corresponding sinh, cosh and tanh values given.
print("Finding the angles")
print(np.arcsinh(1.0))
print()

print("Angesl of each value in the array")
arr = np.array([0.1, 0.2, 0.5])
x = np.arctanh(arr)
print(x)
print()