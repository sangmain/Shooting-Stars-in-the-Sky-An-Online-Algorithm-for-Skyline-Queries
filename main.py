import random
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

data_cnt = 30
############################# Dataset D
random.seed(4379)
# distances = [random.randint(0, 200) for _ in range(data_cnt)]/
# distances = [random.uniform(0.0, 2.0) for _ in range(data_cnt)]
distances = [random.randint(0, 5000) for _ in range(data_cnt)]

prices = [random.randint(0, 5000) for _ in range(data_cnt)]

# dataset = pd.DataFrame({"price": prices, "distance": distances})
dataset = []
for price, distance in zip(prices, distances):
    dataset.append([price, distance])

# print(dataset.duplicated(['distance', 'price']))
print()
# plt.scatter(prices, distances)
# # dataset.plot.scatter(x="price", y="distance")
# plt.show()

# ########
import skyline_query as sq
# import skyline_query2 as sq
skylines = sq.getskylines(dataset)

skylines = np.array(skylines)

plt.scatter(prices, distances, color="blue")
plt.scatter(skylines[:, 0], skylines[:, 1], color="red", label="Skylines")
plt.legend()
plt.show()
# dataset.plot.scatter(x="price", y="distance", color="blue")
# plt.scatter(skylines[:, 0], skylines[:, 1], color="red", label="Skylines")
# plt.xlim(0.34752048913785316,  190.65247951086215) 
# plt.ylim(-0.06839386840927793, 2.0993498601356593)
# plt.savefig("Result")
# plt.show()