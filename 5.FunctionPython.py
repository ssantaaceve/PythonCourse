str # Transforma en string

prueba1 = 1
conve1 = str (prueba1)
print(conve1)
print(type(conve1))

int # Transforma en entero

prueba2 = "2"
conve2 = int (prueba2)
print(conve2)
print(type(conve2))

abs # da la media

edasSergio = 18
edadMonica = 27
edadSantiago =25
promedio = abs (edasSergio + edadSantiago + edadMonica)
print (promedio) # revisar  coomo es el uso de este 

#Funciones Str
len #Cuenta el numero de caracteres de la cadena de texto
texto1 = "sergio"
print(len(texto1))

texto2 = "sergio"
print(texto2.capitalize())  #Pone la primera letra en mayuscula
print(texto2.upper()) #Convierte en mayuscula todo
print(texto2.count("S")) #Cuenta cuantas veces esta el caracter mencionado
print(texto2.isnumeric()) #Valida si es numerico resultado False
print(texto2.lower()) #convierte todo en miniscula
print(texto2.isupper()) #Valida si todo esta es mayucula, true o false
print(texto2.startswith("se")) #Valida que la palabra empiece con se o el caracter indicado