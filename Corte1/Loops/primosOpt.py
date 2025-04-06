def es_primo(n):
    if n < 2:
        return False
    for div in range(2, int(n ** 0.5) + 1):  # Solo iteramos hasta la raíz cuadrada de n
        if n % div == 0:
            return False
    return True

# 9) Imprimir los números primos entre 0 y 30
print("Números primos entre 0 y 30:")
for num in range(31):
    if es_primo(num):
        print(num)

# 11) Evaluar optimización con y sin break
def contar_ciclos(tope, usar_break):
    ciclos = 0
    primos = []
    for num in range(tope):
        if num < 2:
            continue
        primo = True
        for div in range(2, int(num ** 0.5) + 1):
            ciclos += 1
            if num % div == 0:
                primo = False
                if usar_break:
                    break
        if primo:
            primos.append(num)
    return ciclos, primos

tope_rango = 100
ciclos_sin_break, primos_sin_break = contar_ciclos(tope_rango, False)
ciclos_con_break, primos_con_break = contar_ciclos(tope_rango, True)

print(f"Cantidad de ciclos sin break: {ciclos_sin_break}")
print(f"Cantidad de ciclos con break: {ciclos_con_break}")
print(f"Optimización: {100 * ciclos_con_break / ciclos_sin_break:.2f}% de ciclos aplicando break")