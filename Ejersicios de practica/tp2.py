import string

#EJERCICIO 1
'''1.Crear un programa que reciba el número de años que tiene nuestra computadora y muestre en la
consola que el computador es nuevo si es menor o igual a 2 años y que el computador es viejo si es mayor a 
2 años.

num_vigencia = int(input("Ingrese el numero de años de la computadora: "))
if num_vigencia<=2:
    print("Es nuevo")
else:
    print("Es viejo")'''

#EJERCICIO 2
'''2.Hacer que el programa anterior muestre un mensaje de error si el usuario digita un 
número negativo.

num_vigencia=int(input("Ingrese el numero de años de la computadora: "))
if num_vigencia<0:
    print("Error, no se puede ingresar un numero negativo")
elif num_vigencia<=2:
    print("Es nuevo")
else:
    print("Es viejo")'''

#EJERCICIO 3
'''3.Solicitar al usuario que ingrese los nombres de dos personas, 
los cuales se almacenarán en dos variables. A continuación. Imprimir "coincidencia" si ambos 
nombres comienzan con la misma letra. Si no es así, imprimir "no hay coincidencia".

nombre_1=input("Ingrese el primer nombre: ").upper()
nombre_2=input("Ingrese el segundo nombre: ").upper()
if nombre_1[0]==nombre_2[0]:
    print("Coincidencia")
else:
    print("No hay coincidencia")'''

#EJERCICIO 4 
'''4.Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: 
candidato A por el partido rojo, candidato B por el partido verdad, candidato C por el partido azul.

candidato_A="Partido Rojo"
candidato_B="Partido verdad"
candidato_C="Partido azul"

voto=input("A que candidato quiere votar? A,B O C: ").upper()

if voto=="A":
    print("Usted a votado por el ",candidato_A)
elif voto=="B":
    print("Usted a votado por el ",candidato_B)
elif voto=="C":
    print("Usted a votado por el ",candidato_C)
else:
    print("Opcion Erronea")'''

#EJERCICIO 5
'''5.Escribir un programa que solicite al usuario una letra, si es una vocal, mostrar el mensaje "Es vocal".
Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, 
informarle que no se puede procesar el dato.

vocal_ingresada = input("Ingresa una letra: ").upper()
numero_vocal = len(vocal_ingresada)

if numero_vocal < 2 and numero_vocal != 0 :
    
    if vocal_ingresada == "A" or vocal_ingresada == "E" or vocal_ingresada == "I" or vocal_ingresada == "O" or vocal_ingresada == "U":
        print("Ingresaste una vocal")
    else:
        print("No es una vocal")
else:
    print("Ingresaste mas de un caracter")'''
    
#EJERCICIO 6
'''6.Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible 
por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.

anio = int(input("Ingresa un año para saber si es biciesto o no: "))

if anio%4 == 0 or (anio%100 == 0 and anio%400 == 0 and anio%4 ==0):
    print("El año es bisiesto")
else: 
    print("El año no es biciesto")'''
    
#EJERCICIO 7
'''7.Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres.
num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))
num3 = int(input("Ingresa el tercero número entero: "))

if num1 > num2 and num1>num3:
    print(f"El número mas grande es el: {num1}")
elif num2>num3 and num2>num1:
    print(f"El número mas grande es el: {num2}")
elif num3>num2 and num3>num1:
    print(f"El número mas grande es el: {num3}")'''

#8 EJERCICIO 8 
'''8.Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. 
Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla “Usuario y contraseña correctos. 
Puede ingresar a Camelot”. Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”.

usuario = input("Ingrese el nombre de usuario: ").upper()
contra = input("Ingrese la contraseña de usuario: ").upper()
if usuario == "GWENEVERE" and contra == "EXCALIBUR":
    print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
    print("Acceso denegado")'''

#EJERCICIO 9
'''9.Los alumnos de un curso se han dividido en dos grupos A y B 
de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un nombre anterior 
a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que 
pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre = input("Ingrese nombre de la persona: ")
genero = input("Ingrese el genero de la persona [Masculino/Femenino]: ")

genero = genero[0].lower()
nombre = nombre[0].lower()

if((string.ascii_lowercase.index(nombre) < string.ascii_lowercase.index("m") and genero == "f") or
   (string.ascii_lowercase.index(nombre) > string.ascii_lowercase.index("n") and genero == "m")):
    print("Pertenece al grupo A")
elif((string.ascii_lowercase.index(nombre) >= string.ascii_lowercase.index("m") and genero == "f") or
   (string.ascii_lowercase.index(nombre) <= string.ascii_lowercase.index("n") and genero == "m")):
    print("Pertenece al grupo B")
else:
    print("Error en el programa")'''

