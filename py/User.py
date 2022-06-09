class User:
    __name = None
    __licensePlate = None
    __role = None
    __creditcard = None
    
    def __init__(self, name, licensePlate, role, creditcard):
        self.__name = name
        self.__licensePlate = licensePlate
        self.__role = role
        self.__creditcard = creditcard