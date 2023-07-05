from numpy import random
import numpy as np

#Permutations is an arrangement of modules =.
#e.g e.g. [3, 2, 1] is a permutation of [1, 2, 3].
print()
print("Using the 'shuffle'")
arr = np.array([1,2,3,4,5,7])
print("Before",arr)
random.shuffle(arr)
print("After : ",arr)
print()
#Shuffle changes the original array.

print("Permutation returns a re-arranged array leaving the original array unchanged")
arr = np.array([1,2,4,6,8,5,6,7])
print(random.permutation(arr))
print()