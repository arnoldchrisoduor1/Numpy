import numpy as np
from numpy import random

#Random numbers generated through a generation algorithm are called 'pseudo random'
print()
print("Generate random number between 1 and 100")
x = random.randint(100)
print(x)
print()

print("Generate a random float")
x = random.rand()
print(x)
print()

print("Generate a 1-D array")
x = random.randint(100, size = 5)
print(x)
print()

print("Generate a 2-D array")
x = random.randint(100, size = (3, 5))
print(x)
print()

print("Generate 1-D array of floats")
x = random.rand(5)
print(x)
print()

print("Generate a 2-D array of floats")
x = random.rand(3, 5)
print(x)
print()

print("Choosing a random number from an array")
x = random.randint(100, size = 7)
print(x)
y = random.choice(x)
print(y)
print()

print("Choosing a random number to make a 2-D array")
y = random.choice(x, size = (2,5))
print(x)
print("Genearting...")
print(y)
print()