'''Realizar un programa que cumpla con las siguientes condiciones:

Pedir al usuario su nombre. Cada vez que el programa interactúe con él debe llamarlo por su nombre.
Generar un menú de opciones, que serán:
Juego de números.
Juego de palabras.
Si el usuario elige la primera opción, se debe pedir el ingreso de números enteros (condición de salida: cuando ingrese 0). Al finalizar mostrar por pantalla:
El mayor número par.
El promedio de los números impares.
Si el usuario elige la segunda opción, se debe pedir el ingreso de una frase y mostrar por pantalla la cantidad de cada vocal que contiene dicha frase.
No olvides realizar las debidas validaciones!'''


name = input("Por favor ingrese su nombre: ").title()
print("MENÚ DE OPCIONES \n"
      "1. Juego de números \n"
      "2. Juego de palabras \n"
      "3. Salir")

option = int(input(f"Por favor {name} ingrese una opción: "))

while(option != 3):
    if(option == 1):

        number = int(input(f"Por favor {name} ingrese números enteros positivos ó 0 para terminar de ingresar números: "))
        max_add_number = 0
        average_odd_number = 0
        counter = 0

        while(number < 0):
             number = int(input(f"Por favor {name} ingrese números enteros positivos ó 0 para terminar de ingresar números: "))

        while(number != 0):

            if(number < 0):
                number = int(input(f"{name} el número ingresado no es positivo ingrese otro número entero ó 0 para terminar de ingresar números: "))
                continue
        
            elif(number % 2 == 0):
                if(number > max_add_number):
                    max_add_number = number
            elif(number % 2 == 1):
                counter += 1
                average_odd_number += number

            number = int(input(f"Por favor {name} otro número entero ó 0 para terminar de ingresar números: "))
        
        if(max_add_number == 0 and counter != 0):
            print("------------------------ \n"
                "No se ingresaron números par enteros positivos \n"
                f"El promedio de los números impares positivos fue {average_odd_number/counter}")
        elif(max_add_number == 0):
             print("------------------------ \n"
                "No se ingresaron números par enteros positivos \n"
                "No se ingresaron números impar enteros positivos")
        elif(counter == 0):
             print("------------------------ \n"
                f"El mayor número par positivo fue {max_add_number} \n"
                "No se ingresaron números impar enteros positivos")            
        else:
            print("------------------------ \n"
                    f"El mayor número par positivo fue {max_add_number} \n"
                    f"El promedio de los números impares positivos fue {average_odd_number/counter}")
    elif(option == 2):
        phrase = (input(f"Por favor {name} ingrese una frase: ").strip()).upper()
        counter_a = 0
        counter_e = 0
        counter_i = 0
        counter_o = 0
        counter_u = 0

        for i in range(len(phrase)):
            if(phrase[i] == "A"):
                counter_a += 1
            elif(phrase[i] == "E"):
                counter_e += 1
            elif(phrase[i] == "I"):
                counter_i += 1
            elif(phrase[i] == "O"):
                counter_o += 1
            elif(phrase[i] == "U"):
                counter_u += 1

        print("------------------------ \n"
              "La frase: \n"
              f"'{phrase.title()}' tiene \n"
              f"{counter_a} vocal/es A \n"
              f"{counter_e} vocal/es E \n"
              f"{counter_i} vocal/es I \n"
              f"{counter_o} vocal/es O \n"
              f"{counter_u} vocal/es U \n")
    else:
        print(f"{name} usted ha ingresado una opción incorrecta")

    print("------------------------ \n"
      "MENÚ DE OPCIONES \n"
      "1. Juego de números \n"
      "2. Juego de palabras \n"
      "3. Salir")
    option = int(input(f"Por favor {name} ingrese otra opción: "))


print(f"Bueno {name} usted ha desidido salir del menú del parcial 1 de programación, que tenga mucha suerte")