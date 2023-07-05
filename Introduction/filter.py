import numpy as np

#Boolean index filtering.
print()
print("Boolean index filtering")
arr = np.array([34,56,78,89])
x = np.array([True, False, True, False])
newarr = arr[x]
print(newarr)

#Conditioning filtering.
print()
print("Conditioning filtering")
arr = np.array([34, 45, 67, 67, 34, 89, 98, 65, 45])
filter_arr = []
for element in arr:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]
print(newarr)
print()

#return only even elements
print("Return only even numbers")
fill = []
for ix in arr:
    if ix%2 == 0:
        fill.append(True)
    else:
        fill.append(False)
newarr = arr[fill]
print(newarr)
print()

#newfilter
print("Easier filter")
arr = np.array([67, 74, 27, 28, 95, 26])
filter_arr = arr > 42

newarr = arr[filter_arr]
print(newarr)
print()

#easy array for even numbers
print("Easy even number filter")
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(newarr)
print()
