print("Este programa devuelve el menor de los 5 numeros introducidos")
menor = int(input("Introduce un numero: "))
for i in range(4):
    n = (int(input("Introduce un numero: ")))
    if menor > n:
        menor = menor + n
        n = menor - n
        menor  = menor -n
print("El menor es:", menor,)