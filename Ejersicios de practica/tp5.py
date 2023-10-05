'''Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos.

Al finalizar mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos.

import tp5_sumatoria

number = int(input("Ingrese un número para saber la sumatoria de sus digitos o cero para salir: "))
counter = 0
counter_digits = 0
while(number != 0):
    tp5_sumatoria.summation(number)

    print(f"La sumatoria de los digitos es {tp5_sumatoria.summation(number)}")
    counter += number
    counter_digits += tp5_sumatoria.summation(number)

    number = int(input("Ingrese otro número para saber la sumatoria de sus digitos o cero para salir: "))

print(f"La suma de todos los números ingresados es: {counter} \n"
      f"La sumatoria de los digitos de la suma de todos los números ingresados es {tp5_sumatoria.summation(counter)} \n"
      f"La sumatoria de los digitos de los números ingresados es {counter_digits} \n")'''


'''1. El siguiente programa debería imprimir el número 2 si se le ingresan como valores x=5,
y=1 pero en su lugar imprime 5. ¿Qué hay que corregir?

#DEFINICION DE FUNCIONES
def most(a,b): 
    #if(x > y):
    #    return x
    #else:
    #    return y
    #Deberia ser:
    if(a > b):
        return a
    else:
        return b
    
def least(a,b): 
    #if(x < y):
    #    return x
    #else:
    #    return y
    #Deberia ser:
    if(a < b):
        return a
    else:
        return b
    
#PROGRAMA PRINCIPAL
x = int(input("Un número: "))

y = int(input("Otro número: "))

#print(most(x-3, least(x+2,y-5)))

#Deberia ser:
print(most(x-4, least(x+2,y-5)))'''