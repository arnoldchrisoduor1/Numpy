from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#A distribution following Pareto's law i.e. 80-20 distribution (20% factors cause 80% outcome).

#It has two parameter:

#a - shape parameter.

#size - The shape of the returned array.

print()
print("Generating a 2x3 pareto distribution sample")
x = random.pareto(a = 2, size = (2, 3))
print(x)
print()

sns.distplot(random.pareto(a = 3, size = (1000)), kde = False, label = 'Pareto')
plt.legend()
plt.show()