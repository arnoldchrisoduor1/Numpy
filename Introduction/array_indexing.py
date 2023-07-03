import numpy as np

#accessing using indexes.
print()
print("Accessing an array")
arr = np.array([4,6,7,8,5])
print(arr[0])
print()

#Adding the third and fourth elemnts.
print("Adding the third and the fourth elements")
print(arr[2] + arr[3])
print()

#Accessing the 2-D arrays.
#the dimensions rep. the rows while the index represent the columns
arr = np.array([[56,45,7,3,66], [67,45,7,6,34,]])
print("Accessing a 2-D array")
print(arr[0,1])
print(arr[1, 3])
print()

#Accessing a 3-D array.
print("Accessing a 3-D array")
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])
print()

#negative indexing.
print("Negative Indexing")
arr = np.array([[34,56,78,45,94,48], [56,4,6,7,89,67]])
print(arr[1,-1])
print(arr[0, -2])
print()