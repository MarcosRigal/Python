print("Este programa calcula la suma de los numeros impares, hasta el impar indicado.")
n = int(input("Hasta que impar desea sumar: "))
if n <= 0 :
    while n <= 0:
        print("Error introduzca un numero mayor que 0")
        n = int(input("Hasta que impar desea sumar: "))
suma = 0
for i in range(n+1):
    if i % 2 != 0:
        suma =  suma + i
    
print("La suma de los:", n, "primeros primos es:", suma)