print("Este programa devuelve el menor de los 5 numeros introducidos")
n = int(input("Introduce un numero: "))
menor = n
while n > 0:
    n = (int(input("Introduce un numero: ")))
    if menor > n:
        menor = menor + n
        n = menor - n
        menor  = menor -n
        n = menor
print("El menor es:", menor,)