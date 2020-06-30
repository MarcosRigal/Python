months = {1: 'Enero que tiene 31 dias', 2: 'Febrero que tiene 28 dias', 3: 'Marzo que tiene 31 dias', 4: 'Abril que tiene 30 dias', 5: 'Mayo que tiene 31 dias', 6: 'Junio que tiene 30 dias', 7: 'Julio que tiene 31 dias', 8: 'Agosto que tiene 31 dias', 9: 'Septiembre que tiene 30 dias', 10: 'Octubre que tiene 31 dias', 11: 'Noviembre que tiene 30 dias', 12: 'Diciembre que tiene 31 dias'}
month = int(input("Introduzca un numero entre 1 y 12 para obtener el mes con el que se corresponde: "))
if month < 1 or month >12:
    while month < 1 or month >12:
        print("Error este numero no se corresponde con ningun mes")
        month = int(input("Introduce un numero válido: "))
print("El mes es: ", months[month])