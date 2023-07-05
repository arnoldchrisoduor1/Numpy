from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


#Chi Square distribution is used as a basis to verify the hypothesis.

#It has two parameters:

#df - (degree of freedom).

#size - The shape of the returned array.

print()
print("Generating chi_square samples")
x = random.chisquare(df = 2, size = (2, 3))
print(x)
print()

sns.distplot(random.chisquare(df = 2, size = (1000)), hist = False, label = 'Chi_Square')
plt.legend()
plt.show()