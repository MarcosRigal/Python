def Fibonacci(n):
    if n == 1:
        print("1")
    elif n == 2:
        print("1")
        print("2")
    else:
        i = 2
        a = 1
        b = 2
        c = 3
        print("1")
        print("2")
        while i < n:
            i +=1
            print(c)
            a = b
            b = c
            c = a+b
            

print("Este programa imprime por pantalla los n premeros digitos de la sucesión de Fibonacci.")
n = int(input("Hasta que digito de la sucesión de Fibonacci desea llegar: "))
if n <= 0:
    while n <= 0:
        print("Error introduzca un valor para n mayor que 0")
        n = int(input("Hasta que digito de la sucesión de Fibonacci desea llegar: "))
Fibonacci(n)
        