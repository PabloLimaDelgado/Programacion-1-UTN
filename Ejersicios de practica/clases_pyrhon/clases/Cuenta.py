class Cuenta:
    def __init__(self, headline=""):
        self.__headline = headline
        self.__amount = 0
        self.__can_change_headline = False

    @property
    def headline(self):
        return self.__headline

    @headline.setter
    def headline(self, new_headline):
        if self.__can_change_headline: 
            self.__headline = new_headline
            self.__can_change_headline = False 
        else:
            print("No puedes cambiar el titular sin mover dinero.")

    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, value):
        self.__amount = value

    def cambiar_atributo(self):
        option = int(input("Para cambiar el nombre debe mover dinero: [1]Para mover Dinero [0]Para salir: "))

        if option == 1:
            option_two = int(input("[1]Para retirar Dinero [2]Para ingresar dinero: "))

            if option_two == 1:
                count_money = int(input("Cantidad de dinero a retirar: "))
                self.__amount -= count_money
            
            elif option_two == 2:
                count_money = int(input("Cantidad de dinero a ingresar: "))
                self.__amount += count_money

            self.__can_change_headline = True  
            new_headline = input("Ingrese el nuevo nombre del titular: ") 
            self.headline = new_headline  

    def mostrar_datos(self):
        print(f"El nombre del titular es: {self.__headline} y el dinero en su cuenta es {self.__amount}")


    def retirar_dinero(self, money):
        self.__amount -= money

        print(f"El dinero en su cuenta es: {self.amount}")

    def ingresar_dinero(self, money):
        self.__amount += money

        print(f"El dinero en su cuenta es: {self.amount}")