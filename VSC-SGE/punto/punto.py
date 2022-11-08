import math
class punto():
    """ Representación de un punto en el plano, los atributos son x e y
    que representan los valores de las coordenadas cartesianas."""

    def __init__(self,x=0,y=0):
        self.__x=x
        self.__y=y

    def mostrar(self):
        return str(self.x)+":"+str(self.y)
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y

    def distancia(self, otro):
        """ Devuelve la distancia entre ambos puntos. """
        dx = self.__x - otro.x
        dy = self.__y - otro.y
        return math.sqrt((dx*dx + dy*dy))
    