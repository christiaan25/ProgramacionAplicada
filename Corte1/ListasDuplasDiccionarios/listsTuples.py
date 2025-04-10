########################### LISTAS ###########################
#############################################################

# Definición de una lista de colores
lista_colores = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']

print(lista_colores)
print(type(lista_colores))
print("Elemento en la posición 2:", lista_colores[2])

print("Tamaño de lista_colores:", len(lista_colores))

print("Elementos desde la posición 0 hasta antes de la 2:", lista_colores[0:2])
print("Elementos hasta antes de la posición 2:", lista_colores[:2])

# Agregar elementos
lista_colores.append('Blanco')  # Agrega al final
print(lista_colores)

lista_colores.insert(3, 'Negro')  # Inserta en la posición 3
print(lista_colores)

# Concatenar otra lista
lista_colores.extend(['Marrón', 'Gris'])
print(lista_colores)

# Buscar posición de un elemento
print("Posición de 'Azul':", lista_colores.index('Azul'))

# Eliminar un elemento específico
lista_colores.remove('Marrón')
print(lista_colores)

# Insertar nuevamente 'Marrón' en posición 8
lista_colores.insert(8, 'Marrón')
print(lista_colores)

# Eliminar y mostrar el último elemento
print("Elemento eliminado:", lista_colores.pop())

print("Tamaño actual:", len(lista_colores))

# Repetir lista 3 veces
lista_colores_repetida = lista_colores * 3
print("Lista repetida:", lista_colores_repetida)

# Ordenar lista (alfabéticamente)
print("Lista ordenada:")
lista_colores.sort()
print(lista_colores)

# Lista de números
lista_numeros = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print("Lista de números ordenada de menor a mayor:")
lista_numeros.sort()
print(lista_numeros)

print("Lista de números ordenada de mayor a menor:")
lista_numeros.sort(reverse=True)
print(lista_numeros)

########################### TUPLAS ###########################
#############################################################

print("###########################")
print("########## TUPLAS #########")

# Convertir lista en tupla (inmutable)
tupla_colores = tuple(lista_colores)
print("Tupla de colores:", tupla_colores)

print("Primer elemento:", tupla_colores[0])
print("Tercer elemento:", tupla_colores[2])

# Verificar si un elemento está en la tupla
print("¿'Rojo' está en la tupla?", 'Rojo' in tupla_colores)
print("Cantidad de veces que aparece 'Rojo':", tupla_colores.count('Rojo'))

# Tupla con un solo elemento (importante la coma)
tupla_un_elemento = ('Blanco',)
print("Tupla con un solo elemento:", tupla_un_elemento)

# Empaquetado de tupla
datos_personales = 'Gaspar', 5, 8, 1999
print("Datos personales:", datos_personales)

# Desempaquetado de tupla
nombre, dia, mes, anio = datos_personales
print("Nombre:", nombre)
print("Día:", dia)
print("Mes:", mes)
print("Año:", anio)

print(f"Nombre: {nombre} - Día: {dia} - Mes: {mes} - Año: {anio}")

# Convertir tupla en lista
lista_datos_personales = list(datos_personales)
print("Datos personales en lista:", lista_datos_personales)
