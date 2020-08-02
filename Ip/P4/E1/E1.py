def espar(v):
    if v%2 == 0:
        return True
    return False

n = int(input("Introduce un numero para saber si es par: "))
if espar(n):
    print("El numero", n, "es par.")
else:
    print("El numero", n, "no es par.")
    