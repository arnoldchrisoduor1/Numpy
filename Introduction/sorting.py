import numpy as np

#using the sort() to sort an array
print("Using the sort()")
arr = np.array([2,56,45,87,36,25,86,36])
print(arr)
print(np.sort(arr))
print()
#This method returns a copy of the array leaving the original unchanged.

#Sorting booleans.
print("Sorting boolean values")
arr = np.array([True, False, True])
print(arr)
print(np.sort(arr))
print()

#Soring a 2-D array
print("Sorting a 2-D array")
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(arr)
print("Sorting...")
print(np.sort(arr))
print()