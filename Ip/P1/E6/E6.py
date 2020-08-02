print("Este programa calcula la media de 4 numeros reales")
media = 0
valor = {0: 'primer', 1: 'segundo', 2: 'tercer', 3: 'cuarto'}
for i in range(4):
    print("Introduce el", valor[i],  "numero.")
    num = float(input())
    media += num
print("La media es: ", media/4)