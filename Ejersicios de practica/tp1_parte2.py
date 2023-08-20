import math

#EJERCICIO 1
'''Calcular el perímetro y área de un rectángulo dada su base y su altura.

base = float(input("Ingrese el valor de la base del rectángulo: "))
altura = int(input("Ingrese el valor de la altura: "))

perimetro_rectangulo = (base * 2) + (altura * 2)
area_rectangulo = base * altura

print(
    f"El area del rectángulo es: {area_rectangulo}. \nEl perímetro del rectángulo es: {perimetro_rectangulo}"
)'''

#EJERCICIO 2
'''2. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

cateto1 = float(input("Ingrese el valor del primer cateto: "))
cateto2 = float(input("Ingrese el valor del segundo cateto: "))

hipotenusa = ((cateto1) ** 2 + (cateto2) ** 2) ** (1/2)

print(f"La hipotenusa del triangulo es: {hipotenusa}")'''

#EJERCICIO 3
'''Dados dos números, mostrar la suma, resta, división y multiplicación de
ambos.

num1 = float(input("Ingrese el valor del primer número: "))
num2 = float(input("Ingrese el valor del segundo número: "))


print(f"La suma de {num1} y {num2} es igual a: {num1 + num2}  \n"
    f"La resta de {num1} y {num2} es igual a: {num1 - num2} \n"
    f"La multiplicación de {num1} y {num2} es igual a: {num1 * num2} \n"
    f"La división de {num1} y {num2} es igual a: {num1 / num2}")'''


#Ejercicio 4 
'''4. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.

F=float(input("Ingrese los grados Fahrenheit: "))
C=(F-32)*(5/9)
print("El valor en grados celsius es: ",C)'''

#Ejercicio 5 
'''5. ¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?

a) A = input(nombre, “¿Cuál es tu canción favorita?”)
a)Tiene un error al colocar la variable “nombre”(en caso de que la variable nombre tenga un valor,se debe 
concatenar con un +), y al poner una mayúscula como nombre de la variable es mala práctica.
Solucion: A = input(nombre +"¿Cuál es tu canción favorita?")

b) precio = input(“Precio: “)
b) Tiene que transformar la entrada de datos a float, si no sería un string
Solución: precio = float(input("Precio: "))

c) edad = int(input(“Edad: “))
    print(tu edad es, edad)
c)No coloco “  ” al mostrar por pantalla
Solución: print("tu edad es", edad)

d) edad = int(input(“Edad: “))
    print(“Veamos si tu edad es 18…”, edad=18)
d) Error al mostrar por pantalla la edad del usuario
Solución: print("Veamos si tu edad es 18…", edad)'''

#EJERCICIO 6 
'''6. Calcular la media de tres números pedidos por teclado.

print("Este programa sirve para calcular la media de 3 números")
num1 = float(input("Ingresa el primer número: ")) 
num2= float(input("Ingresa el segundo número: ")) 
num3= float(input("Ingresa el tercer número:"))

print("La media de los 3 números es de: ", (num1 + num2 + num3)/3)'''

#EJERCICIO 7
'''7. Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a 
cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

print("Este programa sirve para calcular la cantidad de horas y minutos corresponden a la cantidad de minutos ingresados")

minutos_ingresados = int(input("Ingrese la cantidad de minutos que desea calcular: "))

horas_calculadas = int(minutos_ingresados/60)
minutos_caclulados = int(minutos_ingresados%60)

print(f"La cantidad de minutos ingresados es hora: {horas_calculadas} minutos {minutos_caclulados}")'''

#EJERCICIO 8
'''8. Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, 
el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que 
realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

sueldo_base = int(input("Ingrese el del sueldo base "))
venta1 = int(input("Ingrese el valor del producto vendido: "))
venta2 = int(input("Ingrese el valor del producto vendido: "))
venta3 = int(input("Ingrese el valor del producto vendido: "))

ventas_totales = (venta1*0.1)+(venta2*0.1)+(venta3*0.1)

ganancia_total = sueldo_base + ventas_totales

print("El total que cobrara el empleado es: ",ganancia_total)'''

#EJERCICIO 9: 
'''9. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar 
finalmente por su compra.

compra = float(input("Ingrese el valor de la compra: "))
descuento = compra * 0.15 

print(f"El valor total a pagar aplicando el descuento del 15 porciento es de: {compra - descuento}")'''

#EJERCICIO 10
'''10. Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone 
de los siguientes porcentajes:

·     55% del promedio de sus tres calificaciones parciales.
·     30% de la calificación del examen final.
·     15% de la calificación de un trabajo final.

parcial1 = int(input("Ingrese la nota del primer parcial: "))
parcial2 = int(input("Ingrese la nota del segundo parcial: "))
parcial3 = int(input("Ingrese la nota del tercer parcial: "))

parcial_total = ((parcial1 + parcial2 + parcial3) / 3)

parcial_total *= 0.55

examen_final = int(input("Ingrese la nota del examen final: "))
examen_final *= 0.30

trabajo_final = int(input("Ingrese la nota del trabajo final: "))
trabajo_final *= 0.15

calificacion_final = (parcial_total + trabajo_final + examen_final)

print(f"La nota final es: {calificacion_final}")'''

