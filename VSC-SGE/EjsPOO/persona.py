class persona():

    def __init__(self,nombre="", edad=0, dni=""):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        if edad > 0 and edad < 100 and (len(dni) == 9 and letras[int(dni[:8]) % 23] == dni[8]):
            self.__nombre=nombre
            self.__edad=edad
            self.__dni=dni


    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self,edad):
        if edad > 0 and edad < 100:
            self.__edad=edad

    @property
    def dni(self):
        return self.__dni

    @edad.setter
    def dni(self,dni):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        if (len(dni) == 9 and letras[int(dni[:8]) % 23] == dni[8]):
            self.__dni=dni
    

    def mostrar(self):
        return str(self.__nombre)+":"+str(self.__edad)+":"+str(self.__dni)

    def esMayorDeEdad(self):
        return self.__edad >= 18