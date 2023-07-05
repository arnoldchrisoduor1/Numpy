import numpy as np

print()
print("Summations over elements")
arr1 = np.arange(1, 8)
arr2 = np.arange(1, 8)
print(arr1)
print(arr2)
arr = np.sum([arr1, arr2])
print(arr)
print()

print("Sum vaues in each array")
print(arr1)
print(arr2)
arr = np.sum([arr1, arr2], axis = 1)
print(arr)
print()

print("Performing cumulative sum")
print(arr1)
arr = np.cumsum([arr1])
print(arr)
print()