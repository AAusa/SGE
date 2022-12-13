from vehiculo import vehiculo
class garage():
    ruedas = 4
    def __init__(self,numVehiculos, vehiculos):
        self.__numVehiculos = numVehiculos
        self.__vehiculos=vehiculos

    @property
    def numVehiculos(self):
        return self.__numVehiculos

    @numVehiculos.setter
    def numVehiculos(self,numVehiculos):
        self.__numVehiculos=numVehiculos
    
    @property
    def vehiculos(self):
        return self.__vehiculos

    @vehiculos.setter
    def vehiculos(self,vehiculos):
        self.__vehiculos=vehiculos

    def totalKm(self):
        totalkm = 0
        for vehiculo in self.__vehiculos:
            totalkm += vehiculo.km
        return totalkm

    def totalCombustible(self):
        totalCombustible = 0
        for vehiculo in self.__vehiculos:
            totalCombustible += vehiculo.combustible
        return totalCombustible
    
    def annadirVehiculo(self, vehiculo):
        self.__vehiculos.append(vehiculo)
        self.__numVehiculos=self.__numVehiculos+1

    def quitarVehiculo(self, matricula):
        for vehiculo in self.__vehiculos:
            if vehiculo.matricula == matricula:
                self.__vehiculos.remove(vehiculo)
                self.__numVehiculos=self.__numVehiculos-1