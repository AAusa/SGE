from vehiculo import vehiculo
from coche import coche
from moto import moto
from bicicleta import bicicleta
from garage import garage
v = vehiculo("v","12312312K",2,1992, 1, 1, 20, 0)
c = coche(v, "qwqS")
print(c.aString)

m = moto(v, "qwqS")
print(m.aString)

b = bicicleta(v, 2)
print(b.aString)

g = garage(3, [c,m,b])

