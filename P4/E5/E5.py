def esPrimo(n):
    if n == 0 or n == 1:
        return False
    i = int(n/2)
    while i > 1:
        if n % i == 0:
            return False
        i -= 1
    return True

print("Este programa imprime los n primeros numeros primos.")
n = int(input("¿Hasta que número primo desea calcular?: "))
i = 2
primos = 1
while primos < n:
    if esPrimo(i):
        print(i)
        primos += 1
    i += 1