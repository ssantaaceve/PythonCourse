#Ejercicio 8
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1


numero = int(input('Escribe un número entero positivo: '))

for i in range(1, numero + 1, 2):  # Inicia en 1 y se incrementa de 2 en 2
    for j in range(i, 0, -2):  # Imprime números de i a 1 en decremento de 2
        print(j, end=" ")  # Imprime los números en la misma línea
    print()  # Salto de línea después de cada fila