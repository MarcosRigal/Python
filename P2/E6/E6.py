print("Este programa imprime los divisores del numero introducido por pantalla.")
n = int(input("Introduzca el número para calcular sus divisores: "))
print("Los divisores son: ")
i = int(n/2)
while i > 0:
    if n % i == 0:
        print(i)
    i -= 1