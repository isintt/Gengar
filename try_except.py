# while True:
#     try:
#         edad=int(input("ingrese su edad: ")) # si aparece un error,
#         # salta a la linea 6, donde esta except para manejar el error.
#         print("su edad es ", edad)
#         break
#     except ValueError as e: # se puede utilizar cualquier variable, usualmente es una e.
#         print("solo se aceptan numeros enteros")
#         print(e)


# for i in range(10):
#     n1=int(input("ingrese un numero: "))
#     if n1%2!=0:
#         break # le pone un fin al bucle (en este caso al ingresar un numero impar).


# ingrese numeros indefinidamente
# hasta que ponga el numero 0
# sumelos y muestre el total.

# num=0
# while True:
#     try:
#         n1=int(input("ingrese un numero: "))
#         num+=n1
#         if n1==0:
#             break
#     except:
#         print("Solo numeros enteros")

#     print("el total es" , num)


# op=0
# total=0 #acumulador. ya que se ponen distintos valores que se van sumando.
# cantprod=0 #contadores.
# while op!=4:
    # try:
    #     print("1.- radio stereo sony $70.000")
    #     print("2.- LGTV 55 pulgadas super gamer $500.000")
    #     print("3.- PS5 $580.000")
    #     print("seleccione una opcion")
    #     op=int(input())
    #     match op:
    #         case 1:
    #             print("el precio ha pagar es ", 700000*1.19)
    #             total+=700000*1.19
    #             cantprod+=1
    #         case 2:
    #             print("el precio ha pagar es ", 500000*1.19)
    #             total+=500000*1.19
    #         case 3:
    #             print("el precio ha pagar es ", 580000*1.19)
    #             total+=580000*1.19
    #         case 4:
    #             print(f"su total a pagar es {total}")
    #             print(f"su total de producto es {cantprod}")
    #         case _:
    #             print("opcion invalida")
    # except:
    #     print("Debe ingresar solo numeros enteros")



#Ejemplo de validacion:
porc=float(input("ingrese el porcentaje de rucos en su comuna"))

if porc>0 and porc<100:
    print("porcentaje correcto")
else:
    print("porentaje fuera de rango")





toon1= input("ingrese el toon 1")
toon2= input("ingrese el toon 2")

v1=0
v2=0
while True:
    try:
        cant=int(input("¿cuantos votantes son? "))
        break
    except:
        print("solo puede ingresar valores enteros positivos")





