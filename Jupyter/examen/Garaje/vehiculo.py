class vehiculo():
    def __init__(self,nombre, matricula, ruedas, anioFabricacion, velocidad, combustible, velocidadMaxima, km):
        self.__nombre = nombre
        self.__matricula=matricula
        self.__ruedas = ruedas
        self.__anioFabricacion=anioFabricacion
        self.__velocidad = velocidad
        self.__combustible=combustible
        self.__velocidadMaxima = velocidadMaxima
        self.__km=km
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self,matricula):
        self.__matricula=matricula
    
    @property
    def ruedas(self):
        return self.__ruedas

    @ruedas.setter
    def ruedas(self,ruedas):
        self.__ruedas=ruedas

    @property
    def anioFabricacion(self):
        return self.__anioFabricacion

    @anioFabricacion.setter
    def anioFabricacion(self,anioFabricacion):
        self.__anioFabricacion=anioFabricacion
    
    @property
    def velocidad(self):
        return self.__velocidad

    @velocidad.setter
    def velocidad(self,velocidad):
        self.__velocidad=velocidad

    @property
    def combustible(self):
        return self.__combustible

    @combustible.setter
    def combustible(self,combustible):
        self.__combustible=combustible

    @property
    def velocidadMaxima(self):
        return self.__velocidadMaxima

    @velocidadMaxima.setter
    def velocidadMaxima(self,velocidadMaxima):
        self.__velocidadMaxima=velocidadMaxima
    
    @property
    def km(self):
        return self.__km

    @km.setter
    def km(self,km):
        self.__km=km

    def acelerar(self,velocidad):
        if self.__velocidad+velocidad < self.__velocidadMaxima:
            self.__velocidad=self.__velocidad+velocidad

    def frenar(self,velocidad):
        if self.__velocidad-velocidad > 0:
            self.__velocidad=self.__velocidad-velocidad

    def aString(self):
        return str(self.__nombre)+":"+str(self.__matricula)+":"+str(self.__ruedas)+":"+str(self.__anioFabricacion)+":"+str(self.__velocidad)+":"+str(self.__combustible)+":"+str(self.__velocidadMaxima)+":"+str(self.__km)
    