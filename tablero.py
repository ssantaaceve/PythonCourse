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

