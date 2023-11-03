#from Contact import Contact

class Diary:

    list_contact = []

    def __init__(self, id):
        self.id = id

    
    def new_contact(self, contact):
        Diary.list_contact.append(contact)

    def show_contacts(self):
        i = 1
        for contacts in Diary.list_contact:
            print(f"Los contactos de la lista {self.id} son: ")
            print(f"Nombre del contacto {i} es: {contacts.name}")
            print(f"Mail del contacto {i} es: {contacts.email}")
            print(f"Número del contacto {i} es: {contacts.number}")
            i += 1

    def find_contac_with_name(self, name):
        for contacts in Diary.list_contact:
            if contacts.name == name:
                print(f"Los datos del contacto son: ")
                print(f"Nombre del contacto es: {contacts.name}")
                print(f"Mail del contacto es: {contacts.email}")
                print(f"Número del contacto es: {contacts.number}")

    def modify_contact(self, contact):
        if contact in Diary.list_contact:
            option = int(input("Ingrese que desea modificar: 1.Nombre 2.Email 3.Número: "))

            if(option == 1):
                contact.name = input("Ingrese el nombre: ")

            elif(option == 2):
                contact.email = input("Ingrese el email: ")
            
            elif(option == 3):
                contact.number = input("Ingrese el numero: ")

    def close_agency(self):
        print(f"La agenda con id {self.id} ha sido cerrada")