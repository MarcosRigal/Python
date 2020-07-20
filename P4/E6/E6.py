def factorial(v):
    if v  == 0:
        return 1
    factorial = v
    while v > 1:
        v = v-1
        factorial = factorial*v
    return factorial

def combinaciones(n, k):
    return ((factorial(n))/(factorial(k)*factorial(n-k)))

print("Este programa calcula las combinaciones de n sobre k:")
n = int(input("Introduce el valor de n: "))
k = int(input("Introduce el valor de k: "))
if n < 0 or k < 0 or k > n:
    print("Error n debe ser mayor que k y este a su vez mayor o igual que 0.")
else:
    print("Las combinaciones de:", n, "sobre:", k, "son:", combinaciones(n, k))
