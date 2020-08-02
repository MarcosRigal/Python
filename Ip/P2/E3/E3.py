print("Este programa calcula el factorial de un numero dado por teclado")
n = int(input("Intrdocuce un numero: "))
if n == 0 :
    print("El factorial de 0 es 1.")
else:
    factorial = 1
    for i in range(n):
        factorial = factorial * (i+1)
    print("El factorial de:", n, "es:", factorial)