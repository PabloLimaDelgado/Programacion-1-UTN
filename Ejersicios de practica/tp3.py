#EJERCICIO 1
'''1.Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

word = input("Ingrese una palabra: ")

for i in range(10):
    print(word)'''

#EJERCICIO 2
'''2.Escribir un programa que pregunte al usuario su edad y 
muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

age = int(input("Ingrese su edad: "))
year= 1
for i in range(age):
    print(year)
    year+=1'''

#EJERCICIO 3
'''3.Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

number = int(input("Ingresar un numero entero positivo: "))
for i in range(1,number+1):
    if(i%2 != 0):
        print(i,end=", ")'''

#EJERCICIO 4
'''4.Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

number = int(input("Ingrese un numero entero positivo: "))

for i in range(number+1):
    print(number,end=", ")
    number-=1'''

#EJERCICIO 5
'''5.Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y 
    muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

amount = float(input("Ingresar la cantidad a invertir: "))
interest = float(input("Ingrese el interes anual: "))
year = int(input("Ingresar por cuantos años desea invertirlos: "))

for i in range(year): 
    capitalTotal = (amount*interest/100)
    print(f"Capital obtenido por el año {i+1} es: ",capitalTotal)
print("Debido a los intereses que genero, ahora el capital es de: ",amount+capitalTotal*year)'''

#EJERCICIO 6
'''6.Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
rectángulo como el de más abajo, de altura el número introducido.
    *
    **
    ***
    ****
    *****
    ******

int_number = int(input("Ingrese un número entero que indique la altura del triangulo: "))

for i in range(int_number+1):
    for j in range(0, i, 1):
        print("*", end="")
    print(" ")'''

#EJERCICIO 7
'''7.Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.

for i in range(1,11):
    print(f"Tabla del {i}")
    for j in range(1,11):
        print(f"{i} x {j}: {i*j}", end=" ")
        print(" ")
    print(" ")'''

#EJERCICIO 8
'''Escribir un programa que pida al usuario un número entero y muestre por
pantalla un triángulo rectángulo como el de más abajo.
            1
            3 1
            5 3 1
            7 5 3 1
            9 7 5 3 1

integer = int(input("Ingrese un número entero: "))

for i in range(1, integer + 1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print()'''

#EJERCICIO 9
'''Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña hasta que introduzca la
contraseña correcta.

password = "contraseña"

while True:
    prompt = input("Ingrese la contraseña: ")
    if prompt == password:
        print("¡Contraseña correcta!")
        break
    else:
        print("Contraseña incorrecta. Inténtelo nuevamente.")'''

#EJERCICIO 10
'''Escribir un programa que pida al usuario un número entero y muestre por
pantalla si es un número primo o no. Solicitar al usuario un número entero

integer = int(input("Ingrese un número entero: "))

is_a_prime_number = True
if integer <= 1:
    is_a_prime_number = False
else:
    for i in range(2, int(integer**0.5) + 1): #Por ejemplo, si integer es 10, entonces integer**0.5 es 3.16, int(integer**0.5) es 3 y int(integer**0.5) + 1 es 4. Así que el bucle probará los valores 2 y 3, que son los únicos números menores que la raíz cuadrada de 10 que necesitamos verificar para determinar si 10 es primo o no.
        if integer % i == 0:
            is_a_prime_number = False
            break

if is_a_prime_number:
    print(f"{integer} es un número primo.")
else:
    print(f"{integer} no es un número primo.")'''

#EJERCICIO 11
'''11.Escribir un programa que pida al usuario una palabra y luego muestre por pantalla 
una a una las letras de la palabra introducida empezando por la última.

word = input("Ingresa una palabra: ")
aux = len(word) - 1
while aux != -1:
    print(word[aux], end="")
    aux -=1'''

#EJERCICIO 12
'''12.Escribir un programa en el que se pregunte al usuario por una frase y una letra,
 y muestre por pantalla el número de veces que aparece la letra en la frase.
 
phrase=input("Ingrese una frase: ") . upper()
letter = input(f"Ingresa la letra que deseas buscar en la frase {phrase}: ") . upper()
number = 0
for letter2 in phrase:
    if letter2 == letter:
        number+=1

print(f"La letra {letter}, aparece {number} veces en la frase {phrase}")'''

# EJERCICIO 13
'''13.Escribir un programa que muestre el eco de todo lo que el usuario introduzca 
hasta que el usuario escriba “salir” que terminará.

while True:
    message=input("Ingrese un mensaje: ").lower()
    if message=="salir" or message=="exit":
        break
    print(message)'''

#EJERICIO 14
'''14.Escriba un programa que pida dos números enteros y escriba qué números
 son pares y cuáles impares desde el primero hasta el segundo.

number_one = int(input("Ingrese un número entero: "))
number_two = int(input("Ingrese otro número entero: "))

if number_two>number_one:
    num = number_two
    number_three = number_one + 1
else: 
    num = number_one 
    number_three = number_two + 1
while number_three!=num:

    if number_three%2 == 0:
        print(f"El número {number_three} es par", end=(", ") )
    else:
        print(f"El número {number_three} es impar", end=(", ") )
    number_three+=1'''

