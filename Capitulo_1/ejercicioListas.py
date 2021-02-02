# ejemplo de uso de listas

print("Ejemplo de uso de listas")

# declaracion de lista 
lista1=[10,15,15,17,14]
lista2=["María","Pepe","Marta","Antonio"]
lista3=["uno",4,True,"gorro"]


# ejemplos de salida de datos de listas
print(lista1[1:]) # desde el elemento 1 hasta el final
print(lista1[1]) # solo el elemento 1
print(lista2[0:3]) # del elemento 0 hasta el 2
print("lista 3=",lista3)


#agregar elememtos a la lista 

lista1.append(25.48)
print(lista1)

lista2.append("Olegario") # se inserta el final
print(lista2)

#introduccion con indice en una posición determinada
lista1.insert(2,-25.48) # se inserta un valor en la posion 2
print(lista1)

# extender la lista al final con otra lista
lista2.extend(["Mixo","Mixi","Luna","Copito","Pinky","Pongo"])
print(lista2)

# para saber el indice en el que está un elemento
print(lista2.index("Mixi"))

# comprobar si un elemento está en una lista
print("Luna" in lista2)

# eliminar elementos de una lista mediente la nominacion
lista2.remove("Marta")
print(lista2)

# eliminar elementos del final de la lista
lista2.pop()
print(lista2)

# sumar listas
lista2=lista2+lista3
print(lista2)
