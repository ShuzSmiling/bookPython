# Class CellPhone contains data for mobile phone

class CellPhone:
    
    def __init__(self, manufact, model, price):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = price
        

    # method set_manufact accepts argument
    # for manufacturer phone
    def set_manufact(self, manufact):
        self.__manufact = manufact
        
    
    # method set_model accepts argument
    # for number mobile phone
    def set_model(self, model):
        self.__model = model
        
    
    # method set_retail_price accepts 
    # argument for retail_price phone
    def set_retail_price(self, price):
        self.__retail_price = price
        
    
    # method get_manufact return 
    # manufact phone
    def get_manufact(self):
        return self.__manufact
    
    
    # method get_model return
    # number model phone
    def get_model(self):
        return self.__model
    
    
    # method get_retail_price return
    # retail price phone
    def get_retail_price(self):
        return self.__retail_price
    
     