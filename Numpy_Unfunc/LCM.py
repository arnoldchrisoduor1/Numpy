import numpy as np

num1 = 24
num2 = 8

print()
print("LCM of two numbers")
x = np.lcm(num1, num2)
print(x)
print()

print("Finding the lcm of an array")
arr = np.array([6,8,36, 48])
print(np.lcm.reduce(arr))
print()