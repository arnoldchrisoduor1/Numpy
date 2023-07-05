import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

#Plotting values.
x = random.randint([1, 2, 3, 4,5,6,7])
#sns.distplot(x)
#plt.show()

#Plotting without the histogram.
sns.distplot([7,6,5,4,2,3,6], hist = False)
plt.show()

