print("Este programa dice si el número introducido es mayor menor o igual que cero")
num = int(input("Introduce un número: "))
if num < 0:
    print("El numero es menor que 0.")
elif num == 0:
    print("El numero es igual que 0.")
elif num > 0:
    print("El numero es mayor que 0.")