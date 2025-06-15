import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5])
print("Forma original:", arr.shape)
reshaped = arr.reshape(2, 3)
print("Forma reshaped:", reshaped.shape)