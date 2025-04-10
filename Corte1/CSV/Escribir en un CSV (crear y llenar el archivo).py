import csv

# Datos de ejemplo
alumnos = [
    ["Nombre", "Edad"],
    ["Juan", 20],
    ["María", 22],
    ["Pedro", 21],
    ["Lucía", 19]
]

# Crear y escribir el archivo CSV
with open('alumnos.csv', mode='w', newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(alumnos)

print("Archivo alumnos.csv creado y datos guardados correctamente.")
