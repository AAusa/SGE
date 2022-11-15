from persona import persona
class cuenta():

    def __init__(self,titular, cantidad=0):
        self.__titular = titular
        self.__cantidad=cantidad


    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self,titular):
        self.__titular=titular

    @property
    def cantidad(self):
        return self.__cantidad

    def ingresar(self,cantidad):
        if cantidad > 0:
            self.__cantidad=self.__cantidad+cantidad

    def retirar(self,cantidad):
        if cantidad > 0:
            self.__cantidad=self.__cantidad-cantidad

    def mostrar(self):
        return self.__titular.mostrar()+":"+str(self.__cantidad)
    