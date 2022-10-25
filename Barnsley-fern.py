import random

import matplotlib.pyplot as plt
from random import randint
x = [0]
y = [0]
for i in range(0, 50000):

    p = randint(1, 100)

    if p == 1:
        x.append(0)
        y.append(0.16 * (y[i]))

    if p >= 2 and p <= 86:
        x.append(0.85 * (x[i]) + 0.04 * (y[i]))
        y.append(-0.04 * (x[i]) + 0.85 * (y[i]) + 1.6)

    if p >= 87 and p <= 93:
        x.append(0.2 * (x[i]) - 0.26 * (y[i]))
        y.append(0.23 * (x[i]) + 0.22 * (y[i]) + 1.6)

    if p >= 94 and p <= 100:
        x.append(-0.15 * (x[i]) + 0.28 * (y[i]))
        y.append(0.26 * (x[i]) + 0.24 * (y[i]) + 0.44)

plt.figure(facecolor= "black")
plt.scatter(x, y, s = 0.2, c ='green')
plt.axis("off")
plt.show()
