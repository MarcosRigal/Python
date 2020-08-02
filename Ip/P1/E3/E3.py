import numpy as np

print("Este programa calcula la raiz cuadrada de un numero")
num = int(input("Introduce un numero: "))
if num < 0 :
    while num < 0:
        break
    print("No se puede hace la raiz cuadrada de un numero negativo")
    num = int(input("Introduce un numero: "))  
print("La raiz cuadrada es: ", np.sqrt(num))
