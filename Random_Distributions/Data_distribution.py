import numpy as np
from numpy import random

#Random distribution is a set of numbers following a certain probebility density function
#Probability density function : a function tha describes a continuous probability.
#In the choice() probebility os set bewteen 0 - 1 and has to add upto 1.

print()
print("Generating random numbers")
x = random.choice([3, 5 ,7, 9], p=[0.1, 0.6, 0.3, 0.0], size=(3, 5))
print(x)
print()
