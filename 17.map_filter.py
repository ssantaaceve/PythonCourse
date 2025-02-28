numero = int(input('dame un numero'))

numeros_impares = list(map(lambda x: 3*1, range(numero)))
print(numeros_impares)


numero2 = int(input('dame un numero'))

numeros_impares2 = list(filter(lambda x: x%2 !=0, range(numero2)))
print(numeros_impares2)