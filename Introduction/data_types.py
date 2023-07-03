#Checking the data type of an array using the "dtype" attribute.
import numpy as np

print()
print("Checking the data type of an array:")
arr = np.array([3,45,67,78])
print(arr.dtype)
print()

#Arrays with defined data type.
print("Arrays with defined data type")
arr = np.array([3,5,6,7,8], dtype="S")
print(arr)
print(arr.dtype)
print()

#defining the size of a data type
print("Defining the type of a data type also")
arr = np.array([4,6,7,8], dtype= "i4")
print(arr)
print(arr.dtype)
print()

#Converting the data types
print("Converting the data types.")
arr = np.array([2.3, 4.5, 6.4, 87.4])
print("Before change: ",arr.dtype)
newrr = arr.astype('i')
print(newrr)
print("After Change: ",newrr.dtype)
print()
#we can also use the int parameter
#newrr = arr.astype(int)

#Cnaging from integer to boolean.
print("Changing from integer to boolean")
arr = np.array([1, 0, 3])
newrr = arr.astype(bool)
print(newrr)
print(newrr.dtype)
print()