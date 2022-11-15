from cuenta import cuenta


class cuentaJoven(cuenta):

    def __init__(self,cuenta, bonificacion):
        super().__init__(cuenta.titular, cuenta.cantidad)
        self.__bonificacion=bonificacion
  
    def retirar(self,nuevaCantidad):
        if nuevaCantidad > 0 and self.esTitularValido():
            super().retirar(nuevaCantidad)

    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self,bonificacion):
        self.__bonificacion=bonificacion
    
    def esTitularValido(self):
        return self.titular.esMayorDeEdad() and self.titular.edad < 25 #Como cuentaJoven hereda de cuenta: self.titular hace referencia al objeto titular de cuenta, es decir, su titular

    def mostrar(self):
        return super().mostrar()+":Cuenta Joven: "+str(self.__bonificacion)+"%"