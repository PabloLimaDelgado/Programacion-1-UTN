
class Motocicleta:
    new_moto = "Nueva"
    engine = False

    #CONSTRUCTOR VACIO
    '''def __init__(self) -> None:
        pass'''
    
    def __init__ (self, color, matricula, combustible_litros, numero_ruedas, marca, fecha_fabricacion, velocidad_punta, peso):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.__modelo = ""
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso

    @property
    def modelo(self):  # Getter
        return self.__modelo
    
    @modelo.setter
    def modelo(self, __model):  # Setter
        self.__modelo = __model
    
    def start_engine(self):
        if(self.engine == True):
            print("El motor ya estaba en funcionamiento")

        else:
            print("El motor estaba apagado, ahora esta encendido")
            self.engine = True

    def off_engine(self):
        if(self.engine == False):
            print("El motor ya estaba apagado")

        else:
            print("El motor estaba encendido, ahora esta apagado")
            self.engine = False
    

    def consult_price(self):
        return self.price


    def mostrar_modelo(self):
        print(self.__modelo)
