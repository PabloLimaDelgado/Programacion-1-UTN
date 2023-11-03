class Persona:
    def __init__ (self):
        self.__name = ""
        self.__age = 0
        self.__dni = ""

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, __name):
        self.__name = __name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, __age):
        self.__age = __age

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, __dni):
        self.__dni = __dni

    
    def mostrar_datos(self):
        print(f"Los datos de la persona {self.__name} son edad: {self.__age} y DNI: {self.__dni}")

    def esMayorDeEdad(self):
        return True if self.__age >= 18 else False