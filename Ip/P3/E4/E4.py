print("Este programa imprime los divisores del numero introducido por pantalla.")
n = int(input("Introduzca el número para calcular sus divisores: "))
print("Los divisores son: ")
for i in range(int(n/2)):
    i += 1
    if n % i == 0:
        print(i)