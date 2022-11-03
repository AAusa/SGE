class alumno():
    def __init__(self,nombre="Antonio"):
        self.nombre=nombre
        self.__secreto="asdasd"
    @property
    def secreto(self):
       return self.__secreto