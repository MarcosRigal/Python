def esPerfecto(n):
    suma = 0
    for i in range(int(n/2)):
        i += 1
        if n % i == 0:
            suma = suma +i
    if suma == n:
        return True
    return False    


n = int(input("Introduce un numero para saber si es perfecto: "))
if esPerfecto(n):
    print("Sí,", n, "es un numero perfecto.")
else:
    print("No,", n, "no es un numero perfecto.")