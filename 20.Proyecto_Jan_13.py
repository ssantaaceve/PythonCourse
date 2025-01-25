###Ejercicio 1
'''print ('hola mundo')'''

#Ejercicio 2
'''Saludo = 'Hola mundo'
print (Saludo)'''

#Ejercicio 3

'''nombre = input('escribe tu nombre bro')
profesion = input('Escribe que quieres rey')
print (f'Mi nombre es {nombre} y quiero ser {profesion}') '''


#Ejercicio 4
'''suma = 3 + 2
producto = 2*5 

print ((suma/producto)**2) '''

#Ejercicio 5
'''horas = input('cuántas horas trabajaste?')
valor_hora = input ('cuál es el precio que tiene la hora?')

print (int(horas) * int(valor_hora))'''

#ejercicio 6

'''variable_n = (int(input('Variable n: ')) + 1)

for i in range(1, variable_n):
    sumatoria = (i * (i+1))/2
    print (f'sumar rango 1 a n es {sumatoria}')'''



#ejercicio 7

'''usuario_peso = input('dame tu peso en kg')
usuario_estatura = input('dame tu estatura')

indice_masa_corporal = float(usuario_peso)/(float(usuario_estatura))**2
print (f'tu índice de masa corporal es {indice_masa_corporal}')


peso = input("¿Cuál es tu peso en kg? ")
estatura = input("¿Cuál es tu estatura en metros?")
imc = round(float(peso)/float(estatura)**2,2)
print("Tu índice de masa corporal es " + str(imc)) '''



## Ejercicio 7 

'''Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales. '''


# Ejercicio 8

'''Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.'''

'''var1 = 5
var2 = 2

print (var1/var2) # = 2.5 
print (var1//var2) # = 2 Cociente: parte entera de la división
print (var1%var2) # = 1 Resto:lo que sobra de la división '''


'''dividendo = int(input ('dividendeo'))
divisor = int(input ('divisor'))

resto = dividendo % divisor
cociente = dividendo // divisor
division = dividendo/divisor

print(f'{dividendo} entre {divisor} da un cociente de {cociente} y un resto de {resto} donde {dividendo} y {divisor} son los números introducidos por el usuario, y {cociente} y {resto} son el cociente y el resto de la división entera respectivamente')
'''

'''Ejercicio 9
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.'''





'''def calculo_Capital (x, y, z):
     return ((x * y) + x) * z

Cantidad_Inversion = int(input('cuánto vas a invertir'))
Interes_anual = float(input('Cuál es tasa anual: '))
Cantidad_de_años = int(input('cuántos años: '))
    
Resultado_final= calculo_Capital (Cantidad_Inversion, Interes_anual, Cantidad_de_años)

print (Resultado_final)


 

Cantidad = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años?"))
print("Capital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))  '''


'''Ejercicio 10
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.'''


'''def peso_total_lote(x,y):
    return (x * 112) + (y * 75)

Total_lote = peso_total_lote(int(input('Número de payasos vendidos')), int(input('Número de muñecas vendidas')))
print(Total_lote) '''


##Ejercicio 11
'''Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.'''

'''amount = int(input('digita el saldo de tu cuenta: '))
year = int(input('digita el número de años: '))
interest = float(input('digita el interes: '))

def Saldo_cuenta_de_ahorros(amount, year, interest):
    if year == 1:
        print(round(amount * (1 + interest / 100), 6))  # Interés compuesto para 1 año
    else:
        for i in range(1, year + 1):
            saldo = amount * (1 + interest / 100) ** i  # Fórmula de interés compuesto
            print(f"Año {i}: {round(saldo, 6)}")  # Mostrar saldo con 6 decimales

Saldo_cuenta_de_ahorros(amount, year, interest)




cantidad = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años?"))
print("Capital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))'''

#Ejercicio 12

'''Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.'''


Valor_pan = 3.49
Descuento_pan_viejo = 0.6
barras_bendidas = int(input('número de barras de pan viejo que bendiste: '))
print(f'Este es el precio habitual de una barra de pan {Valor_pan}, pero como el pan es viejo tendras un descuento del {Descuento_pan_viejo * 100}%. El costo del total de panes que compraste es {(Valor_pan*(1-Descuento_pan_viejo))*barras_bendidas}.')

