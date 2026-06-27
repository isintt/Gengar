## Crear un gestor de pacientes

pacientes=[
    {"nombre": " Aquiles Baeza", "prevision": "Fonasa", 
     "temperatura":34.6, "grave": False}
]

# '''crear al gestor de pacientes en un centro medico
# Para poner el nombre se debe validar que no este vacio 
# y ademas tenga mas de 8 caracteres
# Para la prevision de salud solo exiten 3 posibles valores
# Fonasa, Isapre, o Fodesa
# Al ingresar un paciente, se debe poner la temperatura
# Crear una funcion que valide si esta grave o no
# Para que este grave debe tener mas de 39°''' -->


pacientes.append({"nombre": ""})

def estado(temperatura):
        if temperatura>39:
             return True
        else:
             return False

def mostpaciente():
     if len():
          print()

while True:
    try:
        print("--Gestor de pacientes--")
        print("ingrese el nombre del paciente")
        pacient=input("Nombre del paciente: ")
    except:
        print("Nombre invalido. ingreselo nuevamente.")

