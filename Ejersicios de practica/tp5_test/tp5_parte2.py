import math

#EJERCICIO 1
'''1.Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. 
Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.'''

def DNI(dni):
    dni_str = str(dni)
    if len(dni_str) >=7 and len(dni_str)<=8:
        if dni.isdigit():
            return True
        return False
    else:
        return False
    
'''dni = input("Ingrese su DNI: ")
print(DNI(dni))'''

#EJERCICIO 2
'''2.Escribir una función que, dado un string, retorne la longitud de la última palabra. Se considera que 
las palabras están separadas por uno o más espacios. También podría haber espacios al principio o al final 
del string pasado por parámetro.'''

def longitud_ultima_palabra(cadena):
    cadena = cadena.strip()
    palabras = cadena.split()
    if palabras:
        return len(palabras[-1])
    else:
        return 0
    
'''cadena = input("Ingrese una frase: ")
print(f"La longitud de la ultima palabra es: {longitud_ultima_palabra(cadena)}")'''

#EJERCICIO 3
'''3.Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club. 
Para eso ingresará nombre completo y número de DNI de cada socio, indicando que finalizará el procesamiento mediante el ingreso de un nombre vacio.
Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse más de un nombre, en cuyo caso será: 
nombre1, nombre2, apellido. Si un socio tuviera más de un apellido, el usuario solo ingresará uno.
Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa debe dejar al usuario en un bucle hasta que ingrese un DNI correcto.
Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre, la cantidad de letras del apellido y los 3 primeros dígitos de su DNI. Ejemplo:
Nombre: María Ines Rosales
ID -> Maria7254


def DNI(dni):
    dni_str = str(dni)
    if len(dni_str) >=7 and len(dni_str)<=8:
        if dni.isdigit():
            return True
        return False
    else:
        return False
    
def name_person(name,last_name,dni):
    name_str = name.split()
    if len(name_str) == 1:  
        name1 = name_str[0]
        full_name = name1 + " "
    elif len(name_str) == 2:    
        name1 = name_str[0]
        name2 = name_str[1]
        full_name = name1 + " " + name2 + " "
    else:
        print("Ingreso un dato incorrecto!")
    cant_last_name = len(last_name)
    full_name += last_name
    DNI(dni)
    if DNI(dni) == True:
        if len(dni) == 7:
            id = int(dni) // 10000
        else:
            id = int(dni) // 100000 
    name_id = name1+ str(cant_last_name) + str(id)
    print(f"#Nombre: {full_name}")
    print(f"#ID -> {name_id}")

name = input("Ingrese su nombre: ").title()
last_name = input("Ingrese su apellido: ").title()
dni = input("Ingrese su dni: ")
name_person(name,last_name,dni)'''

#EJERCICIO 4
'''4.Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. 
Crea una función que reciba los dos números, y devuelve si el primero es múltiplo del segundo.

def multiplo(num1,num2):
    if num1 % num2 == 0:
        print(f"{num1} es multiplo de {num2}")
    else:
        print(f"{num1} no es multiplo de {num2}")

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
multiplo(num1,num2)'''

#EJERCICIO 5
'''5.Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. 
Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. 
El programa pedirá el número de días que se van a introducir.'''

def cal_temp(temp_max,temp_min):
    temperature_med=(temp_max+temp_min)/2
    return temperature_med

'''tot_days = int(input("Cuantos dias va a ingresar: "))
aux = 0

while (aux < tot_days):

    aux+=1
    print(f"Dia {aux}")

    temperature_max=float(input("Ingrese la temperatura maxima: "))
    temperature_min=float(input("Ingrese la temperatura minima: "))

    print("La temperatura media es: ", cal_temp(temperature_max,temperature_min))'''

#EJERCICIO 6
'''6.Crea una función que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra. 
Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función.

def transform_word(word_space):
    for i in word_space:
        if i != None:
            print(i, end=" ")

word=input("Ingrese una cadena de texto: ")
transform_word(word)'''

