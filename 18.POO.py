#La Programación Orientada a Objetos es un paradigma de programación que organiza el diseño del software en torno a objetos. Los objetos son instancias de clases, que pueden tener atributos (datos) y métodos (funciones).


class person:
    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName

    def greet (self):
        print (f'hola mi nombre es {self.name} {self.lastName }')


SaldoPrimerObjeto = person('Ana', 'Gabriela')
SaldoPrimerObjeto.greet()        