# sin argumento y sin retorno.
def saludo():
    print("hola que tal")

# sin argumento y con retorno.
def suma():
    num1= 3
    num2 = 5
    return(num1 + num2)

def esMayor():
    edad=24
    if edad>=18:
        return True
    else:
        return False

result=suma()

print(result)

# Con argumento y sin retorno
def saludaMe(name):
    print("hola", name)

saludaMe("fiby")

def calculaIVA(neto):
    print(f"el precio con IVA es {neto*1.19}")

calculaIVA(4000)

#Con argumento y con retorno
def sumaCA(n1,n2):

    return(n1 + n2)


def calculaIVA(neto):
    return neto*1.19

print("el resultado es:", sumaCA())
print("el total con IVA es: ", calculaIVA(10000))


v = int(input("ingrese el valor neto: "))

print("el total con IVA es: ", calculaIVA(v))


def calculaDescuento(valor, desc):
    return valor -(valor*desc/100)
datos=[29500, 22]
print("El valor con descuento es", calculaDescuento(*datos))




# actividad 333
nombre = input("ingresa tu nombre: ")
nom=nombre.split() # split para hacer lista los nombres/numeros que se ingresen
print(nom)


numeros=input("ingresa una lista de numeros para saber cuales " \
              "son pares y cuales son impares. separalos por espacios: ")

def paresImpares():
        print()


# Cree una funcion para pedir notas
# y ponerlas en el argumento para sacar el promedio

cnotas=int(input("Ingrese lacantidad de notas: "))
notas=[0]
for n in range(cnotas):
    nota=int(input(f"ingrese la nota {n+1}: "))
    notas.append(nota)

def calcularprom(no):
    return sum(no/len(no))

print("El promedio es ", calcularprom(notas), notas )


# crear una funcion para poder 
#validar si un input es numero

nota=input("ingresa la nota ").isdigit()

if nota:
    print("")


