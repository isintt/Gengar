# Uso de Len
# Ninja = "kkk"
# print(Len(Ninja))
# se utiliza Len para contar las letras.

# uso de replace
# Ninja = "kkk"
# print(Len(Ninja))
# print(Len(Ninja.replace(" ", "")))
# Se utiliza replace para eliminar los espacios.

print("¿cuantos juegos son?")
juegos = int(input("Ingrese numero de juegos: "))

print("para poder registrarse en el juego. registre su nombre")
print("debe tener al menos 5 caracteres.")
nom = input("ingrese su nombre de usuario: ")

while " " in nom:
    try:
        print("no debe haber espacios. intentelo de nuevo")
        nom = input("ingrese su nombre de usuario: ")
        (len(nom))
    except:
        print("ingreso invalido")