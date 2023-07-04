import  numpy as np

#looping through a 1-D array.
print()
print("Looping through a 1-D array")
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
for x in arr:
    print(x)

print()

#Iterating through a 2-D array.
print("Itertaing through a 2-D array")
newarr = arr.reshape(2,6)
for x in newarr:
    print(x)

#Iterating on each scalar of an array in a 2-D
print("Iterating through each scalar in a 2-D array")
for x in newarr:
    for y in x:
        print(y)
print()

#Iterating through a 3-D array.
print("Iterating through a 3-D array")
newarr = arr.reshape(2,2,3)
print(newarr)
for x in newarr:
    for y in x:
        for z in y:
            print(z)
print()

#Using nditer() to loop through a 3-D array.
print("Using nditer(), to loop through a 3-D array")
print(newarr)
for x in np.nditer(newarr):
    print(x)

#We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.
print("Changing the data type while itertaing.")
print(newarr)
for x in np.nditer(newarr, flags=['buffered'], op_dtypes=['S']):
    print(x)

#Iterating a multidimensional array with different step size.
print()
print("Iterating a multidimensional array with different step size")
print(newarr)
for x in np.nditer(newarr[:, ::2]):
    print(x)
print()

#Enumeration - getting the index while loopinng using the ndenumerate()
print("Getting the index, using the ndumerate()")
print(newarr)
for idx, x in np.ndenumerate(newarr):
    print(idx, x)
print()