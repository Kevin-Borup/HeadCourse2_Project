class ParkingLot:
    __totalspaces = None
    __availableSpaces = None
    __usedSpaces = None

    def __init__(self, totalSpaces, availableSpaces, usedSpaces):
        self.__totalspaces = totalSpaces
        self.__availableSpaces = availableSpaces
        self.__usedSpaces = usedSpaces

    def AddCar(self, availableSpaces, usedSpaces):
        """If car enters, then used spaces adds up"""
        self.__availableSpaces = availableSpaces - 1
        self.__usedSpaces = usedSpaces + 1
        return
    def GetAvailableSpaces():
        """Show available spaces"""
        #print("Available spaces: " + self.__availableSpaces)
        return
    def GetUsedSpaces():
        """Show used spaces"""
        #print("Used spaces: " + self.__usedSpaces)
        return
    def RemoveCar(self, availableSpaces, usedspaces):
        """If car leaves, then available spaces adds up"""
        self.__availableSpaces = availableSpaces + 1
        self.__usedSpaces = usedspaces - 1
        return