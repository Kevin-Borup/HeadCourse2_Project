class Creditcard:
    __name = None
    __cardNumber = None
    __cardCode = None
    __expDate = None
    
    def __init__(self, name, cardNumber, cardCode, expDate):
        self.__name = name
        self.__cardNumber = cardNumber
        self.__cardCode = cardCode
        self.__expDate = expDate