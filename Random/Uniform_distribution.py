from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#Used to describe probability where every event has equal chances of occuring.

#E.g. Generation of random numbers.

#It has three parameters:

#a - lower bound - default 0 .0.

#b - upper bound - default 1.0.

#size - The shape of the returned array.
print()
print("Creating a 2x3 uniform distribution sample")
x = random.uniform(size = (2, 3))
print(x)
print()

sns.distplot(random.uniform(size=1000), hist = False)
plt.show()