from cuenta import cuenta
from cuentaJoven import cuentaJoven
from persona import persona

p = persona("pepe",20,"12312312K")
print("Persona: ",p.mostrar())
# p1 = persona("pepe",-1)#No se crea
# print(p1.edad())

c = cuenta(p,10)
print("Cuenta: ",c.mostrar())
c.ingresar(10)
print("Cantidad de cuenta: ",c.cantidad)

cj = cuentaJoven(c,20)
cj.retirar(5)
print("Cantidad de cuenta joven: ",cj.cantidad)
print("CuentaJoven: ",cj.mostrar())
