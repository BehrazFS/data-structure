import random
import numpy as np
import matplotlib.pyplot as plt
import search
from search import linear_search, binary_search, ternary_search

# just for generating charts and randon arrays
linear_count = []
binary_count = []
ternary_count = []
for i in range(10, 10001):
    arr = np.random.uniform(1, i, i) // 1
    item = random.randint(1, i + 100)
    search.counter = 0
    linear_search(arr, item)
    linear_count.append(search.counter)
for i in range(10, 10001):
    arr = sorted(np.random.uniform(1, i, i) // 1)
    item = random.randint(1, i + 100)
    search.counter = 0
    binary_search(arr, item, 0, len(arr) - 1)
    binary_count.append(search.counter)
for i in range(10, 10001):
    arr = sorted(np.random.uniform(1, i, i) // 1)
    item = random.randint(1, i + 100)
    search.counter = 0
    ternary_search(arr, item, 0, len(arr) - 1)
    ternary_count.append(search.counter)

plt.plot(range(10, 10001), linear_count, color='r')
plt.plot(range(10, 10001), binary_count, color='g')
plt.plot(range(10, 10001), ternary_count, color='b')
plt.xlabel("array size")
plt.ylabel("number of operations")
plt.show()
