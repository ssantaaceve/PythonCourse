mi_string = "Este es mi string"
print(mi_string)

#Tambien puedes hacer saltos de linea con el string
mi_string_con_salto = "Este es mi string \n salto de linea"
print(mi_string_con_salto) #Esto quiere decir que despues del\n se hace un enter en el texto

mi_string_con_tabulacio = "\tEste es mi string  salto de linea"
print(mi_string_con_tabulacio) #Esto quiere decir que despues del\t de hace un sangria



name, apellido, edad = "sergio", "santa", 27
print ("mi nombre es {} {} y mi edad es {} ".format(name, apellido, edad)) #En este caso llama el valor de las variables solo indicando el espacio con {}
print ("mi nombre es %s %s y mi edad es  %d " %(name, apellido, edad)) #En este caso llamo el valor de la variables referencianado con %s ste y %d int
print ("mi nombre es" + name + " " + apellido + " " + "y mi edad es" + " " + str(edad)) #mas dificil y demorado
print (f"mi nombre es {name} {apellido} y mi edad es {edad}") #Con esta es mas facil y rapido importante la f



#desemaquetado de caracteres
language = 'python'
a, b, c, d, e, f = language
print(a)
print(b)
#Ojo, en este caso estas descomponiendo el string. por eso cuando llamar a lengauge es importante que esten el numero de variables acordes a la cantidad de caracteres 


#Division
langugage_slice = language[1:3]
print(langugage_slice) #Me imprime de la palabra pyhon la y t 

langugage_reverse = language[::-1]
print(langugage_reverse) #Esto pone al reves la palabra



b = "Hello, World!"
print(b[2:])

for x in "banana":
  print(x)