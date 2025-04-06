while True:
    valor = int(input("Ingrese un número entero positivo: "))
    print("Valor: ", valor)
    es_entero = isinstance(valor, int)
    
    if es_entero and valor > 0:
        factorial = 1
        for i in range(1, valor + 1):
            factorial *= i
        print(f'El factorial de {valor} es: ', factorial)
    else:
        print("Por favor, ingrese un número entero positivo.")
