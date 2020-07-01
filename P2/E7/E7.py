def esPrimo(n):
    i = int(n/2)
    while i > 1:
        if n % i == 0:
            return('no')
        i -= 1
    return('sí')

print("Este programa dice si el numero introducido es primo o no")
n = int(input("Introduce un numero para saber si es primo o no: "))
print("El numero", n, esPrimo(n), "es primo")