import random

#EJERCICIO 1 INGLES
'''1. Create a while loop with the following characteristics:

• The initial value of the variable x will be 0.
• The increment value will be 1.
• The exit condition of the loop will be greater than or equal to 30.
• The execution must be broken when x is equal to 15.
• You must print the following sentence each time the loop executes: 'The value of the loop is: ' + x.
• You must skip the executions with the value of x in 4, 6 and 10.
• At each execution jump, you must display the jumped values with this message: 'The value ' + x ' of x was skipped'.
• When the execution of the loop is broken, you must show a message indicating it: 'The execution of the loop was broken when x 
was ' + x.

x = 0
while(x <= 30):
    x = x + 1
    if(x == 15):
        print(f"The execution of the loop was broken when x was {x}")
        break

    elif(x == 4 or x == 6 or x == 10):
         print(f"Te value of {x} was skipped")
         continue
    
    print(f"{x}")'''

#EJERCICIO 1
'''1.Escriba un programa que acepte una secuencia de líneas e imprima todas las líneas convertidas 
en mayúsculas. Deje una línea en blanco para indicar que ha finalizado la entrada de líneas. 

word = input("Ingrese una frase: ").upper()

phrase = []

while(word != ""):
    phrase.append(word)

    word = input("Ingrese otra frase o enter si desea salir: ").upper()

    if(word == ""):
        print("---------")
        break

for i in range(len(phrase)):
    print(phrase[i])'''

#EJERCICIO 2
'''2.Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones.
La bitácora de operaciones tiene la siguiente forma:
D 100
R 50

D 100 significa que depositó 100 pesos
R 50 significa que retiró 50 pesos

Ejemplo de una entrada:
D 200
D 200
R 100
D 50
Introducir una línea vacía indica que ha finalizado la bitácora.
La salida de éste programa sería:
350


operation_register = []
total = 0
operation = " "
while(operation != ""):

    operation = input("Que operación desea hacer: [D] para depositar [R] para retirar: ").upper()
    if(operation != "D" and operation != "R"):
        print(f"La operacion {operation} es incorrecta")
        continue
    elif(operation == ""):
        break

    cash = int(input("Ingrese el monto que desea: "))
    
    if(operation == "D"):
        operation_register.append(str(f"D {cash}"))
        total += cash
    elif(operation == "R"):
        operation_register.append(str(f"R {cash}"))
        total -= cash

for i in range(len(operation_register)):
    print(operation_register[i])

print(f"El total es: {total}")''' 

#EJERCICIO 3
'''3.Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
finalizando cuando se reciba un cero.
Imprimir la cantidad total de números primos ingresados.
Nota: Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores distintos: él mismo 
y el 1.

prime_number = []
num = int(input("Ingrese un número: "))
aux2 = 0
counter = 1

while(num != 0):

    if(num < 1):
        print("El número no es positivo")
        continue
    elif(num == 0):
        break

    while(counter != num):
        aux = num % counter

        if(aux == 0):
            aux2 += 1
            
        counter += 1 
    
    if(aux2 == 1):
        prime_number.append(num)

    num = int(input("Ingrese otro número: "))
    counter = 1
    aux2 = 0

print("Los números primos son: ", end="")
for i in range(len(prime_number)):
    print(prime_number[i], end=" ")'''

#EJERCICIO 4
'''4.Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese 
rango, que sean bisiestos y múltiplos de 10.
Nota: Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, 
excepto que también sea divisible por 400.

#((anio%100 != 0 and anio%4 == 0) or anio%400 == 0)

first_year = int(input("Ingrese el primer año: "))
second_year = int(input("Ingrese el segundo año: "))

print("Los años biciestos y multiplos de 10 son: ")
if(first_year > second_year):

    while(first_year > second_year):

        if(((second_year%100 != 0 and second_year%4 == 0) or second_year%400 == 0) and second_year%10 == 0):
            print(second_year)

        second_year += 1
elif(first_year < second_year):

    while(first_year < second_year):
        
        if(((first_year%100 != 0 and first_year%4 == 0) or first_year%400 == 0) and first_year%10 == 0):
            print(first_year)

        first_year += 1
else:
    print("Los años ingresados son iguales")'''

#EJERCICIO 5
'''5.Escribe un programa que imprima todos los números pares del 1 al 20 usando un bucle for. 
Utiliza la declaración continue para omitir los números impares.

for i in range(1,21):
    if(i % 2 == 1):
        continue
    print(i)'''

#EJERCICIO 6
'''6.Crea una lista de números y utiliza un bucle for para encontrar un número específico. 
Cuando encuentres el número, usa break para salir del bucle.

list = []

list_size = int(input("Ingrese el tamaño de la lista que desea: "))

for i in range(list_size):
    num = random.randint(1,100)
    list.append(num)

print("La lista es: ")
for i in range(len(list)):
    print(list[i], end=" ")

print("")
find_number = int(input("Que número desea buscar:"))

for i in range(len(list)):
    if(find_number == list[i]):
        print(f"El número {find_number} esta en la posición {i+1} de la lista")
        break
    elif(i == (len(list)-1)):
        print(f"Error el número {find_number} no esta en la lista")'''

#EJERCICIO 7
'''7.Crea un programa que muestre un menú de opciones (por ejemplo, opciones 1, 2, 3). 
Utiliza un bucle while para permitir al usuario seleccionar una opción. Si el usuario ingresa "0", 
utiliza break para salir del bucle (Mostrar un mensaje por cada opción elegida).

print(f"Este es un menú de opciones: \n"
      f"Opcion 1 = '1' / Opcion 2 = '2' / Opcion 3 = '3' / Salir = '0'")

option = int(input("Ingrese una opción: "))

while(option != 0):
    if(option == 1):
        print(f"Esta es la opción {option}")
    elif(option == 2):
        print(f"Esta es la opción {option}")
    elif(option == 3):
        print(f"Esta es la opción {option}")
    else:
        print(f"La opción {option} no existe")

    option = int(input("Sigue en el menú vuelva a ingresar una opción: "))

    if(option == 0):
        break

print("Usted ha salido del menú")'''








