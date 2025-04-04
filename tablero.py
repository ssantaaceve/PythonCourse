#Ejercicio 9
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.


user_password = "123456"

def password_interfaz():
    while True:
        password = input("Type your password: ")
        if password == user_password:
            print("Access granted ✅")
            break
        else:
            print("Try again ❌")

password_interfaz()