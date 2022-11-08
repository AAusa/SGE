from punto import punto

class punto3d(punto):
    def __init__(self,x=0,y=0,z=0):
        super().__init__(x,y)
        self.__z=z

    def __init__(self,p,z=0):#Constructor al que se pasa el punto(2d) y z
        super().__init__(p.x,p.y)
        self.__z=z

    @property
    def z(self):
        print("Doy z")
        return self.z

    @z.setter
    def z(self,z):
        print("Cambio z")
        self.z=z

    def mostrar(self):
        return super().mostrar()+":"+str(self.z)

    def distancia(self,otro):
        dx = self.x - otro.x
        dy = self.y - otro.y
        dz = self.__z - otro.__z
        return (dx*dx + dy*dy + dz*dz)**0.5	

# p = punto3d(0,0,0)
# print(p.mostrar())