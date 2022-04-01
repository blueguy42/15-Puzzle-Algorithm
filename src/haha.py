import numpy as np

x = np.array([[0, 1], [2, 3]])
y = np.array([[0, 1], [2, 3]])

print(type(x.tobytes()))
print(type(y.tobytes()))