#EJERCICIO 7
'''7.Crea una función que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. 
Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.

def travel_list(list):
    max = list[0]
    min = list[0]
    for i in list:
        if (i > max):
            max = i

        elif (i < min):
            min = i

    print(f"El numero maximo es: {max}")
    print(f"El numero minimo es: {min}")

list_number = []

number = 1

while (number != 0):
    number = int(input("Ingrese un numero (ingrese 0 para terminar): "))

    if(number == 0):
        break

    if (number != 0):
        list_number.append(number)

travel_list(list_number)'''

#EJERCICIO 8
'''8.Diseñar una función que calcule el área y el perímetro de una circunferencia. 
Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.'''

def funcion_radio(radio):
    area = int(math.pi * (radio ** 2))
    perimeter = int(2 * math.pi * radio)
    return f"El área es: {area} y el perímetro es {perimeter}."

'''number = 0
while number == 0 or number<0:
    number = float(input("Ingrese el radio de la circunferencia: "))
print(funcion_radio(number))'''


#EJERCICIO 9
'''9.Crear una subrutina llamada “login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es 
“asdasd”. Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.
Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.'''

def login(name,password,tryes,maxtryes):
    if tryes != maxtryes:
        if name == "usuario1" and password == "asdasd":
            return True
        else:
            return False
    else:
        return "Se agotaron el número de intentos"
        
'''attempts = 0
while attempts <100:
    
    user = input("Ingresa el usuario: ")
    passw = input("Ingresa la contraseña: ")
    
    if login(user,passw,attempts,2) == True:
        print("Bienvenido")
        break
    
    elif login(user,passw,attempts,2) == "Se agotaron el número de intentos"  :
        print("Se agotaron el número de intentos")
        break
    
    else:
        print("Datos no válidos, inténtelo de nuevo")
        
    attempts+=1 '''

#EJERCICIO 10
'''10.Escribir una función que aplique un descuento a un precio. 
Esta función tiene que recibir un diccionario con los precios y porcentajes del carrito de compra, aplicar los descuentos a los productos del carrito  y 
devolver el precio final de la compra.

def funcion10(diccionary):
    pryce_of_things = list(diccionary.keys())
    off = list(diccionary.values())
    aux = 0
    total = 0
    while aux < len(pryce_of_things):
        total = total + pryce_of_things[aux] - (pryce_of_things[aux]*(off[aux]/100))
        aux += 1
    return total

dicc_shop = {}
aux = True
while aux == True:
    
    key = float(input("Ingrese el valor de un producto, o 0 para terminar: "))
    while key < 0:
        key = float(input("El valor del producto no puede ser negativo, ingrese un número positivo: "))
        
    if key == 0:
        break
    
    value_of_key = float(input(f"Ingrese el porcentaje de descuento del producto con valor {key}: "))
    
    while value_of_key< 0:
        value_of_key = float(input(f"El porcentaje de descuento no puede ser menor a 0, ingrese un descuento válido para el producto con precio {key}: "))
        
    dicc_shop[key] = value_of_key

print(f"Lo que tiene que pagar es: {funcion10(dicc_shop)}")'''

#EJERCICIO 11
'''11.Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de 
aplicar la función dada a cada uno de los elementos de la lista.

def funcion11_2(list,funtion):
    aux=0
    list_return = []
    while aux < len(list):
        list[aux] = funtion(list[aux])
        list_return.append(list[aux])
        aux+=1
        
    return (list_return)

def funcion11_lower(b):
    return (b.lower())

def funcion11_title(c):
    return(c.title())

def funcion11_upper(a):
        return(a.upper())

option = 1
list_word = []
while option != "0":
    word = input("Ingrese oracion al azar, si no desea agregar más oraciones ingrese 0(cero): ")
    if word == "0": 
        break
    else: 
        list_word.append(word)
        
option2 = 0
while option2 != "1" and option2 != "2" and option2 != "3":
    option2 = input("Que desea hacer con las oraciones? 1) Ponerlas todas a mayusculas  2) Ponerlas en minúsculas 3)Ponerla solamente la primera en mayúscula: ")
if option2 == "1": 
    print(funcion11_2(list_word,funcion11_upper))
elif option2 =="2":
    print(funcion11_2(list_word,funcion11_lower))
else:
    print(funcion11_2(list_word,funcion11_title))'''

