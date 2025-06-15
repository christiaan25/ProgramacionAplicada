import numpy as np
arr = np.round(np.random.rand(5), 2)
print("Array aleatorio:", arr)
print("Primer elemento:", arr[0])
print("Todo:", arr[:])
print("Desde el índice 1:", arr[1:])
print("De 1 a 3:", arr[1:4])

arr[:] = 0
print("Reiniciado:", arr)
arr[2:5] = 0.5
print("Asignado parcialmente:", arr)