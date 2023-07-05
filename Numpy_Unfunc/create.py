import numpy as np

print()
print("Creating my own unfunc function")
def myadd(x, y):
    return x + y
myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1,2,3,4], [5,6,7,8]))
print()

print("Checking functionif its nfunc or not")
print(type(np.add))
print()

print("Checking if it's unfunc using the if..else loop")
if type(np.add) == np.ufunc:
    print("Function is ufuc")
else:
    print("Function isn't ufunc")
print()