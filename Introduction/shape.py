import numpy as np
#The shape of an array is the number of elements in each dimension.

print()
print("Getting the shape of a 2-D array")
arr = np.array([[45, 67, 43, 5, 67], [12, 49, 36, 26, 27]])
print(arr.shape)
print("First dimension has 2 elements while the second one has 5")
print()

#shape of a predetermined array.
print("Getting the shape of a predetermined array.")
arr = np.array([3,45,67,78], ndmin = 5)
print(arr)
print(arr.shape)
print()

#reshpaing an array
print("Reshaping a 1-D to 2-D")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
#The outermost dimension will have 4 arrays, each with 3 elements:
newarr = arr.reshape(4, 3)
print("Before : ",arr)
print("After: ",newarr)
print()

#Reshape form 1-D o 3-D.
print("Reshaping from 1-D to 3-D")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print("Original: ",arr)
print("New array: ",newarr)
print()

#Returns copy() or view() : its a view.
print("Does reshape return copy or view")
arr = np.array([1,2,3,4,5,6,7,8])
print(arr.reshape(2, 4).base)
print()

#Convert 1D array with 8 elements to 3D array with 2x2 elements
print("Convert 1D array with 8 elements to 3D array with 2x2 elements:")
arr = np.array([1,2,3,4,5,6,7,8])
newarr = arr.reshape(2,2,-1)
print(newarr)
#we cannot pass the -1 to more than one dimension.

#Flattening an array - converting a multidimensional array ,
#to a 1-D array.
print()
print("Flattening a multidimensional array")
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print("Original : ",arr)
print("new : ",newarr)
print()