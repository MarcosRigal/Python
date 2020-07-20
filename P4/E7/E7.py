def nDivisores(n):
    nDivisores = 0
    for i in range(int(n/2)):
        i += 1
        if n % i == 0:
            nDivisores +=1
    return nDivisores

n = int(input("Introduce un numero para obtener su numero de divisores: "))
print(n, "tiene:", nDivisores(n), "divisores")