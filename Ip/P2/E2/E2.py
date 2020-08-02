print("Este programa calcula el k-esimo término de la siguiente serie: 1+2+3+4+5+6+7+8+9+...+k")
print("¿Hasta que termino desea calcular?")
n = int(input("Su elección: "))
if n <= 0:
    while n <= 0:
        print("Error introduzca un numero mayor que cero: ")
        n = int(input("Su elección: "))
i = 1
resultado = 0
while i <= n:
    resultado = resultado + i
    i += 1
print("El valor de la sucesión para el término", n, "es:", resultado,)