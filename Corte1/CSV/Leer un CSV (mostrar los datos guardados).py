import csv

# Leer y mostrar los datos del archivo CSV
with open('alumnos.csv', mode='r') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)
