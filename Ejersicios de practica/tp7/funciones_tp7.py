#EJERCICIO 1
def bubble_sort(array):
    i = 0
    j = 0
    aux = 0

    for i in range (len(array)-1):
        for j in range(len(array) - i - 1):
            if(array[j+1] < array[j]):
                aux = array[j + 1]
                array[j + 1] = array[j]
                array[j] = aux

    return array

#EJERCICIO 2
def selection_sort(array):
    i = 0
    j = 0
    menor = 0
    pos = 0
    tmp = 0

    for i in range (len(array)-1):
        menor = array[i]
        pos = i

        for j in range((i+1), len(array)):
            if(array[j] < menor):
                menor = array[j]
                pos = j

        if(pos != i):
            tmp = array[i]
            array[i] = array[pos]
            array[pos] = tmp
    
    return array

#INSERST
def insert_sort(array):
    p = 0
    j = 0
    aux = 0

    for p in range(1, len(array)):
        aux = array[p]
        j = p - 1

        while((j >= 0) and (aux < array[j])):
            array[j + 1] = array[j];  
            j -= 1
        
        array[j + 1] = aux
    
    return array

#MERGE SORT
def merge_sort(array, izq, der):
    if izq < der:
        m = (izq + der) // 2  # Use '//' for integer division
        merge_sort(array, izq, m)
        merge_sort(array, m + 1, der)                                                                              
        merge(array, izq, m, der)
    return array

def merge(array, izq, m, der):
    arrayAux = []
    for i in range(izq, der + 1):
        arrayAux.append(array[i])

    i = izq 
    j = m + 1 
    k = izq

    while i <= m and j <= der:                                    
        if arrayAux[i - izq] <= arrayAux[j - izq]:
            array[k] = arrayAux[i - izq]
            i += 1
        else:
            array[k] = arrayAux[j - izq]
            j += 1
        k += 1

    while i <= m:
        array[k] = arrayAux[i - izq]
        i += 1
        k += 1

    while j <= der:
        array[k] = arrayAux[j - izq]
        j += 1
        k += 1

#BUSQUEDA LINEAL
def linear_search(array, searched_number):

    for i in range(len(array)):
        if array[i] == searched_number:  
            return f"El número {searched_number} se encuentra en el array en la posición {i+1}"
        
    return f"El número {searched_number} no se encuentra en el array" 

#BUSQUEDA BINARIA
def binary_search(array, searched_number):
    izq = 0 
    der = len(array) -1

    while izq <= der:
        medio = (izq+der) // 2

        if array[medio] == searched_number:
            return f"El número {searched_number} se encuentra en el array"

        elif array[medio] > searched_number:
            der = medio-1

        else:
            izq = medio+1

    return f"El número {searched_number} no se encuentra en el array"

#EJERCICIO 4
def bubble_sort_len(array):
    i = 0
    j = 0
    aux = 0

    for i in range (len(array)-1):
        for j in range(len(array) - i - 1):
            if(len(array[j+1]) < len(array[j])):
                aux = array[j + 1]
                array[j + 1] = array[j]
                array[j] = aux

    return array

#EJERCICIO 5
def bubble_sort_reverse(array):
    i = 0
    j = 0
    aux = 0

    for i in range (len(array)-1):
        for j in range(len(array) - i - 1):
            if(array[j+1] > array[j]):
                aux = array[j + 1]
                array[j + 1] = array[j]
                array[j] = aux

    return array

#EJERCICIO 6
def counting_sort(array):
    min_value = min(array)
    max_value = max(array)

    count_array = [0] * (max_value - min_value + 1)

    for num in array:
        count_array[num - min_value] += 1

    sorted_array = []
    for i, count in enumerate(count_array):
        sorted_array.extend([i + min_value] * count)

    return sorted_array

#EJERCICIO 7
def order_list(array):
    list_number = []
    list_str = []
    ordered_list = []

    for i in array:

        #isinstance sirve para saber si la variable es igual a la clase deseada
        if isinstance(i, int):
            list_number.append(i)

        elif isinstance(i, str):
            list_str.append(i)

    list_str.sort()
    list_number = bubble_sort(list_number)

    for i in list_number:
        ordered_list.append(i)

    for i in list_str:
        ordered_list.append(i)

    return ordered_list