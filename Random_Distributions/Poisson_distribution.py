from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#Poisson Distribution is a Discrete Distribution.

#It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what is the probability he will eat thrice?

#It has two parameters:

#lam - rate or known number of occurrences e.g. 2 for above problem.

#size - The shape of the returned array.

print()
print("Generating poisson data points")
x = random.poisson(lam = 2, size = (10))
print(x)
print()

#sns.distplot(random.poisson(lam = 2, size = 100), hist = True, kde = False)
sns.distplot(random.normal(loc = 50, scale = 7, size=1000), hist = False, label = 'normal')
sns.distplot(random.poisson(lam = 50, size = 1000), hist = False, label = 'Poisson')
plt.legend()
plt.show()