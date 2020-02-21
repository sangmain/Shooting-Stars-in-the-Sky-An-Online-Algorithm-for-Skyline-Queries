import random
import matplotlib.pyplot as plt
import numpy as np
import time
data_cnt = 30
############################# Dataset D
random.seed(4379)
distances = [random.uniform(0.0, 2.0) for _ in range(data_cnt)]
prices = [random.randint(0, 200) for _ in range(data_cnt)]


dataset = []
for price, distance in zip(prices, distances):
    dataset.append([price, distance])

plt.scatter(prices, distances)
plt.show()

###########
import skyline_query as sq ### 
import skyline_query_sort as sq_sort
start = time.time()
skylines = sq.getskylines(dataset)
print("Skyline_query Algorithm")
print(skylines)
print(time.time() - start)

skylines = np.array(skylines)
plt.scatter(prices, distances, color="blue")
plt.scatter(skylines[:, 0], skylines[:, 1], color="red", label="Skylines")
plt.legend()
plt.show()


skylines = sq_sort.getskylines(dataset)
print("Skyline_query Sorted Algorithm")
print(skylines)
print(time.time() - start)

skylines = np.array(skylines)
plt.scatter(prices, distances, color="blue")
plt.scatter(skylines[:, 0], skylines[:, 1], color="red", label="Skylines")
plt.legend()
plt.show()




