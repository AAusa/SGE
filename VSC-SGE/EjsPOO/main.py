from persona import persona
from cuenta import cuenta
from cuentaJoven import cuentaJoven

p = persona("pepe",20,"12312312K")
# print(p.mostrar())
# p1 = persona("pepe",-1)#No se crea
# print(p1.edad())

c = cuenta(p,10)
# c.ingresar(10)
# print(c.cantidad)

cj = cuentaJoven(c,20)
cj.retirar(5,c.titular.edad)
print(cj.cantidad)
#print(cj.mostrar())
