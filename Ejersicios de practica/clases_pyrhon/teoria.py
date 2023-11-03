#MOTOCICLETA
'''from clases.Motocicleta import Motocicleta

motorcycle_one = Motocicleta("Azul", "AF 271 CZ", 10, 2, "Honda", "12/12/2012", 150, 500)
motorcycle_two = Motocicleta("Rojo", "AB 113 FA", 10, 2, "Yamaha", "02/01/2005", 180, 510)

motorcycle_one.__modelo = "Modelo 1"
motorcycle_two.__modelo = "Modelo 2"

print(f"El modelo de la moto 1 es: {motorcycle_one.__modelo}")
print(f"El modelo de la moto 2 es: {motorcycle_two.__modelo}")

motorcycle_one.start_engine()
motorcycle_one.start_engine()
motorcycle_one.off_engine()
motorcycle_one.off_engine()

motorcycle_one.price = 7500

print(f"El precio de la motocicleta {motorcycle_one.marca} y {motorcycle_one.__modelo} es de {motorcycle_one.price}$.")


print(f"El precio de la motocicleta {motorcycle_one.marca} y {motorcycle_one.__modelo} es de {motorcycle_one.consult_price()}$. (Como metodo)")

#Como price nunca fue añadido a moto 2, el medoto se rompe porque nunca fue declarado
#print(f"El precio de la motocicleta {motorcycle_two.marca} y {motorcycle_two.modelo} es de {motorcycle_two.consult_price()}$.")

motorcycle_one.mostrar_modelo()
motorcycle_two.mostrar_modelo() '''

#EJERCICIO 1
'''1. Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los
siguientes métodos para la clase:
• Un constructor, donde los datos pueden estar vacíos.
• Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
• mostrar(): Muestra los datos de la persona.
• esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

from clases.Persona import Persona

person_1 = Persona()

person_1.name = "Pablo Lima"
person_1.age = 21
person_1.dni = "43829992"


person_2 = Persona()

person_2.name = "Ignacio Molina"
person_2.age = 17
person_2.dni = "47334132"

#print(f"El nombre de la persona es {person_1.name}, la edad es {person_1.age} y el dni es {person_1.dni}")
person_1.mostrar_datos()

if(person_1.esMayorDeEdad()):
    print(f"{person_1.name} es mayor de edad")
else:
    print(f"{person_1.name} no es mayor de edad")

if(person_2.esMayorDeEdad()):
    print(f"{person_2.name} es mayor de edad")
else:
    print(f"{person_2.name} no es mayor de edad")'''

#EJERCICIO 2
'''2. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y
cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los
siguientes métodos para la clase:
• Un constructor, donde los datos pueden estar vacíos.
• Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
directamente, sólo ingresando o retirando dinero.
• mostrar(): Muestra los datos de la cuenta.
• ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa,
no se hará nada.
• retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

from clases.Cuenta import Cuenta

count_1 = Cuenta()

count_1.amount = int(input("Ingrese la cantidad de dinero en cuenta: "))
count_1.headline = "Pablo"

count_1.cambiar_atributo()

count_1.retirar_dinero(10)
count_1.ingresar_dinero(20)
count_1.mostrar_datos()'''

#EJERCICIO 3
'''3. Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los
métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y el tipo de
triángulo que es (equilátero, isósceles o escaleno).

from clases.Triangle import Triangle

triangle_1 = Triangle()

triangle_1.side_1 = int(input("Ingrese el lado 1: "))
triangle_1.side_2 = int(input("Ingrese el lado 2: "))
triangle_1.side_3 = int(input("Ingrese el lado 3: "))


triangle_1.show_dates()
triangle_1.what_triangle_is()'''

#EJERCICIO 4
'''4. Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el
teléfono y el email. Además deberá mostrar un menú con las siguientes opciones:

• Añadir contacto
• Lista de contactos
• Buscar contacto
• Editar contacto
• Cerrar agenda'''

from clases.Diary import Diary
from clases.Contact import Contact

id_diary = int(input("Ingrese el id del diario: "))

diary_one = Diary(id_diary)

contact_one = Contact("Pablo Lima", "mail1@gmail.com")
contact_one.number = 6524414

contact_two = Contact("Andres Vercich", "mail2@gmail.com")
contact_two.number = 3214401

diary_one.new_contact(contact_one)
diary_one.new_contact(contact_two)

diary_one.show_contacts()

diary_one.find_contac_with_name("Pablo Lima")

diary_one.modify_contact(contact_one)

diary_one.show_contacts()