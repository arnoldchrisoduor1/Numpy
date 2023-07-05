from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#Exponential distribution is used for describing time till next event e.g. failure/success etc.

#It has two parameters:

#scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.

#size - The shape of the returned array.

print()
print("Generating an exponential data sample")
x = random.exponential(scale = 2, size = (10))
print(x)
print()

sns.distplot(random.exponential(size = 200), hist = False)
plt.legend()
plt.show()