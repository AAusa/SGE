from vehiculo import vehiculo
class coche(vehiculo):
    def __init__(self,vehiculo, motor):
        super().__init__(vehiculo.nombre,  vehiculo.matricula,  vehiculo.ruedas,  vehiculo.anioFabricacion,  vehiculo.velocidad,  vehiculo.combustible,  vehiculo.velocidadMaxima,  vehiculo.km)
        self.__motor=motor

    ruedas = 4
    @property
    def motor(self):
        return self.__motor

    @motor.setter
    def motor(self,motor):
        self.__motor=motor

    def marchaAtras(self):
        if self.__velocidad == 0:
            self.__velocidad=-10