#EJERCICIO 15
'''15.Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.

number = int(input("Ingrese un número mayor que cero: "))
while number==0 or number <0:
    number = int(input("Por favor, tiene que ser mayor que cero: "))

aux = 1
dividers = ""
while aux < number+1:
    
    if number % aux == 0:
        dividers += f", {aux}"
    aux +=1

print(f"Los divisores del numero {number} son{dividers}")'''

#EJERCICIO 16
'''16.Escriba un programa que pregunte cuántos números se van a introducir, 
pida esos números y escriba cuántos negativos ha introducido.

how_many= int(input("Ingrese cuantos números se van a introducir: "))
aux = 1
negative = " "
while how_many>=aux:
    number = int(input("Ingrese un número:"))
    if number < 0:
        negative += f"{number} "
    aux +=1

print(f"Los números negativos que ingreso son:{negative}")'''

#EJERCICIO 17
'''17.Solicitar al usuario que ingrese una frase y
 luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas).

phrase = input("Ingrese una frase: ").lower()
vocal = " "
for letter in phrase:
    if letter == "a" or letter =="e" or letter =="i" or letter =="o" or letter =="u":
        if letter not in vocal:
                vocal += f"{letter} "

print(f"Las vocales ingresadas son:{vocal}")'''

#EJERCICO 18
'''18.Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. 
La sucesión comienza con los números 0 y 1 y, a partir de éstos, 
cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…

number_one = 0
number_two = 1
aux  = 0
while aux <5:
    print(number_one,number_two, end=" ")
    number_one = number_one + number_two
    number_two = number_one+number_two
    aux+=1'''

#EJERCICIO 19
'''Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, 
que será la cantidad de dinero que queremos ahorrar. A continuación, 
el programa solicitará una y otra vez las cantidades que se irán ahorrando, 
hasta que el total ahorrado iguale o supere al objetivo. 
El programa deberá comprobar que las cantidades ingresadas sean positivas.

objetive = int(input("Ingrese el monto a alcanzar con los ahorros: "))
saving = 0
while saving <=objetive:
    newMoney = int(input("Ingrese el dinero ahorrado: "))

    if(newMoney > 0):
        saving +=newMoney
    else:
        print("El dinero a depositar no es positivo")

    if saving >= objetive:
        print("¡Se alcanzo el ahorro deseado!")
        break'''

#EJERCICIO 20
'''Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
Finalmente, mostrar la sumatoria de todos los números ingresados.
num = int(input("Ingrese un número: "))
aux = 0
while num != 0:
    aux+=num
    num = int(input("Ingrese un número: "))

print(f"La sumatoria de los números es de: {aux}")'''

#EJERCICIO 21
'''21.Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál 
fue el mayor número ingresado.

num = 1
num_bigger = 0
while num != 0:
    num = int(input("Ingrese un numero: "))
    if num > num_bigger:
        num_bigger = num
        
print(f"El número mas grande fue {num_bigger}")'''

#EJERCICIO 22	
'''22.Solicitar al usuario que ingrese números enteros positivos y, por cada uno, 
imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. 
Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.

num = int(input("Ingrese un número positivo: "))
add_number_count = 0

while (num != -1):
    if(num <= 0):
        num = int(input("El número debe ser positivo: "))
    else:
         while num > 0:
            aux = num%10
            num = num // 10
            add_number_count = add_number_count + aux

    num = int(input("Ingrese un número positivo: ")) 

print(f"La sumatoria de los digitos de los números fue: {add_number_count}")'''

#EJERCICIO 23
'''23.Crear un programa que permita al usuario ingresar los montos de las compras de un cliente 
(se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), 
cortando el ingreso de datos cuando el usuario ingrese el monto 0.'''

#EJERCICIO 24
'''24.Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. 
Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, 
se le debe aplicar un 10% de descuento.

shopping = []
while True: 
    amount = float(input("Ingrese el monto del producto: "))
    
    if amount == 0:
        break
    elif amount < 0:
        print("El valor no puede ser negativo. Ingrese un nuevo monto.")
    else:
        shopping.append(amount)

value = sum(shopping)
if value > 1000:
    value -= (value * 0.10)
    print("El valor de su compra supera los $1000. Ha recibido un descuento del 10% \n")
print(f"El total de las compras es: ${value} \n")'''

#EJERCICIO 25
'''25.Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando 
todos los números enteros positivos que hay entre el 1 y ese número. El factorial de 0 es 1.

factorial = 1
num = int(input("Ingrese un numero positivo: "))

while num < 0:
    num = int(input("Ingrese un numero positivo: "))

for i in range(0, num):
    factorial += (factorial*i)
print(f"El factorial del número {num} es: {factorial}")'''






 
