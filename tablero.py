#Ejercicio 6
#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

student_name = input('what is your name?  ')
def elegir_opcion():
    option = input("Elige una opción (1 o 2):\n1. male \n2. female \n")
    if option == '1':
        return 'male'
    elif option == '2':
        return 'female'
    else:
        print("Opción no válida. Por favor elige 1 o 2.")
gender = elegir_opcion()
letter = student_name[0]

if  letter.lower() in 'abcdefghijkl' and gender == 'female':
    print (f'Your name starts with a letter between A and L ({letter}) \nand you are a {gender}. \nYour group would be THE GROUP A.')
elif letter.lower() in 'opqrstucwxyz' and gender == 'male':
    print (f'Your name starts with a letter between P and Z ({letter}) \nand you are a {gender}. \nYour group would be THE GROUP A.')
else: 
    print (f'Your name not starts with a letter ({letter}) \nand you are a {gender}. \nsergioYour group would be THE GROUP B.')