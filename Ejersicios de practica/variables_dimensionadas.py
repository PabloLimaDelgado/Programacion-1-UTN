#EJERCICIO 1
'''Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente
forma: (nombre, dni, destino). Por ejemplo:
*(‘Manuel Juarez’, 12345678, ‘San Juan’), (‘Silvana Paredes’, 62258472, ‘Mendoza’)+
Además en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo:
*(‘Buenos Aires’, ‘Argentina’), (‘Lisboa’, ‘Portugal’), (‘Mendoza’, ‘Argentina’)+

Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
- Agregar pasajeros a la lista de viajeros.
- Agregar ciudades a la lista de ciudades.
- Dado el DNI de un pasajero, ver a qué ciudad viaja.
- Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
- Dado el DNI de un pasajero, ver a qué país viaja.
- Dado un país, mostrar cuántos pasajeros viajan a ese país.
- Salir del programa.

list_passenger = []
list_destination = []

menu = True

def add_passenger():
    name = input("Ingrese un nombre: ")
    dni = int(input("Ingrese un DNI: "))
    destiny = input("Ingrese un destino: ")

    one_tuple = (name, dni, destiny)

    list_passenger.append(one_tuple)

def add_destiny():
    city = input("Ingrese una ciudad: ")
    country = input("Ingrse un pais: ")

    one_tuple = (city, country)

    list_destination.append(one_tuple)

def find_city(dni_selected):
    for name, dni, destiny in list_passenger:
        if(dni_selected == dni):
            print(f"El pasajero con nombre {name} y dni {dni} viaja a {destiny}")
        else:
            print(f"Pasajero no encontrado")

def find_cant_pasenger(city_selected):
    counter = 0
    for name, dni, destiny in list_passenger:
        if(city_selected == destiny):
            print("Entre")
            counter += 1
    print(f"La cantidad de pasajeros que viajan a la ciudad de {city_selected} es {counter}")

def cant_country(country_selected):
    counter = 0
    for city, country in list_destination:
        if(country_selected == country):
            destiny_aux = city
            for name, dni, destiny_aux in list_passenger:
                counter += 1

    print(f"La cantidad de pasajeros que viajan a {country_selected} es {counter}")

while(menu == True):
    print(" Opcion 1: Agregar pasajeros a la lista de viajeros \n",
          "Opcion 2: Agregar ciudades a la lista de ciudades \n",
          "Opcion 3: Dado el DNI de un pasajero, ver a qué ciudad viaja \n",
          "Opcion 4: Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad \n",
          "Opcion 5: Dado un país, mostrar cuántos pasajeros viajan a ese país  \n", 
          "Opcion 6: Salir  \n")
    
    option = int(input("Ingrese una opción: "))

    if(option == 1):
        add_passenger()
    elif(option == 2):
        add_destiny()
    elif(option == 3):
        dni = int(input("Ingrese el dni de un pasajero: "))
        find_city(dni)
    elif(option == 4):
        city = input("Ingrese una ciudad: ")
        find_cant_pasenger(city)
    elif(option == 5):
        country = input("Ingrese un pais: ")
        cant_country(country)
    elif(option == 6):
        break
    else:
        print("Ingreso una opción incorrecta")
    print("-----------------------------------")'''

#EJERCICIO 2
'''Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, la cual
contiene tuplas con información de cada venta: (cliente, día del mes, monto, domicilio del cliente). Ejemplo:
*(‘Nuria Costa’, 5, 1234.5,’Calle 1 – 456’), (‘Jorge Russo’, 7, 3999, ‘Calle 2 – 741’)+
Escribir una función que reciba como parámetro una lista con el formato mencionado anteriormente y
retorne los domicilios de cada cliente al cual se le debe enviar una factura de compra. Notar que cada cliente
puede haber hecho más de una compra en el mes, por lo que la función debe retornar una estructura que
contenga cada domicilio una sola vez.
 
list_sales = [ #Lista con las ventas
    ("Pablo Lima", 1, 2500.5, "Cangallo - 3011"),
    ("Elena Garcia", 2, 1800.0, "Belgrano - 1234"),
    ("Diego Lopez", 3, 3500.75, "Rivadavia - 987"),
    ("Carla Sanchez", 4, 2200.0, "Lima - 5678"),
    ("Andres Torres", 5, 2800.25, "San Martin - 4321"),
    ("Pablo Lima", 6, 2600.0, "Cangallo - 3011"),
    ("Ana Martinez", 7, 3100.5, "Balcarce - 6543"),
    ("Carlos Ramirez", 8, 2400.75, "9 de Julio - 2938"),
    ("Maria Gonzalez", 9, 2900.0, "Belgrano - 1234"),
    ("Lucas Fernandez", 10, 3200.25, "Sarmiento - 785"),
    ("Pablo Lima", 11, 3000.5, "Cangallo - 3011"),
    ("Luisa Rodriguez", 12, 2300.0, "San Martin - 4321"),
    ("Miguel Torres", 13, 3600.75, "Rivadavia - 987"),
    ("Pablo Lima", 14, 2700.0, "Cangallo - 3011"),
    ("Laura Perez", 15, 3300.5, "Urquiza - 1304"),
    ("Marcos Diaz", 16, 2600.75, "Lima - 5678"),
    ("Pablo Lima", 17, 3100.0, "Cangallo - 3011"),
    ("Julieta Romero", 18, 3500.25, "Belgrano - 1234"),
    ("Juan Martinez", 19, 2800.5, "Rivadavia - 987"),
    ("Pablo Lima", 20, 2900.0, "Cangallo - 3011")
]

def bill(list):
    list_aux = []

    for name, day, amount, address in list: #Recorro la lista y guardo las variables y las hago una tupla
            
            nameAux = name
            addressAux = address
            one_tuple = (nameAux, addressAux)

            if(one_tuple not in list_aux): #Si esa tupla esta en la lista ya, no la añado pero si no esta la añado asi quedan gurdadas solo una vez als direcciones de todos los clientes
                list_aux.append(one_tuple)

    return list_aux

print(bill(list_sales))'''

