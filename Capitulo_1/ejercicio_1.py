# pruebas con python


print("Hola mundo")

# entrada de los datos numericos enteros
print("Introduce dos números enteros ")
dato1=int(input("Introduce el dato 1 "))
dato2=int(input("Introduce el dato 2 "))


if(dato1>dato2):
    print("dato1=",dato1," es mayor o igual que dato2=",dato2)
elif(dato1==dato2):
    print("dato1=",dato1," es igual que dato2=",dato2)
else:
    print("dato1=",dato1," es menor que dato2=",dato2)

#operaciones basicas
print("Cálculos realizados")
print("La suma de ",dato1," y de ",dato2," es ",dato1+dato2)
print("El producto de ",dato1," y de ",dato2," es ",dato1*dato2)
print("La diferencia de ",dato1," y de ",dato2," es ",dato1-dato2)
print("La división real de ",dato1," y de ",dato2," es ",dato1/dato2)
print("La division entera de ",dato1," y de ",dato2," es ",dato1//dato2)
print("El resto de la division entera de ",dato1," y de ",dato2," es ",dato1%dato2)
print("La potencia de  ",dato1," elevada a  ",dato2," es ",dato1**dato2)


