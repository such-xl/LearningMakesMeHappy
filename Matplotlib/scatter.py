import matplotlib.pyplot as plt
import numpy as np

n = 1024

X = np.random.normal(0, 1, n)
Y = np.random.normal (0, 1, n)

T = np.arctan2(Y, X)
plt.xticks(())
plt.yticks(())
plt.scatter(X, Y, s=35, c=T, alpha=.5)
plt.show()