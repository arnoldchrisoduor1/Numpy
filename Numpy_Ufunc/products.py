import numpy as np

print()
print("Finding the product of the elemnts in an array")
arr = np.arange(1, 10)
print(arr)
print(np.prod(arr))
print()

print("The product of elemts intwo arrays")
arr1 = np.arange(1, 10)
print(arr)
print(arr1)
x = np.prod([arr, arr1])
print(x)
print()

print("Product of individual arrays")
print(arr)
print(arr1)
print(np.prod([arr, arr1], axis = 1))
print()

print("Cumulative product")
print(arr)
print(arr1)
print(np.cumprod([arr, arr1]))
print()