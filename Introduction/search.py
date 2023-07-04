import numpy as np

#Getting index of a value.
print()
print("Getting the index of a value.")
arr = np.array([1, 2, 3, 4, 5, 4, 9, 8])
x = np.where(arr == 4)
print(x)
print()

#Indexes where the values are even
print("Find the indices where the values are even")
x = np.where(arr%2 == 0)
print(x)
print()

#searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.
print("Where to insert 7 to maintain search order:")
x = np.searchsorted(arr, 7)
print(arr)
print(x)
print()

#we can give side='right' to return the right most index instead
print("Where 7 should be inserted starting from the right.")
print(arr)
x = np.searchsorted(arr, 7, side='right')
print(x)