#EJERCICIO 11
'''11. Pide al usuario dos números y muestra la “distancia” entre ellos 
(el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

distancia = abs(numero1 - numero2)

print(f"la distancia entre ellos es: {distancia}")'''

#EJERCICIO 12
'''12. Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica.

numero = int(input("Ingrese un numero para calcular su raiz cuadrada y cubica: "))

numero_cuadrada = numero ** (1/2)
numero_cubica = numero ** (1/3)

print(f"La raiz cuadrada de {numero} es: {numero_cuadrada}\nla raiz cubica de {numero} es: {numero_cubica}")'''

#EJERCICIO 13
'''Dado un número de cifras, diseñe un algoritmo que permita obtener el número invertido. 
Ejemplo, si se introduce 23 que muestre 32

num1 = input("Ingrese un número: ")

print(num1[::-1])'''

#EJERCICIO 14
'''Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que 
intercambie los valores de ambas variables y muestre cuánto valen al final las dos variables.

numA = float(input("Ingrese el primer número:"))
numB = float(input("Ingrese el primer número:"))

aux = numA
numA = numB
numB = aux

# print(f"El número A es {numA} y el número B {numB}")'''

#EJERCICIO 15
'''Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la 
hora de llegada a la ciudad B.

ciudadAHH = int(input("Ingrese la hora de salida: "))
ciudadAMM = int(input("Ingrese los minutos de salida: "))
ciudadASS = int(input("Ingrese los segundos de salida: "))

segundos_duracion = int(input("Ingrese cuantos segundos dura el viaje: "))

total_segundos = ciudadASS + segundos_duracion

ciudadBSS = total_segundos % 60 #Cantidad de segundos
ciudadBMM = (ciudadAMM + (total_segundos // 60)) % 60 #Parte entera de los (segundos / 60) mas los minutos residuo 60
ciudadBHH = (ciudadAHH + (ciudadAMM + (total_segundos // 60)) // 60) % 24 #Parte entera de los (minutos / 60) mas las horas residuo 24

print(f"La hora de llegada es {ciudadBHH:02d}h:{ciudadBMM:02d}m:{ciudadBSS:02d}s")'''

#EJERCICIO 16
'''16. Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

nombre = input ("Ingresar su nombre: ") 
apellido1 = input("Ingrese su primer apellido: ")
apellido2 = input("Ingresar su segundo apelldio: ") 

iniciales = print("La iniciales son: ",nombre[0]," ",apellido1[0]," ", apellido2[0])'''

#EJERCICIO 17
'''17.Solicitar al usuario que ingrese su nombre. El nombre se debe almacenar en una variable llamada usuario. 
A continuación mostrar por pantalla: “Ahora estás en la matrix, [nombre del usuario]”.

usuario = input ("Ingresar su nombre por favor: ") 
print(f"Ahora estas en la matrix, [{usuario}]")'''

#EJERCICIO 18
'''18.Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante. A ese valor, 
sumarle un 6.2% en concepto de servicio y un 10% de propina. Imprimir en pantalla el monto final a pagar.

precioCena =  float(input("Ingresar que monto le salio la cena: "))

precioFinal = precioCena+(precioCena*(10/100))+(precioCena*0.062)

print("En el monto final a pagar es de: ",precioFinal)'''

#EJERCICIO 19
'''19. Solicitar al usuario que ingrese el día, mes y año de su nacimiento y almacenar cada uno de ellos en una variable 
numérica (en total, tres variables diferentes). Finalmente, mostrar la fecha en formato dd/mm/aaaa.

dia = int(input("Ingrese el dia en que nacio: "))
mes = int(input("Ingrese el mes en que nacio: "))
anio = int(input("Ingrese el año en que nacio: "))

print(f"La persona nacio en {dia:02d}/{mes:02d}/{anio}")'''

# EJERCICIO 20
'''20. Hacer otra versión del programa, pero esta vez almacenado todo en una única variable con formato DDMMAAA.

dia = int(input("Ingrese el dia en que nacio: "))
mes = int(input("Ingrese el mes en que nacio: "))
anio = int(input("Ingrese el año en que nacio: "))

unica_variable = f"{dia:02d}/{mes:02d}/{anio}"

print(unica_variable)'''

#EJERCICIO 21
'''21. Una pareja de motociclistas necesita hacer ciertos cálculos antes de emprender un viaje en moto, 
para saber cuántos tanques de combustible consumirá el viaje entero. Para eso deben 
ingresar: cuántos kilómetros puede recorrer su moto con 1 litro de combustible, qué capacidad (en litros) tiene el 
tanque y cuántos kilómetros en total recorrerán.
Hacer un programa que solicite los datos necesarios y luego informe la cantidad de tanques de combustible necesarios

consumo = float(input("Ingrese la cantidad de km que recorre con un litro de combustible: "))
capacidad = float(input("Ingrese la cantidad de litros que posee el tanque de combustible: "))
kilometros = float(input("Ingrese la cantidad de kilometros que recorrera en el viaje: "))

cuantos = kilometros/(capacidad*consumo)
cuantos_tanques = round(cuantos,0)
print(f"DEBERÁ CARGAR ALREDEDOR DE {cuantos_tanques} VECES EL TANQUE")

un_tanque = capacidad*consumo
total_tanques = math.ceil(kilometros/un_tanque)

print(f"Debera cargar {total_tanques} veces el tanque")'''