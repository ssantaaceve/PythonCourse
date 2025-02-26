#Ejercicio 1
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

age = int(input('how old are you  '))

if age >= 18:
    print (f'this person is {age} years old, so he is allowed to drink a lot.')
else:
    print(f'this person is {age} years old,  so this guy has to stay at home.')



#Ejercicio 2
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

password = input ('type your password: ')
password_save = password.upper()


def password_validation (x):
    if x == password_save:
        print ('you are sign in')
    else: 
        print ('sorry, try again')
        
Password_val = input('type your password to sign in ')
password_validation (Password_val.upper())





#Ejercicio 3
#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.


value_1 = float(input('Type the first number: '))
value_2 = float(input('Type the second number: '))

if value_2 == 0:
    print('Sorry, my friend, you cannot perform that operation. Please try again with a value greater than zero.')
else:
    operation = value_1 / value_2
    print(f'The result of your operation is {operation}')





#Ejercicio 4
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

numero = int(input('escribe aquí tu número'))

if numero % 2 != 0:
    print ('el número es impar')
else:
    print ('el número es par')



#Ejercicio 5
#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

age_user = int(input('how old are you? '))
incomes = int(input('how much money did you earn last year? '))

incomes_monthly = incomes/12

if incomes > 16 and incomes_monthly >= 1000:
    print ('you have to pay taxes from last year')
else:
    print ("you don't have to pay taxes from last year")


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

##Ejercicio 7
##Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
#Renta	Tipo impositivo
#Menos de 10000€	5%
#Entre 10000€ y 20000€	15%
#Entre 20000€ y 35000€	20%
#Entre 35000€ y 60000€	30%
#Más de 60000€	45%

##Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

Earnings_annual = int(input('how much monind did you earn the last year?'))

if Earnings_annual < 10000:
    print (f'You have tu par a 5% of the total of your earnings. so you will pay {Earnings_annual * 0.05}')
elif  10000 <= Earnings_annual < 20000:
    print (f'You have tu par a 15% of the total of your earnings. so you will pay {Earnings_annual * 0.15}')
elif  20000 <= Earnings_annual < 35000:
    print (f'You have tu par a 20% of the total of your earnings. so you will pay {Earnings_annual * 0.20}')
elif  35000 <= Earnings_annual < 60000:
    print (f'You have tu par a 30% of the total of your earnings. so you will pay {Earnings_annual * 0.30}')
elif  Earnings_annual >=20000:
    print (f'You have tu par a 45% of the total of your earnings. so you will pay {Earnings_annual * 0.45}')

##Ejercicio 8
#En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
#Nivel	Puntuación
#Inaceptable	0.0
#Aceptable	0.4
#Meritorio	0.6 o más
#Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.


start =  input('Would you like to start te program? ')# Solicito informaciond el usuario

if start.upper() == 'SI': # Creo condicionar para empezar programa dependiendo de la respuesta de usuario, en el caso de no ser 'si' el sistema ejecutara el else de este condicional 'try again';
    def process_qualificatiopn (): #Creo una funcion por si el  usuario pone un valor erroneo el sistema se repita hasta que se diligencien los valores aceptados
        option = float(input ('elige una opcion entre 0.0(Inaceptable) 0.4(Aceptable) 0.6 o mas (Meritorio) para tu trabajador')) # ojo con el cambio del tipo de la variable (CASTING) para que corra el programa
        if  option ==0.0:
            return print(f'Your worker will earn an amount of {2400 * option}, because their qualification was {option}.')
        elif option ==0.4:
            return print(f'Your worker will earn an amount of {2400 * option}, because their qualification was {option}.')
        elif option >= 0.6: 
            return print(f'Your worker will earn an amount of {2400 * option}, because their qualification was {option}.')
        else:# Con este comando condiciono al programa a que se repita si no se diligencian los valores establecidos
            print('you have to put "0.0", "0.4", "0.6"')
            process_qualificatiopn ()
    Final_qualification = process_qualificatiopn ()
    print (Final_qualification)
else: 
    print ('try again')


##Ejercicio 9
##Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

age_user = int(input('Please, can you type your age before you go inside the playroom: '))

if age_user < 4:
    print('You can go in for free')
elif 4 <= age_user <= 18:
    print('You can go in after you pay the amount of 5 euros')
else:
    print('You can go in after you pay the amount of 10 euros')

#Ejercicio 10
#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.  
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.


def pizza_program():
    while True:
        option = input("What kind of pizza would you like today?\n(1) Vegetarian\n(2) Non-Vegetarian\nPlease choose 1 or 2: ")

        if option == '1':
            print("You have selected Vegetarian Pizza.")
            ingredients = input("Now, please select one of these ingredients:\n(1) Pimienta\n(2) Tofu\nChoose 1 or 2: ")
            
            if ingredients == '1':
                print("You have selected Pimienta.\nYour pizza will have pimienta, mozzarella, and tomato.")
            elif ingredients == '2':
                print("You have selected Tofu.\nYour pizza will have tofu, mozzarella, and tomato.")
            else:
                print("Invalid choice. Please select a valid ingredient.")
                continue  # Repite el bucle si la opción no es válida
            
        elif option == '2':
            print("You have selected Non-Vegetarian Pizza.")
            ingredients = input("Now, please select one of these ingredients:\n(1) Pepperoni\n(2) Ham\n(3) Salmon\nChoose 1, 2, or 3: ")
            
            if ingredients == '1':
                print("You have selected Pepperoni.\nYour pizza will have pepperoni, mozzarella, and tomato.")
            elif ingredients == '2':
                print("You have selected Ham.\nYour pizza will have ham, mozzarella, and tomato.")
            elif ingredients == '3':
                print("You have selected Salmon.\nYour pizza will have salmon, mozzarella, and tomato.")
            else:
                print("Invalid choice. Please select a valid ingredient.")
                continue  # Repite el bucle si la opción no es válida

        else:
            print("Invalid option. Please choose either 1 or 2.")
            continue  # Repite el bucle si la opción no es válida
        
        # Preguntar si desea elegir otra pizza
        replay = input("Would you like to choose again? (yes/no): ").strip().lower()
        if replay != 'yes':
            print("Thank you for using the pizza program!")
            break  # Sale del bucle si el usuario no quiere repetir

# Ejecutar el programa
pizza_program()

