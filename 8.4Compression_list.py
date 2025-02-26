#Una Comprehension List es una forma concisa de crear listas en Python, pues permite generar listas nuevas transformando cada elemento de una colección existente o creando elementos a partir de un rango. La sintaxis es compacta y directa, lo que facilita la comprensión del propósito de tu código de un vistazo.


# El expreso de python, breves rapidas y potentes


# podemos creear listas utilizando una lina de codigo

# Utilizacion del if y el for

squares = [x**2 for x in range(1, 11)]
#print ('los cuadrados son', squares)#Se debe poner en este tipo de conetenedores

celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) *32 for temp in celsius]
print (fahrenheit)
# importante tener en cuenta que se establece una variables y luego se opera esa variable en un ciclo for para todos los casos que se escohan en un rango o se mencionen en una variable


evens = [x for x in range(1,21) if x%2 ==0]
print(evens)
