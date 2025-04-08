#podemos modificar trabajar y leer archivos fuera de python
#oko si el archivo esta dentro de esta cerpta python se puede llamar de esta forma, sino se tiene que llamar con todo el nombre de la ruta

'''with open('cuento.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())'''




#leer todas las lineas en una lista
with open ('cuento.txt', 'r') as file:
    lines = file.readlines()
    print (lines)