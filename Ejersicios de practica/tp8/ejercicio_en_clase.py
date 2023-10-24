import random
import funciones

#EJERCICIO EN CLASE 1
'''1. Escribir una función que simule el siguiente experimento: Se tiene una rata en una
jaula con 3 caminos, entre los cuales elige al azar (cada uno tiene la misma
probabilidad), si elige el 1 luego de 3 minutos vuelve a la jaula, si elige el 2 luego de 5
minutos vuelve a la jaula, en el caso de elegir el 3 luego de 7 minutos sale de la jaula.
La rata no aprende, siempre elige entre los 3 caminos con la misma probabilidad, pero
quiere su libertad, por lo que recorrerá los caminos hasta salir de la jaula.

mouse = funciones.recursive_mouse(0)

print(f"La cantiad de minutos que el mouse estuvo en la jaula fue: {mouse} minutos")'''

#EJERCICIO EN CLASE 2
'''2. Una funcion recursiva que devuelve en forma de string el número con los digitos en el 
orden inverso al que fueron mandados. Por ejemplo si ingresamos el número 210, nos va a devolver 012

print(funciones.f(998332312))'''


#EJERCICIO 1
'''1. Escribir una función que reciba un número positivo n y devuelva la cantidad de dígitos que tiene.

numero = int(input("Ingrese un número positivo: "))
while (True) and (numero != 0):

 if numero > 0:
     print("El número tiene", funciones.count_digits(numero), "dígito(s).")
 else: 
     print ("Numero entero POSITIVO INCORRECTO. ") 
     break
 numero = int(input("Ingrese un número positivo: "))'''

#EJERCICIO 2
'''2. Escribir una función que reciba 2 enteros n y b y devuelva True si n es potencia de b.
n = int(input("Ingrese un número n: "))
b = int(input("Ingrese un número b: "))

if funciones.es_potencia(n, b):
    print(f"{n} es una potencia de {b}.")
else:  
    print(f"{n} no es una potencia de {b}.")'''

#EJERCICIO 3
'''3. Escribir una funcion recursiva que reciba como parámetros dos strings a y b, y devuelva una lista
con las posiciones en donde se encuentra b dentro de a. Ejemplo:

cadena_a = "mi mama me mima"
cadena_b = "ma"

posiciones = funciones.encontrar_posiciones(cadena_a, cadena_b)
print(f"Las posiciones de '{cadena_b}' en '{cadena_a}' son: {posiciones}")'''

#EJERCICIO 4
'''4. Escribir dos funciones mutualmente recursivas par(n) e impar(n) que determinen la paridad del
numero natural dado, conociendo solo que:
• 1 es impar.
• Si un número es impar, su antecesor es par; y viceversa.

numero = int(input("Ingrese un numero: "))

if funciones.par(numero):
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")'''

#EJERCICIO 5
'''5. Escribir una función recursiva que encuentre el mayor elemento de una lista.

array = []

for i in range(10):
    num = int(random.random()*100)
    array.append(num)

print(f"La lista es: {array}")

print(f"El número mas grande de la lista es: {funciones.max_list_num(array, 0, 0)}")'''

#EJERCICIO 6
'''6. Escribir una función recursiva para replicar los elementos de una lista una cantidad n de veces. Por
ejemplo, replicar ([1, 3, 3, 7], 2) = ([1, 1, 3, 3, 3, 3, 7, 7])

array = []

num = int(input("Ingrese la cantidad de elementos que va a tener el arreglo: "))
repeat_num = int(input("Ingrese la cantidad de veces que desea que se repitan los números: "))

for i in range(num):
    num = int(random.random()*5)
    array.append(num)

print(f"El array original es: {array}")

print(f"El array con los números repetidos es: {funciones.repeat_num_list(array, repeat_num)}")'''

#EJERCICIO 7
'''7. Implemente un algoritmo, usando una función recursiva, que resuelva la siguiente sumatoria:
K(n, p) = p + 2 * p + 3 * p + 4 * p + … + n * p
● El programa debe pedir al usuario que ingrese un número n, y un número d,
● Luego debe calcular el valor de K(n, p) usando una función recursiva,
● Debe imprimir el resultado de K(n, p)

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

print("La sumatoria es: ")
print(funciones.sum_recursiv(num1,num2))'''

#EJERCICIO 8
'''8. El triángulo de Pascal es un arreglo triangular de números que se define de la siguiente manera: Las
filas se enumeran desde n = 0, de arriba hacia abajo. Los valores de cada fila se enumeran desde k =
0 (de izquierda a derecha). Los valores que se encuentran en los bordes del triángulo son todos
unos. Cualquier otro valor se calcula sumando los dos valores contiguos de la fila de arriba. Escribí la
función recursiva pascal(n, k) que calcula el valor que se encuentra en la fila n y la columna k.

print("El valor es: ", funciones.calcular_valor_pascal(7,3))'''

#EJERCICIO 9
'''9. Escribí una función recursiva combinaciones(lista, k) que reciba una lista de caracteres únicos, y un
número k, e imprima todas las posibles cadenas de longitud k formadas con los caracteres dados
(permitiendo caracteres repetidos).

list_characters=["&","?","#","%","!"]
number = 3

print("Las combinaciones posibles son: ")
funciones.combinations(list_characters,number)'''

#EJERCICIO 10
'''La norma ISO 216 especifica tamaños de papel. Es el estándar que define el popular tamaño de
papel A4 (210 mm de ancho y 297 mm de largo). Las hojas A0 miden 841 mm de ancho y 1189 mm
de largo. A partir de la A0 las siguientes medidas, digamos la A(N+1), se definen doblando al medio
la hoja A(N). Siempre se miden en milímetros con números enteros: entonces la hoja A1 mide 594
mm de ancho (y no 594.5) por 841 mm de largo.

Escribí una función recursiva medidas_hoja_A(N) que para una entrada N mayor que cero, devuelva
el ancho y el largo de la hoja A(N) calculada recursivamente a partir de las medidas de la hoja
A(N-1), usando la hoja A0 como caso base. La función debe devolver el ancho y el largo -en ese
orden- en una tupla.

number = 1
while (True):
    number = int(input("Ingrese un numero mayor que 0: "))

    if (number>0):
        break
    
width, length = funciones.sheet_measurement(number)
print(f'Ancho de A{number}: {width} mm, Largo de A{number}: {length} mm')'''