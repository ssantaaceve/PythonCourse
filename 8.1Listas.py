### Listas o arrays###
My_list = list()
My_other_lis = []
#nuestra lista vine siendo una caja que almacena información
#En este caso nos cuenta longitud de my_list; la posicion es 0


My_list = [35,24,62,52,30,30,17]
print(My_list)
print(len(My_list)) 
My_other_lis = [35, 1.77, 'sergio', 'santa']
print (type(My_other_lis))

print (My_other_lis[0]) #Comando para escoger un campo especificio del array, en este caso el campo 1 en programacion es el campo 0
print (My_other_lis[1])


print (My_other_lis.count(1.77)) # con este comando contamos cuantas veces se repite el dato especificado en el array

print (My_list + My_other_lis) #En este caso se suma todas las variables sumando los campos 


My_other_lis.insert (1, "azul")
print(My_other_lis) #inserta un dato en la posicion 1 y corre los demas datos hacia adelantante

My_other_lis.append ("sergio")
print(My_other_lis) #inserta un dato en la ultima posicion

My_other_lis.remove ("sergio")
print(My_other_lis) #inserta un dato en la ultima posicion

## Python Collections (Arrays)
## There are four collection data types in the Python programming language:

## List is a collection which is ordered and changeable. Allows duplicate members.
## Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
## Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
## Dictionary is a collection which is ordered** and changeable. No duplicate members.

# Creación de listas
lista_vacia = []
lista_numeros = [1, 2, 3, 4, 5]
lista_mixta = [1, "dos", 3.0, True]

print("Lista vacía:", lista_vacia)
print("Lista de números:", lista_numeros)
print("Lista mixta:", lista_mixta)

# Acceder a elementos
print("\nAcceso a elementos")
print("Primer elemento:", lista_numeros[0])
print("Último elemento:", lista_numeros[-1])

# Modificar elementos
print("\nModificar elementos")
lista_numeros[0] = 10
print("Lista de números modificada:", lista_numeros)

# Agregar y eliminar elementos
print("\nAgregar y eliminar elementos")
lista_numeros.append(6)
print("Lista después de append:", lista_numeros)
lista_numeros.insert(2, 99)
print("Lista después de insert:", lista_numeros)
lista_numeros.remove(99)
print("Lista después de remove:", lista_numeros)
ultimo = lista_numeros.pop()
print("Elemento eliminado con pop:", ultimo)
print("Lista después de pop:", lista_numeros)
elemento = lista_numeros.pop(1)
print("Elemento eliminado en la posición 1:", elemento)
print("Lista después de eliminar en la posición 1:", lista_numeros)

# Operaciones básicas
print("\nOperaciones básicas")
lista_concatenada = lista_numeros + lista_mixta
print("Lista concatenada:", lista_concatenada)
lista_repetida = lista_numeros * 2
print("Lista repetida:", lista_repetida)
print("¿Está 3 en la lista?", 3 in lista_numeros)
print("Longitud de la lista:", len(lista_numeros))

# Iteración sobre los elementos de una lista
print("\nIteración sobre elementos de la lista")
for elemento in lista_numeros:
    print(elemento)

# Salida final
print("\nGracias por utilizar el programa de listas. ¡Hasta la próxima!")

# Creación de listas

listavacia = []

listanumeros = [1, 2, 3, 4, 5]

listamixta = [1, "dos", 3.0, True]



print("Lista vacía:", listavacia)

print("Lista de números:", listanumeros)

print("Lista mixta:", listamixta)



# Acceder a elementos

print("\nAcceso a elementos")

print("Primer elemento:", listanumeros[0])

print("Último elemento:", listanumeros[-1])



# Modificar elementos

print("\nModificar elementos")

listanumeros[0] = 10

print("Lista de números modificada:", listanumeros)



# Agregar y eliminar elementos

print("\nAgregar y eliminar elementos")

listanumeros.append(6)

print("Lista después de append:", listanumeros)

listanumeros.insert(2, 99)

print("Lista después de insert:", listanumeros)

listanumeros.remove(99)

print("Lista después de remove:", listanumeros)

ultimo = listanumeros.pop()

print("Elemento eliminado con pop:", ultimo)

print("Lista después de pop:", listanumeros)

elemento = listanumeros.pop(1)

print("Elemento eliminado en la posición 1:", elemento)

print("Lista después de eliminar en la posición 1:", listanumeros)



# Operaciones básicas

print("\nOperaciones básicas")

listaconcatenada = listanumeros + listamixta

print("Lista concatenada:", listaconcatenada)

listarepetida = listanumeros * 2

print("Lista repetida:", listarepetida)

print("¿Está 3 en la lista?", 3 in listanumeros)

print("Longitud de la lista:", len(listanumeros))

