from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
#Logistic Distribution is used to describe growth.

#Used extensively in machine learning in logistic regression, neural networks etc.

#It has three parameters:

#loc - mean, where the peak is. Default 0.

#scale - standard deviation, the flatness of distribution. Default 1.

#size - The shape of the returned array.
print()
print("Generating a 2x3 logistic sample")
x = random.logistic(loc = 1, scale = 2, size = (2, 3))
print(x)
print()

#sns.distplot(random.logistic(size = (1000)), hist = False, label = 'logistic')

sns.distplot(random.normal(scale = 2, size = 1000), hist = False, label = 'normal')
sns.distplot(random.logistic(size = 1000), hist = False, label = 'logistic')
plt.legend()
plt.show()