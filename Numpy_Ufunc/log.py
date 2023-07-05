import numpy as np
from math import log

print()
print("Using log to base 2")
arr = np.arange(1, 10)
print(arr)
print(np.log2(arr))
print()

print("Getting log to base 10")
arr = np.arange(1, 10)
print(arr)
print(np.log10(arr))
print()

print("Getting log to base e")
arr = np.arange(1, 10)
print(arr)
print(np.log(arr))
print()

print("Creating custom log")
arr = np.arange(1, 10)
print(arr)
nplog = np.frompyfunc(log, 2, 1)
print(nplog(100, 15))
print()