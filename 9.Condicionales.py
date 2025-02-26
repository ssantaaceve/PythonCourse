##Condicionales
## aplica para numeros
Variable = 2

if Variable > 4:
    print('si funciono')
elif Variable == 3:
    print('if especifico') 
else:
    print ('solo en caso de que nada de o anterior se cumpla')

print('no funciono')

## aplica para str
my_str = 'mi cadena de texto'
if my_str:
    print('mi cadena de texto no es vacia')

if my_str == 'mi cadena de texto':
    print ('mi cadena de texto cumple la cindición')

if my_str == 'mi cadena de texto':
    print ('mi cadena de texto cumple la cindición')

x = 2
y = 3

if x >2 and y <2: #Verdadero si y solo si  los dos se cumplen
    print('true')
else:
    print('false')

if x >2 or y <2: #Verdadero si uno de los dos es ver
    print('true')
else:
    print('false')


if not x >2: #Verdadero si uno de los dos es ver
    print('no es mayor que 2')
else:
    print('false')