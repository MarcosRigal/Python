def factorial(v):
    if v  == 0:
        return 1
    factorial = v
    while v > 1:
        v = v-1
        factorial = factorial*v
    return factorial

n = int(input("Introduce un numero para calcular su factorial: "))
if n < 0:
    resultado = - factorial(-n) 
else:
    resultado = factorial(n)
print("El factorial de", n, "es:", resultado)