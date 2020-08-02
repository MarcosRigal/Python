a = int(input("Introduce un numero: "))
b = int(input("Introduce un numero: "))
if a>b:
    a = a + b
    b = a -b
    a = a -b
print("El valor de a es el menor:", a, ", y el de b es el mayor:", b)