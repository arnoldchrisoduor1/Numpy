import numpy as np

print("From the firts index to the third.")
arr = np.array([3,56,76,45,77])
print(arr[1:4])
print()

#Negative slicing
print("Negative slicing")
print(arr[-4: -2])
print()

#Determining the steps of the slicing.
print("Determining the slicing of the index.")
print(arr[1:5:2])
print()

#Returnig every othe relement from the entire array.
print("Returning every other element from theentire array")
print(arr[::2])
print()

#Slicing a 2-D array.
print("Slicing a 2-D array:")
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1,1:4])
print()

#Returning the same index from both elements in a 2-D array.
print("Returning the 2nd index in both arrays")
print(arr[0:2], 2)
print()

#slicing from 2 elements of a 2-D array
print("Slicing from 2 elements of a 2-D array")
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])