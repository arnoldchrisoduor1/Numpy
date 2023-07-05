import numpy as np

num1 = 6
num2 = 9

print()
print("Finding the gcd")
print(np.gcd(num1, num2))
print()

print("Finding GCDs in arrays")
arr = np.array([36, 12, 9, 24])
print(np.gcd.reduce(arr))
print()
