#Ejercicio 1
#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

palabra = input('type any word')

for i in range(0,10):
    print (palabra)

#Ejercicio 2
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

age_user = int(input('type your age'))

for i in range (0,age_user):
    print (i + 1)


#Ejercicio 3
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

numero_user = int(input('type any positive number '))
for i in range (0, numero_user):
    if i % 2 !=0:
        print(f'{i}, ')


#Ejercicio 4
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas


num = int(input('Escribe un número entero positivo: '))

for i in range (num, -1, -1):
    print(f'{i},')
