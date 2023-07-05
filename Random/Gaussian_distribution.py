from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#It has three parameters:
#loc - (Mean) where the peak of the bell exists.
#scale - (Standard Deviation) how flat the graph distribution should be.
#size - The shape of the returned array.
print()
print("Generating a normal distribution.")
x = random.normal(size = (2, 3))
print(x)
print()

print("Generating  random distributiin of s.d =2 and loc = 1")
x = random.normal(loc = 1, scale = 2, size = (2, 3))
print(x)
print()

sns.distplot(random.normal(size = 1000), hist = False)
plt.show()

#This curve is also known as a bell curve because of the shape.
