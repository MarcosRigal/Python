print("Este programa irá pidiendo números para calcular su media hasta que el número introducido sea menor o igual que 0.")
num = float(input("Introduce un número: "))
media = num
i = 1
while num > 0:
    i += 1
    num = float(input("Introduce otro número: "))
    media += num
print("La media es:", media/i)