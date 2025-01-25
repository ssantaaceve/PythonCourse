'''Ejercicio 1
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido. 

nombre_usuario, numero_entero= input('cual es tu nombre: '), input ('dime el número de veces que quieras que se repita tu nombre: ')

print ((nombre_usuario + "\n") * int(numero_entero)) # \n es el salto de linea '''


'''Ejercicio 2
Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

nombre_completo = input('dame tu nombre completo : ')

print (nombre_completo.upper())
print (nombre_completo.lower())
print (nombre_completo.title()) 
'''

'''Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre. ''' 

name = input ('escribe tu nombre')
print (f'tu nombre {name} tiene {len(name)}' + '\n' + ' letras')