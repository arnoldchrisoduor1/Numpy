import numpy as np

#copying an array
print()
print("Copying an array")
arr = np.array([3,56,76,88])
x = arr.copy()

print(x[1])

#viewing an array.
#Does not affect the original array.
print()
print("Viewing an array")
y = arr.view()
print(y[3])

#Making changes in view()
print()
print("Changing a value in view mode.")
x = arr.view()
print("Original value of arr: ", arr)
print("Original value of x =  ",x)
x[3] = 74
print("New value of x = ",x)
print("Value of original arr :",arr)
print()

#Using base() to check wo owns the data.
print("Checking who owns the data")
arr = np.array([45,67,44,65,87,98,56,9])
x = arr.view()
y = arr.copy()

print("Array that viewed : ",x.base)
print("Array that copied : ", y.base)
print()