import numpy as np

#Splitting an array into 3 parts.
print()
print("Splitting an array into 3 parts")
arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr, 3)
print(arr)
print(newarr)
print()

#Adjusting when it doesnt fit.
print("Adjusting when it doesnt fit.")
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(arr)
print(newarr)
print()

#Accessing a split array().
print("Accessing a split array")
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(arr)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])
print()

#Splitting a 2-D array
print("Splitting a 2-D array")
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(arr)
print(newarr)
print()

#Splitting 2-D arrays along axis = 1.
print("Printing a 2-D array along axis = 1")
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(arr)
print("Splitting...")
print(newarr)
print()

#hsplit() to split along the rows.
print("hsplit(), to slit along the rows.")
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)
print(arr)
print("Splitting...")
print(newarr)

#similar to dstack() and vstack() are dsplit() and vsplit()