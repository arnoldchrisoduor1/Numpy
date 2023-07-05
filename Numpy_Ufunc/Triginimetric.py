import numpy as np

#the ufuncs sin(), cos() and tan() take radian values.
print()
print("sin of pi/2")
x = np.sin(np.pi/2)
print(x)
print()

print("Find sin of all values in an array")
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
print(np.sin(arr))
print()

#Radians = pi/180 * degree_value.
print("Converting degree to rad")
arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
print(x)
print()

print("Coverting radians to degrees")
arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
print(np.rad2deg(arr))
print()

#NumPy provides ufuncs arcsin(), arccos() and arctan() that produce radian values for corresponding sin, cos and tan values given.
print("Finding agles form sine value")
print(np.arcsin(1.0))
print()

print("Finding angles form array of sin values")
arr = np.array([1.0, -1, 0.5])
print(np.arcsin(arr))
print()

print("Finding hypoteneus")
base = 3
height = 4
print(np.hypot(base, height))
print()