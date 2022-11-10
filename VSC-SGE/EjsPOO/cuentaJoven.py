from cuenta import cuenta
class cuentaJoven(cuenta):

    def __init__(self,cuenta, bonificacion):
        super().__init__(cuenta.titular, cuenta.cantidad)
        self.__bonificacion=bonificacion
  
    def retirar(self,nuevaCantidad,edad):
        if nuevaCantidad > 0 and self.esTitularValido(edad):
            cantidad=cantidad-nuevaCantidad

    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self,bonificacion):
        self.__bonificacion=bonificacion
    
    def esTitularValido(self, edad):
        return super().titular.esMayorDeEdad(edad) and edad < 25

    def mostrar(self):
        return super().mostrar()+":Cuenta Joven: "+str(self.__bonificacion)+"%"