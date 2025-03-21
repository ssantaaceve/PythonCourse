#las funciones se definen con la palabra reservada DEF

'''def suma_de_valores (firts_number, second_number):
    print (firts_number + second_number)'''

'''suma_de_valores(3, 5) #se llamada la variable '''

#En este caso la funcion recibe parametros pero tambien los puede retornar


def sum_values_with_return (first_value, second_value):
    return first_value + second_value

my_result = sum_values_with_return (10, 5)
print (my_result)


### Ojo en este caso cuando vamos a llamar a la funcion, lo llamanos dentro de una variable y tendremos como resultado un variable con un valor que depende de un afuncion


while True:
    nombre = input('what is your name bro')
    apellido = input('what is your last name')
    def este_es_tu_nombre (nombre, apellido):
        return (f'el nombre del cliente es: {nombre} y su apellido es {apellido}')

    Nombre_del_cliente = este_es_tu_nombre(nombre, apellido)
    print (Nombre_del_cliente)
    if nombre !='Sergio':
        continue
    else:
        break



print ("The name is Sergio ALERTA")





    