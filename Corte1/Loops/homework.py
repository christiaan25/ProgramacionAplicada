a = input("Ingrese un número (a): ")
a = int(a)
b = input("Ingrese otro número (b): ")
b = float(b)
c = a + b

if a == b:
    print("Son iguales")
else:
    print("Son diferentes")

print("El tipo de a es:", type(a))
print("El tipo de b es:", type(b))
print("c =", c)

if type(a) == type(b):
    print("a y b son del mismo tipo")
else:
    print("a y b son de diferentes tipos")
