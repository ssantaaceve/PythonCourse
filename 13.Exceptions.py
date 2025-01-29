### Exception Handling ###
numberone, numbertwo =5, "1"
try: #Obligarotio
    print (numberone+ numbertwo) #esto daría un error
except:#Obligarotio
    print ('se ha producido un error')#En este caso se produjo un error pero el programa continúa y salta ese error. 
else: #opcional
    print('la ejecución del código se mantiene')
finally: #opcional
    print ('se ha producido un error')