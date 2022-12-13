from vehiculo import vehiculo
class moto(vehiculo):
    def __init__(self,vehiculo, motor):
        super().__init__(vehiculo.nombre,  vehiculo.matricula,  vehiculo.ruedas,  vehiculo.anioFabricacion,  vehiculo.velocidad,  vehiculo.combustible,  vehiculo.velocidadMaxima,  vehiculo.km)
        self.__motor=motor
    ruedas = 2
    @property
    def motor(self):
        return self.__motor

    @motor.setter
    def motor(self,motor):
        self.__motor=motor

    def caballitos(self):
        return "Puedo hacer caballitos"