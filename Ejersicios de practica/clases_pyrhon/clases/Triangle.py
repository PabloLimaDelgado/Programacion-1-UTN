class Triangle:
    def __init__(self):
        self.__side_1 = 0
        self.__side_2 = 0
        self.__side_3 = 0

    @property
    def side_1(self):
        return self.__side_1
        
    @side_1.setter
    def side_1(self, new_side_1):
        self.__side_1 = new_side_1

    @property
    def side_2(self):
        return self.__side_2
        
    @side_2.setter
    def side_2(self, new_side_2):
        self.__side_2 = new_side_2

    @property
    def side_3(self):
        return self.__side_3
        
    @side_3.setter
    def side_3(self, new_side_3):
        self.__side_3 = new_side_3

    def show_dates(self):
        print(f"Lado 1: {self.__side_1}, Lado 2: {self.__side_2}, Lado 3: {self.__side_3}")

    def what_triangle_is(self):
        if( (self.__side_1 == self.__side_2)  and  
            (self.__side_1 == self.__side_3) and 
            (self.__side_2 == self.__side_3) ):

            print(f"El triangulo es equilátero")
        
        elif ( (self.__side_1 == self.__side_2)  and  (self.__side_1 != self.__side_3) ):
            
            print(f"El triangulo es isóseles")
        
        elif ( (self.__side_1 != self.__side_2)  and  
               (self.__side_1 != self.__side_3) and 
               (self.__side_2 != self.__side_3) ):
            
            print(f"El triangulo es escaleno")
