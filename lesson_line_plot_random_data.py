# This script uses matplotlib to create a line graph with dynamic data.
# It plots a sequence of numbers against a set of randomly sampled values to demonstrate basic visualization.

#Import modules
import codecademylib3_seaborn
from matplotlib import pyplot as plt
import random

#Plot code execution with random numbers
numbers_a = range(1,13)
numbers_b = random.sample(range(1, 1001), 12)

plt.plot(numbers_a, numbers_b)
plt.show()
