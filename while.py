#explicacion y ejemplos de while

##Tabla de multiplicar con while
#cont=0
#num=8
#while cont<=10:
#    print("la del 8 es ", num*cont)
#    cont+=1


    ##codigo secreto
#    code=3424

#    pwd=int(input("ingrese el pin"))

#    while code!=pwd:
#        print("error, intentelo de nuevo")
#        pwd=int(input())


op=0
total=0
while op!=4:
    print("1.- radio stereo sony $70.000")
    print("2.- LGTV 55 pulgadas super gamer $500.000")
    print("3.- PS5 $580.000")
    print("4.- salir")
    print("seleccione una opcion")
    op=int(input())
    match op:
        case 1:
            print("el precio ha pagar es ", 700000*19)
            total+=700000*1.19
        case 2:
            print("el precio ha pagar es ", 500000*19)
            total+=500000*1.19
        case 3:
            print("el precio ha pagar es ", 580000*19)
            total+=580000*1.19
        case 4:
            print("saliendo")  
            op=4  
        case _:
            print("opcion invalida")