# Класс automobile содержит общие данные
# об авто на складе

class Automobile:
    
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price
        
    
    def set_make(self, make):
        self.__make = make
        
    
    def set_model(self, model):
        self.__model = model
        
    
    def set_mileage(self, mileage):
        self.__mileage = mileage
        
        
    def set_price(self, price):
        self.__price = price
        
    
    def get_make(self):
        return self.__make
    
    
    def get_model(self):
        return self.__model
    
    
    def get_mileage(self):
        return self.__mileage
    
    
    def get_price(self):
        return self.__price
    
    
class Car(Automobile):
    
    def __init__(self, make, model, mileage, price, doors):
        Automobile.__init__(self, make, model, mileage, price)
        self.__doors = doors
        
    
    def set_doors(self, doors):
        self.__doors = doors
        
        
    def get_doors(self):
        return self.__doors
    

class Truck(Automobile):

    def __init__(self, make, model, mileage, price, drive_type):
        Automobile.__init__(self, make, model, mileage, price)
        self.__drive_type = drive_type
        
    
    def set_drive_type(self, drive_type):
        self.__drive_type = drive_type
        
    
    def get_drive_type(self):
        return self.__drive_type