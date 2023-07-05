from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#Rayleigh distribution is used in signal processing.

#It has two parameters:

#scale - (standard deviation) decides how flat the distribution will be default 1.0).

#size - The shape of the returned array.
print()
print("Generating a 2x3 rayleigh distribution sample")
x = random.rayleigh(scale = 2, size= (2, 3))
print(x)
print()

sns.distplot(random.rayleigh(size = 1000), hist = False, label = 'Rayleight')
plt.legend()
plt.show()

