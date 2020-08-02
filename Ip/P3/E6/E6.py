import random
n = random.randint(0,1001)
print("Intente adivinar el numero aleatorio entre 0 y 1000, para ello introduzca un numero")
res = int(input("El numero es: "))
while res != n:
    if res < n:  
        print("Error, el numero es mayor.")
        res = int(input("El numero es: "))
    elif res > n:
        print("Error, el numero es menor.")
        res = int(input("El numero es: "))
print("Correcto el numero era: ", n)