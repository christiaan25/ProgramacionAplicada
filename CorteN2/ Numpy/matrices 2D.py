import numpy as np
mat = np.array([
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
])
print("Matriz:", mat)
print("Primera fila:", mat[0])
print("Último de primera fila:", mat[0][-1])
print("Filas 1 y 2:", mat[1:][:2])