#EJERCICIO 12
'''12.Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.

def diccionario_frases():
    diccionario = word.split()
    #long = len(diccionario)
    return diccionario

def longitud_word():
    long = len(word) - word.count(" ")
    return long

word = input("Ingrese una frase: ")

print("Su diccionario es: ",diccionario_frases())
print("La longitud de la frase es de: ",longitud_word())'''

#EJERCICIO 13
'''13.Escribir una función que calcule el módulo de un vector.

def module(vector):
    
    #Función que calcula el módulo de un vector.
    #Parámetros:
    #    v: Una tupla de números reales.
    #Devuelve:
    #    El módulo del vector v.
    
    return sum([x ** 2 for x in vector]) ** 0.5

print(module((5, 9)))
print(module((6, 7, 8)))'''

#EJERCICIO 14
'''14.Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función booleana que lo decida.'''

def cousin(num):
   for i in range(2,num):
       if num%i==0:           
           return False
   return True

'''number=int(input("Por favor, ingrese un numero entero:  "))
if cousin(number):
    print("Es primo")
else:
    print("No es primo")'''

#EJERCICIO 15
'''15.Escribir un programa que pida números al usuario,  motrar el factorial de cada uno y, al finalizar, 
la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.

counter_global = 0

def factorial(number):
    if(number == 0):
        return 1
    elif(number == 1):
        return 1
    else:
        return number * factorial(number-1)
    
def counter():
    global counter_global
    counter_global += 1
    return counter_global



num = int(input("Ingrese un número o -1 para salir: "))

while(num != -1):
    counter()
    print(f"El factorial de ese número es: {factorial(num)}")

    num = int(input("Ingrese otro número o cero para salir: "))

    if(num == -1):
        break

print(f"La cantidad de números que se factorizaron fue {counter_global}")'''


#EJERCICIO 16
'''16.Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de ocurrencias del dígito 
en el número, utilizando para ello una función que calcule la frecuencia.

def frecuency_number(number):
    number_list = list(str(number))
    counter = 0

    digit_selected = input("Ingrese un número del 0 al 9: ")

    for i in range(len(number_list)):
        if(number_list[i] == digit_selected):
            counter += 1

    return counter

number = int(input("Ingrese un número: "))
result = frecuency_number(number)

print(f"La cantidad de números que se repite el digito es: {result}")'''

#EJERCICIO 17
'''17.Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número que no sea primo. 
Por cada número, mostrar la suma de sus dígitos. También solicitar al usuario un dígito e informar la cantidad de veces 
que aparece en el número (frecuencia). Al finalizar el programa, mostrar el factorial del mayor número ingresado.

global_list = []

def prime_number(number):
    aux = 1
    counter = 0
    while(aux <= number):
        if(number % aux == 0):
            counter += 1
        aux += 1

    if(counter > 2):
        return 1
    else:
        return 0
    

def sum_digits(number):
    sumatory = 0

    while (number > 0):
        aux = number % 10
        number = number // 10
        sumatory += aux
    
    return sumatory

def frecuency_number(number):
    number_list = list(str(number))
    counter = 0

    digit_selected = input("Ingrese un número del 0 al 9: ")

    for i in range(len(number_list)):
        if(number_list[i] == digit_selected):
            counter += 1

    return counter

def factorial_max_number():
    aux = 0
    for i in range(len(global_list)):
        if(aux <= global_list[i]):
            aux = global_list[i]

    return factorial(aux)

def factorial(number):
    if(number == 0):
        return 1
    elif(number == 1):
        return 1
    else:
        return number * factorial(number-1)
    
num = int(input("Ingrese un número no primo: "))


while(prime_number(num) != 0):
    result = frecuency_number(num)

    print(f"La sumatoria de sus digitos es: {sum_digits(num)}")
    print(f"La cantidad de números que se repite el digito es: {result}")

    global_list.append(num)
    num = int(input("Ingrese otro número no primo: "))

print(f"El factorial del número mas grande es: {factorial_max_number()}")'''
