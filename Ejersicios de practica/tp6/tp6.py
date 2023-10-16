import funciones;

#EJERCICIO 1
'''1. Solicitar al usuario que ingrese números, estos deben guardarse en una lista. Para finalizar el 
usuario debe ingresar 0, el cual no debe guardarse.

list_number=[]

while (True):

    number = int(input("Ingrese un numero(ingrese 0 para terminar): "))
    if (number==0):
        break
    else:
        list_number.append(number)

print(list_number)'''

#EJERCICIO 2
'''2. A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su 
primera ocurrencia. Mostrar un mensaje si no es posible eliminar.

funciones.delet_number(list_number)'''

#EJERCICIO 3
'''3. Imprimir la sumatoria de todos los números de la lista.

print(f"La suma de todos los numeros de la lista es: {funciones.sum_numbers(list_number)}")'''

#EJERCICIO 4
'''4. Solicitar al usuario otro número y crear una lista con los elementos de la lista original, que sean 
menores que el número dado. Imprimir esta nueva lista, iterando por ella.

print(funciones.num_minors(list_number))'''

#EJERCICIO 5
'''5. Generar e imprimir una nueva lista que contenga como elementos a tuplas, cada una compuesta
por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista
original es [5,16,2,5,57,5,2], la nueva lista contendrá: [(5,3),(16,1),(2,2),(57,1)]


len_list = int(input("Ingrese el tamaño de la lista: "))
list = funciones.fill_list(len_list)

counter = 0
j = 0

list_tuple = []

for i in range(len(list)):
    aux_position = list[i]

    if(aux_position == list[i]):     
        for i in list:
            if(aux_position == i):
                counter += 1

    aux_tuple = (aux_position, counter)

    if (aux_tuple not in list_tuple):
        list_tuple.append(aux_tuple)
    counter = 0

print(f"El array es: {list}")  
print(f"El array de tuplas es: {list_tuple}")'''

#EJERCICIO 6
'''6. Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela,
finalizando al ingresar 'x'. A continuación, solicitar que ingrese los nombres de los alumnos de nivel
secundario, finalizando al ingresar 'x'.
a. Informar los nombres de todos los alumnos de nivel primario y de los de nivel secundario,
sin repeticiones.
b. Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
c. Informar qué nombres de nivel primario no se repiten en los de nivel secundario.

aux_bool_secondary = True
aux_bool_primary = True

list_name_secondary = []
list_name_primary = []

while(aux_bool_secondary == True):
    insert_name = input("Ingrese el nombre del alumno de la secundaria o 'x' para salir: ").strip()

    if(insert_name == "X" or insert_name == "x"):
        break

    list_name_secondary.append(insert_name.title())

while(aux_bool_primary == True):
    insert_name = input("Ingrese el nombre del alumno de la primaria o 'x' para salir: ").strip()

    if(insert_name == "X" or insert_name == "x"):
        break

    list_name_primary.append(insert_name.title())

funciones.show_names(list_name_primary, list_name_secondary)
funciones.show_names_repeted_list(list_name_primary, list_name_secondary)
funciones.show_names_repeted_list_primary(list_name_primary, list_name_secondary)'''

#EJERCICIO 7
'''7. Escribir un programa que procese strings ingresados por el usuario. La lectura finaliza cuando se
hayan procesado 50 strings. Al finalizar, informar la cantidad total de ocurrencias de cada carácter,
en todos los strings ingresados. Ejemplo:
‘r’:5
‘%’:3
‘a’:8
‘9’:1

num_strings = 0
character_counts = {}

while num_strings < 5:
    string_word = (input("Ingrese una frase: ").strip()).lower()
    num_strings += 1

    for char in string_word:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1

for char, count in character_counts.items():
    print(f"'{char}':{count}")'''


#EJERCICIO 8
'''Diez equipos de la liga inter-barrial identificados con los números 1, 2, 3, 4, …, 10, participaron en
un campeonato de fútbol con modalidad todos contra todos.

Escriba un programa que:
o Lea el cuadro de goles en un arreglo de dos dimensiones.
o Muestre para cada equipo la cantidad de triunfos, empates y derrotas.
o Muestre la diferencia entre el total de goles marcados y el total de goles recibidos.
o Determine la cantidad de puntos obtenidos por cada equipo.


print(funciones.resultado_final(funciones.equipos_resultado()))'''

#EJERCICIO 9
'''9. Escribir un programa que simule el juego clásico de Memoria (Memotest) utilizando matrices. El
juego consiste en un tablero de cartas boca abajo y el objetivo es encontrar todas las parejas de
cartas iguales.

print(funciones.juego_memo(funciones.make_memo()))'''

#EJERCICIO 10
'''10. Teniendo una matriz cuadrada de cualquier dimensión, obtener lo siguiente:
a. la diagonal principal.
b. la diagonal inversa.

matriz = [[4,5,8,12],[4,7,9,14], [8,7,5,17], [15,3,2,25]]
print(funciones.matriz_inDiagonal(matriz))'''

#EJERCICIO 11
'''11. Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en
el diccionario.'''

#EJERCICIO 12
'''12. Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en
un diccionario. Después debe mostrar por pantalla el mensaje ‘<nombre> tiene <edad> años, vive
en <dirección> y su número de teléfono es <teléfono>’.'''

#EJERCICIO 13
'''13. Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al
usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos
de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.'''