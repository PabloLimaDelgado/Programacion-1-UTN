class Contact:
   def __init__(self, name, email):
      self.name = name
      self.email = email
      self.__number = 0

   @property
   def number(self):
        return self.__number
        
   @number.setter
   def number(self, new_number):
        self.__number = new_number
