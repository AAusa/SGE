from punto3d import punto3d
import punto

p = punto()
pa = punto(4,5)
print(p.distancia(pa))

p0 = punto(1,5)#1,5
p1 = punto3d(p0,1)#1,5,1
p2 = punto3d()#0,0,0
p2 = punto3d(punto(2,1))#2,1,0
print(p1.distancia(p2))
