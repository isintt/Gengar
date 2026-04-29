op = 0
cantPersonas = 0
total = 0
while op != 4:
    print("""
        1.- Niño (1-17) 1000
        2.- Adulto (18-64) 3000
        3.- Adulto Mayor (64 o mas) 1500
        4.- Salir""")
op = int(input("seleccione una opcion"))
match op:
    case 1:
        print("pagando el precio de niño")
        print("¿cuantos niños son?")
        cantN = int(input("ingrese la cantidad de niños que son"))
        while cantN < 1 or cantN > 10:
            print("el numero esta fuera de rango (1-10)")
            cantN = int(input(""))
        cantPersonas += cantN
        total += cantN * 1000
    case 2:
        print("pagando el precio de Adulto")
        cantA = int(input("ingrese la cantidad de adultos"))
        cantPersonas += cantA
        total += cantA * 3000
    case 3:
        print("pagando el precio de Adulto Mayor")
        cantAD = int(input("ingrese la cantidad de Adulto Mayor"))
        cantPersonas += cantAD
        total += cantAD * 1500
    case 4:
        print("Saliendo del programa")
        print(f"el total a pagar es {total}")
        print(f"la cantidad de personas son {cantPersonas}")
        op = 4
    case _:
        print("opcion invalida")


# preguntar sobre el ingreso de
