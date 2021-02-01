# Trabajar con numeros enteros

# definicion de las funciones
def presentacion():
    print("Programa de ejemplo de operaciones de numeros enteros")


def operaciones(dato1,dato2):
    #operaciones basicas
    print("Cálculos realizados")
    print("La suma de ",dato1," y de ",dato2," es ",dato1+dato2)
    print("El producto de ",dato1," y de ",dato2," es ",dato1*dato2)
    print("La diferencia de ",dato1," y de ",dato2," es ",dato1-dato2)
    print("La división real de ",dato1," y de ",dato2," es ",dato1/dato2)
    print("La division entera de ",dato1," y de ",dato2," es ",dato1//dato2)
    print("El resto de la division entera de ",dato1," y de ",dato2," es ",dato1%dato2)
    print("La potencia de  ",dato1," elevada a  ",dato2," es ",dato1**dato2)


def compara(dato1,dato2):
    # funcion de comparacion de los dos datos que se han introducido
    if(dato1>dato2):
        print("dato1=",dato1," es mayor que dato2=",dato2)
    elif(dato1==dato2):
        print("dato1=",dato1," es igual que dato2=",dato2)
    else:
        print("dato1=",dato1," es menor que dato2=",dato2)


def determinaTipo(dato1,dato2):
    # determinacion del tipo de dato
    print("El dato ",dato1," es de tipo ",type(dato1))
    print("El dato ",dato2," es de tipo ",type(dato2))

def parImpar(dato):
    # comprobación de si el numero es par o impar
    if(dato%2==0):
        print("El valor ",dato," es par")
    else:
        print("El valor ",dato," es impar")


# Inicio del programa
presentacion()

# entrada de los datos numericos enteros
print("Introduce dos números enteros ")
dato1=int(input("Introduce el dato 1 "))
dato2=int(input("Introduce el dato 2 "))

# determinar el tipo de los datos
#determinaTipo(dato1,dato2)

# control de paridad de los numeros introducidos
parImpar(dato1)
parImpar(dato2)

# Compara los dos datos
compara(dato1,dato2)


# Llamado a la función
operaciones(dato1,dato2)




