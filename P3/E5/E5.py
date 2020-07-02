media = 0
suma = 0
i = 1
while media < 30:
    suma += int(input("Introduce un numero: "))
    media = (suma/i)
    print(suma,"/",i, "=", media)
    i +=1

