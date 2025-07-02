
# CONJUNTOS (SETS) Y SUS OPERACIONES


# Declaración de un conjunto con duplicados
mascotas = {'perro', 'gato', 'loro', 'pez', 'gato'}
print(mascotas)  # el duplicado 'gato' se elimina automáticamente

# --------------------------------

# Conjuntos numéricos
pares = {2, 4, 6, 8, 10}
mayores = {6, 7, 8, 9, 10}

# Diferencia: elementos en 'mayores' que no estén en 'pares'
print(mayores - pares)

# Unión: todos los elementos de ambos conjuntos
print(mayores | pares)

# Intersección: elementos comunes en ambos conjuntos
print(mayores & pares)

# --------------------------------

# Imprimir conjunto original (sin orden garantizado)
print(mascotas)

# Convertir a lista ordenada alfabéticamente
mascotas_ordenadas = sorted(mascotas)
print(mascotas_ordenadas)

# CREACIÓN DE CONJUNTOS Y DICCIONARIOS VACÍOS

# Diccionario vacío
diccionario_vacio = {}
print(diccionario_vacio)

# Conjunto vacío
conjunto_vacio = set()
print(conjunto_vacio)


# RANGES Y LISTAS NUMÉRICAS

# Del 0 al 9
print(list(range(10)))

# Del 1 al 10
print(list(range(1, 11)))

# Números impares entre 1 y 10
print(list(range(1, 11, 2)))


# CONVERSIÓN ENTRE COLECCIONES


lista_animales = ['gato', 'perro', 'loro', 'pez', 'gato']
print(lista_animales)

# Eliminar duplicados convirtiendo a set
set_animales = set(lista_animales)
print(set_animales)

# Convertir de nuevo a lista
lista_unica = list(set_animales)
print(lista_unica)

# Convertir a tupla
tupla_animales = tuple(lista_unica)
print(tupla_animales)

# DICCIONARIOS Y OPERACIONES BÁSICAS


bolas = {"roja": 12, "azul": 15, "verde": 9}
print(bolas)

# Claves como lista
colores = list(bolas.keys())
print(colores)

# Valores como tupla
cantidades = tuple(bolas.values())
print(cantidades)

# Convertir en un set de tuplas
bolas_items = set(bolas.items())
print(bolas_items)

# --------------------------------

# Crear diccionario a partir de lista de tuplas
d2 = dict([('uno', 1), ('dos', 2)])
print(d2)


# STRINGS Y SUS MÉTODOS


texto = "python"

# Longitud
print(len(texto))

# Primera ocurrencia de 't'
print(texto.index('t'))

# Primer carácter
print(texto[0])

# Substring de índice 2 a 5
print(texto[2:5])

# Verificar si un carácter está en el string
print('y' in texto)


# STRINGS Y LISTAS


# Lista de caracteres
letras = ['p', 'y', 't', 'h', 'o', 'n']

# Unir todos sin espacio
palabra = "".join(letras)
print(palabra)

# Unir con guiones
print("-".join(letras))

# --------------------------------

# Dividir strings

# Por espacios
print("hola mundo python".split())

# Por un carácter específico
print("a|b|c|d".split("|"))

# Por coma y espacio, máximo 1 división
print("uno, dos, tres".split(", ", 1))


# LISTAS BIDIMENSIONALES Y MULTIDIMENSIONALES


# Matriz de 3x3
tabla = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Cambiar el primer elemento
tabla[0][0] = 99
print(tabla)

# Lista 3D
cubos = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]
print(cubos)
print(cubos[1][0][1])  # acceso a '6'


# LISTAS GRANDES Y REPETICIÓN


# Lista de 50 ceros
cincuenta_ceros = [0] * 50
print(cincuenta_ceros)

# Lista de 7 días con 24 horas cada uno (inicializadas como vacías)
horario = [[""] * 24 for _ in range(7)]
print(horario)
