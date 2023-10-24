import random

#EJERCICIO EN CLASE 1
def recursive_mouse(minutes_counter):

    option = random.randint(1, 3)

    if(option == 3):
        return minutes_counter+7

    elif(option == 1):
        return recursive_mouse(minutes_counter+5)
    
    elif(option == 2):
        return recursive_mouse(minutes_counter+3)
    
#EJERCICIO EN CLASE 2
def f(n):
    s = str(n)
    if (len(s) <= 1):
        return s
    return s[-1] + f(int(s[:-1]))

#EJERCICIO 1
def count_digits(n):
    if len(str(n)) == 1:
        return 1
    return 1+count_digits(n//10)

#EJERCICIO 2
def es_potencia(n, b):
    if (n == b) :
        return True
    elif (n < b):
        return False
    return es_potencia(n-b,b)

#EJERCICIO 3
def encontrar_posiciones(a, b):
    posiciones = []
    index = a.find(b)
    
    while index != -1:
        posiciones.append(index)
        index = a.find(b, index + 1)
    
    return posiciones

#EJERCICIO 4
def par(n):
    if n == 0:
        return True  
    else:
        return impar(n - 1)

def impar(n):
    if n == 0:
        return False  
    else:
        return par(n - 1)
    
#EJERCICIO 5
def max_list_num(array, i, max_num):
    if((len(array)-1) >= i):

        if(array[i] > max_num):
            max_num = array[i]
        
        return max_list_num(array, i+1, max_num)
    
    else:
        return max_num

#EJERCICIO 6
'''Si la lista esta vacia quiere decir que ya repetimos todos los nums, y lo que hacemos es ir agarrando el primer num
multiplicar la cantidad de veces que aparece y despues borrarlo. Pd repeated_elements es una lista'''
def repeat_num_list(array, num_repeats):
    if not array:
        return []

    current_element = array[0]
    repeated_elements = [current_element] * num_repeats

    return repeated_elements + repeat_num_list(array[1:], num_repeats)

#EJERCICIO 7
def sum_recursiv(n,p):
    if (n>1):
        return (p*n) + sum_recursiv(n-1,p)
    
    elif(n <=0):
        return"n no puede valer ni ser menor a 0"
    
    elif (n == 1): 
       return p
    
#EJERCICIO 8
def calcular_valor_pascal(fil, column):
    if column == 0 or column==fil:
        return 1
    else:
        return calcular_valor_pascal(fil - 1, column - 1) + calcular_valor_pascal(fil - 1, column)
        
#EJERCICIO 9
def combinations(char,n,built_chain=""):
    if (n==0):
        print(built_chain)
        return  
    
    else:
        for i in char:
            combinations(char,n-1,built_chain+i)

#EJERCICIO 10
def sheet_measurement(n):
    if (n==0):
        return(841,1189)
    previous_width, previous_length = sheet_measurement(n-1)
    if (n % 2 == 1):
        return (previous_length, previous_width // 2)
    else:
        return (previous_width // 2, previous_length)
    