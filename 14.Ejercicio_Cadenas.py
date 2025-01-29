
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





