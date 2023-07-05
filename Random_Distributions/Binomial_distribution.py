from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

#Binomial Distribution is a Discrete Distribution.
#It describes the outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails.
#It has three parameters:
#n - number of trials.
#p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).
#size - The shape of the returned array.

print("Generating 10 data points for 10 trials at a coin toss")
x = random.binomial(n=10, p=0.5, size=10)
print(x)
print()

#sns.distplot(random.binomial(n=10, p=0.5, size = 1000), hist =True, kde = False)
#plt.show()

sns.distplot(random.normal(loc = 50, scale = 5, size = 1000), hist = False, label = 'normal')
sns.distplot(random.binomial(n = 100, p = 0.5, size = 1000 ), hist = False, label = 'binomial')
plt.show()