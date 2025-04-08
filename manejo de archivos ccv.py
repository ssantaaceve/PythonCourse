import csv

#leer un archivo
with open ('products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(csv_reader)