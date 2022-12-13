from vehiculo import vehiculo
class bicicleta(vehiculo):
    def __init__(self,vehiculo, pedales):
        super().__init__(vehiculo.nombre,  vehiculo.matricula,  vehiculo.ruedas,  vehiculo.anioFabricacion,  vehiculo.velocidad,  vehiculo.combustible,  vehiculo.velocidadMaxima,  vehiculo.km)
        self.__pedales=pedales
    ruedas = 2
    @property
    def pedales(self):
        return self.__pedales

    @pedales.setter
    def pedales(self,pedales):
        self.__pedales=pedales

    def pedalear(self):
        return "Voy a pedales"