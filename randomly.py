#Killer instintc

#dos peleadores se piden al inicio de la pelea
#cada peleador inicia con 100 de HP
#se debe hacer una pelea por turnos
#y cada golpe varia entre 7 y 18
#se termina el match cuando uno de los 2
#tiene su HP menor o igual a 0
#se debe mostrar el ganador al final

import time
import random 

p1=input("ingrese el nombre del peleador 1")
p2=input("ingrese el nombre del peleador 2")
hp1=100
hp2=100
turno=random.randint(1,2)

while hp1>0 and hp2>0:
    if turno%2==0:
        print(f"turno de {p1}")
        atk=random.randint(7,18)
        print(f"el {p1} ataca con {atk} ")
        hp2-=atk
        print(f"el hp de {p2} es {hp2}")
    else:
        print(f"turno de {p2}")
        atk=random.randint(7,18)
        print(f"el {p2} ataca con {atk} ")
        hp2-=atk
        print(f"el hp de {p1} es {hp1}")
        time.sleep(1)
    turno=+1
    print(p1, ""*hp1)
    print(p2, ""*hp2)
if hp1>hp2:
    print("el ganador es ", p1)
else:
    print("el ganador es ", p2)