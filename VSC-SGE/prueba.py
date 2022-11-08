class C:
    def __init__(self):
        self.__x = None
    @property
    def getx(self):
        return self.__x
    @x.setter
    def setx(self, value):
        self.__x = value
    @x.deleter
    def delx(self):
        del self.__x