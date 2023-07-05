from numpy import random
import numpy as np

arr1 = np.array(random.randint(100, size = 6))
arr2 = np.array(random.randint(100, size = 6))

print()
print("Using the add ufunc")
print(arr1)
print(arr2)
print("Adding...")
a = np.add(arr1, arr2)
print(a)
print()

print("Using subtract ufunc")
b = np.subtract(arr1, arr2)
print(arr1)
print(arr2)
print(b)
print()

print("Multiplying va;ues in an array")
c = np.multiply(arr1, arr2)
print(arr1)
print(arr2)
print(c)
print()

print("Raising to power of the secong array")
d = np.power(arr1, arr2)
print(arr1)
print(arr2)
print(d)
print()

print("Remainders from dividing two arrays")
e = np.mod(arr1, arr2)
print(arr1)
print(arr2)
print(e)
print()
#we get the same whe we use the remainder() attribute.

print("Getting both the quotient and the mode values.")
print(arr1)
print(arr2)
print("Working....")
f = np.divmod(arr1, arr2)
print(f)
print()

print("Getting absolute values of values in an array")
arr = np.array([-1,4,-6,-4,7])
g = np.absolute(arr)
print(arr)
print(g)
print()