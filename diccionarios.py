# Uso y explicacion de diccionarios.

alumno={
    "nombre":"Shinji Ikari",
    "edad":14,
    "carrera":"piloto"
}

# print(alumno)
# for Key, value in alumno.items():
#     print(Key, value)

# print(alumno)
# for Key, value in alumno.items():
#     print(f"{Key}= {value}")
# print("---Cambio de datos---")

# alumno["email"]="Shinji@nerv.com"
# alumno["carrera"]="escritor"
# del alumno["edad"]
# for key,value in alumno.items():
#     print(f"{key}= {value}")

# Diccionario
# productos={
#     1:{"nombre": "control inalambrico",
#     "categoria": "electronica",
#     "precio": 45000},
#     2:{"nombre": "pilas recargables",
#     "categoria": "insumos",
#     "precio": 50000},
#     3:{"nombre": "pasta termica",
#     "categoria": "computacion",
#     "precio": 7000}
# }

# print(productos[1]["nombre"])

# # Lista
# productos=[
#     {"nombre": "control inalambrico",
#     "categoria": "electronica",
#     "precio": 45000},
#     {"nombre": "pilas recargables",
#     "categoria": "insumos",
#     "precio": 50000},
#     {"nombre": "pasta termica",
#     "categoria": "computacion",
#     "precio": 7000}
# ]

# print(productos[1]["nombre"])



# TAREA LISTA
# Modificar el programa del carrito de compras
# para poder utilizarlo con listas
# el producto debe tener Nombre y Precio

productos=[]
while True:
    try:
        print("1.- Agregar producto")
        print("2.- mostrar productos")
        print("3.- Eliminar producto")
        print("4.- Actuaizar producto")
        print("5.- salir")
        op=int(input("seleccione una opcion: "))
    except:
        print("")
    match op:
        case 1:
            nombre=input("ingrese el nombre del producto: ")
            precio=int(input("ingrese el precio del producto: "))
            nuev_prod={"nombre":nombre, "precio":precio}
            productos.append(nuev_prod)
        case 2:
            print(productos)
        case 3:
            print("")
        case 4:
            print("saliendo")
            break
        case _:
            print("opcion invalida")