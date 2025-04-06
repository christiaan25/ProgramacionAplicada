# Iterar del 1 al 20 para identificar números pares e impares
for i in range(1, 21):
    residuo = i % 2
    if residuo == 0:
        print(f'{i} es par')
    else:
        print(str(i) + ' es impar')

# Iterar del 0 al 5 para calcular el cubo de cada número
for i in range(0, 6):
    resultado = i ** 3
    print(resultado)

# Solicitar un número de repeticiones al usuario
veces = input("Ingrese un número de veces: ")
veces = float(veces)
veces = int(veces)
print(type(veces))
print(veces)

if veces == 0:
    print("No hacer nada")
else:
    for i in range(1, veces + 1):
        print("i =", i)
