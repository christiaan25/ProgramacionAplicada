import csv
import random
import os

# Nombre del archivo CSV
archivo_csv = 'numeros.csv'

# Cantidad de números binarios a generar
cantidad_numeros = 20

# Lista para guardar los números binarios
numeros_binarios = []

# Generar números aleatorios (0 o 1)
for _ in range(cantidad_numeros):
    numero = random.randint(0, 1)
    numeros_binarios.append([numero])

# Mostrar los números generados
print("Números  generados:")
for numero in numeros_binarios:
    print(numero[0])

# Verificar si el archivo ya existe
archivo_existe = os.path.isfile(archivo_csv)

# Abrir el archivo en modo agregar ('a')
with open(archivo_csv, 'a', newline='') as archivo:
    escritor = csv.writer(archivo)

    # Si el archivo es nuevo, escribir la cabecera
    if not archivo_existe:
        escritor.writerow(['Número'])  

    # Escribir los nuevos números
    escritor.writerows(numeros_binarios)

print(f"\nLos nuevos números se agregaron correctamente a '{archivo_csv}'")
