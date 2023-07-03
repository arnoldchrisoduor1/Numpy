#Array objects in numpy are called "ndarray"
import numpy as np

arr = np.array([8, 5, 9, 4, 3])
print()
print(arr)
print(type(arr))
print()

#creating atuple array
print("Creating a tuple array.")
new = np.array((2, 3, 4, 6, 7))
print(new)
print()

#2D arrays have 1-D arrays as their elements.
print("Creating a 2-D array")

a = np.array([[7,9,6,4,9], [8,45,84,73,39]])
print(a)
print()

#3-D arrays have 2-D array as their elements.
print("Creating 3-D Arrays")
b = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(b)
print()

#The "ndim" attaribute to show us the dimensions of an array.
print("Showing the dimensions of an array - 'ndim' attribute.")
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print()

#Predefining the number of dimensions for higher dimensions.
print("Predefining the dimensions by 'ndimn' - method.")
arr = np.array([5,7,3,5,7], ndmin = 5)
print(arr)
print("Number of dimensions are : ",arr.ndim)
print()