#EJERCICIO 10
'''10.Escribir un programa para una empresa que tiene salas de juegos para todas las edades 
y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa 
debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años
puede entrar gratis, si tiene entre 4 y 18 años debe pagar $500 y si es mayor de 18 años, $1000.

edad = int(input("Ingrese la edad del cliente: "))

if(edad < 4):
    print("La entrada es gratis")
elif(edad >= 4 and edad <= 18):
    print("La entrada cuesta $500")
else:
    print("La entrada cuesta $1000")'''

#EJERCICIO 11
'''11.La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes 
para cada tipo de pizza aparecen a continuación.

•	Ingredientes vegetarianos: Pimiento y tofu.
•	Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta 
le muestre un menú con los ingredientes disponibles para que elija. Solo se puede elegir un ingrediente además de la 
mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es 
vegetariana o no y todos los ingredientes que lleva.


pizza = input("¿Desea una pizza vegetariana? [Si/No]: ")[0].lower()

if(pizza == "s"):
    ingrediente = input("Los ingredientes que se le puede añadir a la pizza vegetariana son [Pimiento/Tofu] elija uno: ")[0].lower()

    if(ingrediente == "p"):
        print("La pizza es vegetariana y sus ingredientes son: mozzarella-tomate-pimiento")
    elif(ingrediente == "t"):
        print("La pizza es vegetariana y sus ingredientes son: mozzarella-tomate-tofu")
    else:
        print("Error de programa")

elif(pizza == "n"):
    ingrediente = input("Los ingredientes que se le puede añadir a la pizza no vegetariana son [Peperoni/Jamón/Salmón] elija uno: ")[0].lower()

    if(ingrediente == "p"):
        print("La pizza no es vegetariana y sus ingredientes son: mozzarella-tomate-peperoni")
    elif(ingrediente == "t"):
        print("La pizza no es vegetariana y sus ingredientes son: mozzarella-tomate-tomate")
    elif(ingrediente == "s"):
        print("La pizza no es vegetariana y sus ingredientes son: mozzarella-tomate-salmón")
    else:
        print("Error de programa")
else:
    print("Error de programa")'''

#EJERCICIO 12
'''12.Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos 
    años han pasado desde ese año o cuántos años faltan para llegar a ese año.

anio_actual = int(input("Ingrese el año actual: "))
anio_cualquiera = int(input("Ingrese el año que desee: "))

if(anio_actual - anio_cualquiera > 0):
    print(f"La cantidad de años que le faltan para llegar al actual es: {anio_actual - anio_cualquiera}")

elif(anio_actual - anio_cualquiera < 0):
    print(f"La cantidad de años que pasaron son {-(anio_actual - anio_cualquiera)}")
else:
    print("El año actual y el desado son el mismo")'''

#EJERCICIO 13
'''Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor. 
Haciendo que el programa avise cuando se escriben valores negativos o nulos.

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 <= 0 or num2<= 0:
    print("Los numeros ingresados son nulos o negativos")
elif num2 > num1:
    aux = num1
    num1 = num2
    num2 = aux
if num1%num2==0:
    print("El numero mayor es multiplo del menor")
else:
    print("El numero mayor no es multiplo del menor")'''

#EJERCICIO 14
'''Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba la solución.
Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos los 
números sean solución. Se recuerda que la fórmula de las soluciones es: x = -b / a

print("Coeficientes de primer grado, formula: a x + b = 0")
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
x = (-b / a)
print(f"El valor de es: {x}")'''

#EJERCICIO 15
'''15.Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o 
la de un círculo. Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), 
el programa tiene que pedir entonces la base y la altura y escribir el área. 
Si se contesta que se quiere calcular el área de un círculo (escribiendo C o c),
el programa tiene que pedir entonces el radio y escribir el área.

area = input("Ingrese si quiere calcular el area de un triangulo[t] o de un circulo[c]: ")
area = area.lower()
if area == "t":
    base = int(input("Ingrese la base de su triangulo: "))
    altura = int(input("Ingrese la altura de su triangulo: "))
    area = (base * altura)/ 2
    print(f"El area de un triangulo es: {area}")
elif area == "c":
    radio = int(input("Ingrese el radio del circulo: "))
    area = ((radio**2) * 3.14)
    print(f"El area de el circulo es: {area}")
else:
    print("Ingrese valores validos")'''

