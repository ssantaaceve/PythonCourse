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