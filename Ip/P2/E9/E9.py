def suma(n):
    suma = 0
    for i in range(n+1):
        if i % 2 == 0 or i % 3 == 0:
            suma += i
    return suma

print("Este programa calcula la suma de los numeros divisibles entre 2 o 3 hasta el numero introducido por el usuario")
n = int(input("Introduzca un numero: "))
print("La suma es:", suma(n))