#EJERCICIO 3
'''Crear un programa para gestionar datos de los socios de un club, permitiendo:
- Cargar información de los socios en un diccionario para acceder por número de socio. Los datos a almacenar
son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al día (s/n). El programa debe iniciar
con los datos de los socios fundadores ya cargados:
o Socio n°1, Amanda Núñez, ingresó: 17/03/2009, cuota al día.
o Socio n°2, Bárbara Molina, ingresó: 17/03/2009, cuota al día.
o Socio n°3, Lautaro Campos, ingresó: 17/03/2009, cuota al día.
- Informar cantidad de socios del club.
- Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas adeudadas.
- Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, para indicar que en realidad
ingresaron el 14/03/2018.
- Solicitar el nombre y apellido de un socio y darle de baja (eliminarlo del listado)
- Imprimir el listado de socios completo.

partner_information = {
    1 : ("Amanda Núñez", 17032009, True),
    2 : ("Bárbara Molina", 17032009, True),
    3 : ("Lautaro Campos", 17032009, True),
    #100: ("Pablo Lima", 13032018, True)
}

def cargar_usuario():
    name = input("Ingrese el nombre del socio: ")
    date = int(input("Ingrese la fecha en formato ddmmaaaa: "))
    current_membership = bool(input("La cuota esta al dia: "))
    key_membership = int(input("Ingrese el número del socio: "))

    partner_information[key_membership] = (name, date, current_membership)

def debts_paid(num_partner):
    if num_partner in partner_information:
        name, day, debt = partner_information[num_partner]
        if debt:
            print(f"Las deudas ya estaban pagadas del socio {num_partner}")
        else:
            partner_information[num_partner] = (name, day, True)
            print(f"Las deudas han sido pagadas del socio {num_partner}")
    else: 
        print(f"El socio con el número {num_partner} no ha sido encontrado")

def modify_date():
    old_date = int(13032018)
    new_date = int(14032018)

    for key, (name, day, debt) in partner_information.items():
        if day == old_date:
            partner_information[key] = (name, new_date, debt)
    
def name_partner_delete(name_partner):
    key_to_delete = None

    for key, (name, _, _) in partner_information.items():
        if name == name_partner:
            key_to_delete = key
            break

    if key_to_delete is not None:
        del partner_information[key_to_delete]
        print(f"El usuario {name_partner} fue eliminado")
    else:
        print(f"El usuario {name_partner} no existe")


def show_partners():
    for key in partner_information:
        name = partner_information[key][0]
        print(f"El nombre del socio número {key} es: {name}")

menu = True

while(menu == True):
    print(" Opcion 1: Cargar información de los socios en un diccionario \n",
          "Opcion 2: Informar cantidad de socios del club \n",
          "Opcion 3: Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas adeudadas \n",
          "Opcion 4: Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, para indicar que en realidad ingresaron el 14/03/2018 \n",
          "Opcion 5: Solicitar el nombre y apellido de un socio y darle de baja \n",
          "Opcion 6: Imprimir el listado de socios completo \n", 
          "Opcion 7: Salir  \n")
    
    option = int(input("Ingrese una opción: "))

    if(option == 1):
        cargar_usuario()
    elif(option == 2):
        print(f"La cantidad de socios del club es {len(partner_information)}")
    elif(option == 3):
        num_partner = int(input("Ingrese el número de socio: "))
        debts_paid(num_partner)
    elif(option == 4):
        modify_date()
    elif(option == 5):
        name_partner = input("Ingrese el nombre del socio a eliminar: ")
        name_partner_delete(name_partner)
    elif(option == 6):
        show_partners()
    elif(option == 7):
        break
    else:
        print("Ingreso una opción incorrecta")
    print("-----------------------------------")

print(partner_information)'''