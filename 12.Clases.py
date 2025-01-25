### Clases ##
'''Lo ideal de las clases es que se identifiquen los codigos dentro de un ambito de actuaciin en donde tenga sentido el codigo

Esto queire decir que en la clase deben haber cosas que corresponden a esa funcion de la claes ejmplo

Clase persona: debe haber infomacion en esta clase sobre nombre, apellio, edad, profesion etc... no puede haber codigo relacionado con carros por que no es el objeto de la clase en especifico
'''


'''class person:
    def __init__(self, name, surname): #contructor de clae. con esto se tendra la capacaidad para que la clase revisa un parametro
        self.name = name #self tiene un propiedad que se llama name
        self.surname = surname

my_person = person('sergio', 'santa')
print (f'{my_person.name} y su apellido es {my_person.surname}')'''


class person:
    def __init__(self, name, surname): #contructor de clae. con esto se tendra la capacaidad para que la clase revisa un parametro
        self.full_name = f'{name} {surname}'
        # La propiedad puede ser cualquier nombre, lo que importa es que llames los parametros/ Similar a las funciones
    def walk (self):
        print(f'{self.full_name}')

my_person = person('sergio', 'santa')
print (my_person.full_name)
my_person.walk()