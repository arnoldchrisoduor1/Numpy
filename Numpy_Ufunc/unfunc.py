from numpy import random
import numpy as np

print()
print("Using zip() method to add elemnts in list")
x = random.randint(100, size = 5)
y = random.randint(100, size = 5)
z = []
print(x)
print(y)
print("zipping....")
for i, j in zip(x, y):
    z.append(i + j)
print(z)
print()

print("Using the add() in numpy")
z = np.add(x, y)
print(z)
print()