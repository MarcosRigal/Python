def esprimo(v):
    i = int(n/2)
    while i > 1:
        if n % i == 0:
            return False
        i -= 1
    return True
n = int(input("Introduce un numero para saber si es primo: "))
if esprimo(n):
    print("Es primo")
else:
    print("No es primo")