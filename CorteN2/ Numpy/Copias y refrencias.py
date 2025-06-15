import numpy as np
new_array = np.array([6, 7, 8, 9])
second_new_array = new_array[0:2]
second_new_array[1] = 4
print("Original modificado:", new_array)

array_to_copy = np.array([1, 2, 3])
copied_array = array_to_copy.copy()
copied_array[0] = 9
print("Original sin modificar:", array_to_copy)
print("Copia modificada:", copied_array)
