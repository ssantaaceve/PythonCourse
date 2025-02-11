
#Ejercicio 1
#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
nombre_usuario, numero_entero= input('cual es tu nombre: '), input ('dime el número de veces que quieras que se repita tu nombre: ')
print ((nombre_usuario + "\n") * int(numero_entero)) # \n es el salto de linea 

#Ejercicio 2
# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

nombre_completo = input('dame tu nombre completo : ')

print (nombre_completo.upper())
print (nombre_completo.lower())
print (nombre_completo.title()) 

#Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
name = input ('escribe tu nombre')
print (f'tu nombre {name} tiene {len(name)}' + '\n' + ' letras')

#Ejercicio 4
# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

numero_telefono = (input('Cual es tu número de teléfono? Escribelo en formato +xx-xxxxxxxxx-xx: '))
Ajuste_texto = numero_telefono[4:-3]
print(Ajuste_texto)

#Ejercio 5
#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

frase = input('escribe la frase que quieras')
print (frase[::-1]) 

#Ejercicio 6
#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

frase_consola = input ('escribe una frase: ')
vocal_consola = input ('escribe una vocal: ')
print(f'La frase que escribrio el usuario es "{frase_consola} "y la vocal que escribió es: {vocal_consola.upper()}')


info_correo = print('cuál es tu correo?: ')
print (info_correo[:info_correo.find('@')])



#Ejercicio 9
#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

date_of_birthday = input('En qué fecha naciste? escribe tu respuesta con el siguiente formato dd/mm/aaaa:  ')

if len(date_of_birthday) != 10:
    day, month, year = date_of_birthday.split('/')
    print (f'la fecha de nacimiento es \n DÍA: {day.zfill(2)}\n MES: {month.zfill(2)} \n AÑO: {year}')
else:
    print (f'la fecha de nacimiento es \n DÍA:{date_of_birthday[:2]} \n MES: {date_of_birthday[3:5]}  \n AÑO: {date_of_birthday[-4:]}')





#Ejercicio 10
#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

productos_de_compra = input('menciona los productos comporados y recuerda poner una coma (,) por cada prodcuto: ')

print(productos_de_compra.replace(',', '\n'))










#Ejercicio 11
#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

nombre_producto = input('cuál es el nombre del producto?: ')
precio_producto = float(input('cuál es el precio del producto?: '))
Cantidad_unidades = int(input('cuál es la cantidad  del producto?: '))


costo_productos= precio_producto * Cantidad_unidades

print (f'el producto {nombre_producto} tiene un precio de {precio_producto:6.2f} y se vendieren un total de {Cantidad_unidades} unidades. lo que quiere decir que el costo total del lote vendido es: {costo_productos:8.2f} ')