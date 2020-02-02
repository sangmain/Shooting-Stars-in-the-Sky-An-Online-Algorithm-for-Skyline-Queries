import random
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

data_cnt = 30
############################# Dataset D
random.seed(4379)
distances = [random.uniform(0.0, 2.0) for _ in range(data_cnt)]
prices = [random.randint(0, 200) for _ in range(data_cnt)]

dataset = pd.DataFrame({"price": prices, "distance": distances})

# print(dataset.duplicated(['distance', 'price']))
dataset.plot.scatter(x="price", y="distance")

########
import skyline_query as sq
print(sq.getskylines(dataset))