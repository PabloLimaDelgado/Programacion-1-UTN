import random

#EJERCICIO 1
'''1. Realizar un programa que pida una frase o palabra y si la frase o palabra es de 4 caracteres de largo, el programa le sumará un signo de exclamación al final, y si no es de 4 caracteres el programa le sumará un signo de interrogación al final. El programa mostrará después la frase final.

phrase = input("Ingrese la frase: ").strip()

if(len(phrase) == 4):
    phrase += "!"
else:
    phrase += "?"


print(f"La frase es: {phrase}")'''

#EJERCICIO 2
'''2. Crea un juego donde el programa elija una palabra al azar de una lista y el usuario tenga que adivinarla letra por letra. Proporciona un número limitado de intentos y utiliza un bucle while para controlar el juego.

hanged = ["AUTO", "CAMION", "CIRCO", "FLAVIO", "NIÑO", "PAPAS", "CIRUJANO", "DINOSAUIRO", "ARGOLLA"]
chosen_word = hanged[random.randint(0, 8)]
number_of_errors = 5
aux_word = "*" * len(chosen_word)
chosen_word_aux = chosen_word

print(aux_word)
while(number_of_errors > 0):

    if(chosen_word == ""):
        print("Felicitaciones encontro la palabra")
        break

    new_word = ""
    tried = input("Ingrese una letra: ").upper()

    while(len(tried) != 1):
        tried = input("Incorrecto solo ingrese una letra: ").upper()

    if tried in chosen_word:
        for index, char in enumerate(chosen_word):
            if char != tried:
                new_word += char

        for index, char in enumerate(chosen_word_aux):
            if char == tried:
                aux_word = aux_word[:index] + char + aux_word[index + 1:]

        print(aux_word)
        chosen_word = new_word
    else:
        number_of_errors -= 1
        print(f"Intento incorrecto le quedan {number_of_errors} intentos")
        print(aux_word) 

if(number_of_errors == 0):
    print(f"Lo lamento ha perdido, la palabra correcta era {chosen_word_aux}") '''


#EJERCICIO 3
'''3. Escribe un programa que cuente cuántas palabras hay en una cadena de texto ingresada por el usuario. '''

counter = 1
prhase = input("Ingrese una cadena de texto: ").strip()

for i in range(len(prhase)):
    if(prhase[i] == " "):
        counter += 1

print(f"La cantidad de palabras de la frase es: {counter}")

#EJERCICIO 4
'''4. Una empresa quiere pagar a sus empleados por la asistencia de lunes a viernes y un adicional por las horas trabajadas los domingos en tareas especiales.  
✔ El empleado asistió todo el mes, además entre 3 y 5 horas los domingos, adiciona el 3 % del sueldo.  
✔ Si asistió todo el mes y entre 6 y 10 horas los domingos, adiciona el 10 %.  
✔ No asistió todo el mes y entre 3 y 10 horas los domingos, adiciona el 2 %.  '''