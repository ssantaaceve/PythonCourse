#Ejercicio 8
#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

precio_producto = input('Cuál es el precio de ese producto en euros y dos decimales? ')

posicion_centimo = precio_producto.find('.') #Esto nos da la posición en donde empiezan los céntimos. 


print(f'El valor del producto es de {precio_producto[:posicion_centimo]} euros con {precio_producto[posicion_centimo +1:]} céntimos') #Para cortar parte derecha str [: n posición], para cortar parte izquierda [n posición +1:]




