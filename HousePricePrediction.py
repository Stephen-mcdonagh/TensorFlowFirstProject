# House Price Prediction Example

import tensorflow as tf
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Generate some house sizes, between 1000 -> 3500 square feet

num_houses = 160
np.random.seed(42)
house_size = np.random.randint(low=1000, high=3500,size = num_houses)

#Generate House Prices from house size with a random noise added

np.random.seed(42)
house_price = house_size * 100 + np.random.randint(low = 20000, high = 70000, size = num_houses)

#Plot on graph the generate prices
plt.plot(house_size, house_price, "bx")
plt.ylabel("PRICE")
plt.xlabel("SIZE")
plt.show()