#EJERCICIO 16
'''16.Haz una calculadora básica pida al usuario dos valores, a y b.
Según la opción que desean, realizar la operación:
•	Si operación es 1 entonces debemos ver el resultado de a + b
•	Si operación es 2 entonces debemos ver el resultado de a * b
•	Si operación es 3 entonces debemos ver el resultado de a - b
•	Si operación es 4 entonces debemos ver el resultado de a / b

a = int(input("Ingrese el primer valor: "))
b = int(input("Ingrese el segundo valor: "))
operacion = int(input("Ingrese la operacion que desea realizar: "))
if operacion == 1:
    operacion = a + b
    print(f"El resultado de su operacion es: {operacion}")
elif operacion == 2:
    operacion = a * b
    print(f"El resultado de su operacion es: {operacion}")
elif operacion == 3:
    operacion = a - b
    print(f"El resultado de su operacion es: {operacion}")
elif operacion == 4:
    operacion = a / b
    print(f"El resultado de su operacion es: {operacion}")
else :
    print("Ingrese un valor correcto")'''

#EJERCICIO 17
'''17.Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, 
otro mensaje diferente si es viernes, otro mensaje diferente si es sábado
o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje.

diaSemana = input("Ingresar un dia de la semana: ")
diaSemana=diaSemana.lower()

if(diaSemana == "lunes"):
    print("El dia ingresado es lunes. ")
elif(diaSemana == "viernes"): 
    print("El dia ingresado es viernes. ")
elif(diaSemana == "sabado" or diaSemana == "domingo"): 
    print("El dia ingresado es sabado o domingo. ")
else: 
    print("Usted no ha ingresado ni Lunes, ni viernes, ni sabadado ni domingo. ")'''

#EJERCICIO 18
'''18.Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora.
La jornada de trabajo mínima es de 48 horas. 
Calcular, dadas las horas trabajadas, si trabajó horas extras y mostrar esta cantidad.
Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas un 10% más
 que las horas laborales comunes.

horasTrabajadas = float(input("Ingresar la cantidad de horas trabajadas en el mes: "))
salarioHoras = float(input("Ingresar cuanto es el salario x horas: "))

if(horasTrabajadas > 48 ):
    horasExtras = (horasTrabajadas-48)
    print(f"Usted realizo {horasExtras} horas extras. ")
    salarioExtra = (horasTrabajadas*salarioHoras)*10/100
    salarioTotal = (horasTrabajadas*salarioHoras) + salarioExtra
    print("Su salario total es de: $",salarioTotal)
else: 
    salarioTotal = horasTrabajadas*salarioHoras
    print(f"Usted ha realizado {horasTrabajadas}hs. Y su salario total es de: ${salarioTotal}")'''

#EJERCICIO 19
'''19.Determinar cuánto se debe pagar por una cantidad de lápices considerando que si son 1000 o más, existe un
descuento de 7% y teniendo en cuenta que el costo por lápiz es de $60; de lo contrario no hay descuento.

precioLapiz = 60
lapices = int(input("Ingresar la cantidad de lapices: "))

if(lapices >= 1000):
        print(f"Por la cantidad que lleva tine un 7% de descuento")
        descuento = (lapices*60)*7/100
        precioFinal = (lapices*60)-descuento
        print("Lo cual su total es de: $",precioFinal)
else:
        precioFinal = (lapices*60)
        print("El precio total es de: ",precioFinal)'''

#EJERCICIO 20        
'''20.Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara 
si su promedio de cuatro (4) notas, es mayor o igual a 6; caso contrario saldrá desaprobado.

notaUno = float(input("Ingrese su primera nota: "))
notaDos = float(input("Ingrese su segunda nota: "))
notaTres = float(input("Ingrese su tercera nota: "))
notaCuatro = float(input("Ingrese su cuarta nota: "))

promedio = (notaUno + notaDos + notaTres + notaCuatro)/4

print("Su promedio es de: ",promedio)
if(promedio >= 6):
    print("APROBADO. ")
else: 
    print("DESAPROBADO. ")'''


