import numpy as np

#In arrays we join by axes.
#Joining using the concatenate() attribute.
print()
print("Joining using the concatenate attribute.")
arr = np.array([2,3,4,5,6])
brr = np.array([76,67,45,34])

newarr = np.concatenate((arr,brr))
print(newarr)
print()

#Joining a 2-D array along the axis = 1.
print("Joining a 2-D array along a 1 axis row.")
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(arr1)
print(arr2)
print("Joining..")
newarr = np.concatenate((arr1, arr2), axis=1)
print(newarr)

#Stacking is the same as concatenation only its done over a new axis.
print()
print("Stacking two 1-D arrays.")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1)
print(arr2)
print("Joining...")
arr = np.stack((arr1, arr2), axis=1)
print(arr)
print()

#Stacking along rows using hstacks()
print("Joining along rows using 'hstacks()'")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1)
print(arr2)
print("Joining...")
arr = np.hstack((arr1, arr2))
print(arr)
print()

#Stacking along columns using vstack().
print("Stacking along columns")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1)
print(arr2)
print("Joining...")
arr = np.vstack((arr1, arr2))
print(arr)
print()

#Stacking along height(depth) using dstack() attribute.
print("Stacking along the height")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1)
print(arr2)
print("Stacking...")
arr = np.dstack((arr1, arr2))
print(arr)
print()
