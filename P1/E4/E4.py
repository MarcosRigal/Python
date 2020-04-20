print("Este programa pide un numero y devuelve el día de la semana asociado")
num = int(input("Introduce un numero: "))
if num < 1 or num > 7:
    while num < 1 or num > 7:
        break
    print("Este numero no se corresponde con ningún dia de la semana")
    num = int(input("Introduce un numero valido: "))  
days = { 1:'Lunes' , 2:'Martes' , 3:'Miercoles' ,  4:'Jueves' , 5:'Viernes' , 6:'Sabado' , 7 : 'domingo' }
day = days[num]
print("El numero: ", num ,"Equivale al: ", day)