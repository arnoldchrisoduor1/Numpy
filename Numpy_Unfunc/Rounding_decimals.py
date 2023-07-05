import numpy as np

print()
print("Remove the decimals all together, trunc()")
arr = np.array([376.68, -34.24, 87.23, -46.78])
x = np.trunc(arr)
print(arr)
print(x)
print()

print(("Using the fix()"))
print(arr)
y = np.fix(arr)
print(y)
print()

print("Increment the preceding decimal by 1 if its >= 5")
print(arr)
z = np.around(arr)
print(z)
print()

print("Floor() to round down")
print(arr)
a = np.floor(arr)
print(a)
print()

print("Ceil() to round up")
print(arr)
b = np.ceil(arr)
print(b)
print()