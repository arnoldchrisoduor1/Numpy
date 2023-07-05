import numpy as np

print()
print("Discrete difference to find the difference of the successive elements")
arr = np.arange(1, 10)
print(arr)
print(np.diff(arr))
print()

print("Performing discrete difference twice")
print(arr)
print(np.diff(arr, n=2))
print()