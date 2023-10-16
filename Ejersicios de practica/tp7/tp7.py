import random
import funciones_tp7
array = []

for i in range(10):
    num = int(random.random()*100)
    array.append(num)


#print(f"El array original es: \n{array}\n")

#EJERCICIO 1
'''1. Escribe un programa que tome una lista de números como entrada y la ordene en orden
ascendente utilizando el método de ordenamiento de burbuja.

print(f"El array con metodo burbuja es: \n{funciones_tp7.bubble_sort(array)} \n")'''

#EJERCICIO 2
'''2. Crea un programa que tome una lista de palabras como entrada y las ordene alfabéticamente en
orden ascendente utilizando el método de ordenamiento de selección.

print(f"El array con metodo seleccion es: \n{funciones_tp7.selection_sort(array)} \n")'''

#INSERT
'''print(f"El array con metodo inersión es: \n{funciones_tp7.insert_sort(array)} \n")'''

#MERGE SORT
'''print(f"El array con metodo merge sort es: \n{funciones_tp7.merge_sort(array, 0, len(array) - 1)} \n")'''

#BUSQUEDA LINEAL
'''num = int(input("Ingrese un número a buscar: "))
print(funciones_tp7.linear_search(array, num))'''

#BUSQUEDA BINARIA
'''ordered_array = funciones_tp7.bubble_sort(array)

num = int(input("Ingrese un número a buscar: "))
print(funciones_tp7.binary_search(ordered_array, num))'''

#EJERCICIO 3
'''3. Crea una lista de diccionarios, donde cada diccionario contiene información sobre un libro (título,
autor, año de publicación, etc.). Luego, escribe un programa que ordene la lista de libros en función
de un campo específico, como el año de publicación o el autor.

list_of_books = []

out = True
while(out == True):
    answer = input("Ingrese True si desea ingresar un usuario o False si desea salir: ")

    if answer == 'True':
            out = True
    elif answer == 'False':
            out = False
    else:
            print("Entrada no válida. Por favor, ingrese 'True' o 'False'.")
            continue
    
    if(out == False):
        break

    book = {}

    key = int(input("Ingrese el año de publicacion: "))
    title = input("Ingrese el titulo del libro: ")
    autor = input("Ingrese el nombre del autor: ")
    book_genre = input("Ingrese el genero del libro: ")

    info_book = {
        "Title": title,
        "Autor": autor,
        "Genero": book_genre
    }

    book[key] = info_book
    list_of_books.append(book)


ordered_list_of_books = sorted(list_of_books, key=lambda x: list(x.keys())[0])
#1. Usando x.keys(), obtenemos todas las claves del diccionario x (esto devuelve una vista de las claves).
#2. Con list(...), convertimos esa vista a una lista.
#3. Con [0], tomamos la primera (y en este caso, única) clave.

print("Los libros ordenados segun el año: ")
for i in ordered_list_of_books:
      print(f"{i}")'''

#EJERCICIO 4
'''4. Escribe un programa que tome una lista de cadenas como entrada y las ordene en orden
ascendente según su longitud. Puedes utilizar el método de ordenamiento de inserción.

string_list = [
    "Explorando el universo del aprendizaje automático.",
    "La tecnología avanza a pasos agigantados.",
    "Inteligencia artificial: un futuro cercano y un posible presente.",
    "La biodiversidad es esencial para la vida.",
    "Cada amanecer trae nuevas oportunidades.",
    "Misterios del cosmos.",
    "Los océanos albergan secretos profundos.",
    "El cambio climático afecta la vida en la Tierra de los hombres.",
    "La música tiene el poder de conectar almas.",
    "Viajar.",
    "El arte de la programación es sutil.",
    "Nuevos horizontes en la medicina moderna.",
    "El mundo digital transforma la sociedad.",
    "La literatura es el espejo del alma.",
    "Medio narrativo.",
    "Desarrollando soluciones.",
    "La revolución de las energías limpias y renovables.",
    "El reino animal está lleno animales.",
    "La cultura gastronómica.",
    "La historia de la humanidad es fascinante."
]

print("\nEl array desordenado es: ")
for i in string_list:
    print(i)

ordered_string_list = funciones_tp7.bubble_sort_len(string_list
                                                    )
print("\nEl array ordenado es: ")
for i in ordered_string_list:
    print(i)'''

#EJERCICIO 5
'''5. Modifica uno de los ejercicios anteriores para ordenar la lista de números en orden descendente en
lugar de ascendente.

print(f"El array con metodo burbuja descendente es: \n{funciones_tp7.bubble_sort_reverse(array)} \n")'''

#EJERCICIO 6
'''6. Escribe un programa que tome una lista de números enteros y ordene la lista utilizando el algoritmo
de ordenamiento por conteo

print(f"El array con metodo de conteto es: \n{funciones_tp7.counting_sort(array)} \n")'''

#EJERCICIO 7
'''7. Crea una lista que contenga tanto números como cadenas de caracteres. Escribe un programa que
ordene esta lista de manera que primero estén los números ordenados de menor a mayor y luego
las cadenas de caracteres ordenadas alfabéticamente.

list = [
    20,
    "arroz",
    90,
    43, 
    "auto", 
    "casa",
    4,
    "libro", 
    55,
    "agua",
    76,
    "cielo", 
    "flor",
    98,
    1,
    17, 
    "gato", 
    21,
    "perro", 
    "luz",
    32,
    "fruta", 
    "silla",
    44, 
    "zapato",
    18, 
    "puerta",
    21,
    29,
    11, 
    "ventana",
    "hoja",
    8, 
    "papel", 
    "tijera",
    92, 
    "pluma", 
    "sombrero"
]

ordered_list = funciones_tp7.order_list(list)

print(f"\nLa lista ordenada es: ")
for i in ordered_list:
    print(i)'''

#EJERCICIO 8
'''8. Implementa el algoritmo de ordenamiento Merge Sort y úsalo para ordenar una lista de números.

print(f"El array con metodo merge sort es: \n{funciones_tp7.merge_sort(array, 0, len(array) - 1)} \n")'''