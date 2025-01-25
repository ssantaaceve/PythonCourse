### Exception Handling ###
numberone, numbertwo =5, "1"
try:
    print (numberone+ numbertwo) #esto daría un error
except:
    print (se ha producido un error')#En este caso se produjo un error pero el programa continúa y salta ese error. 
else: 
    print('la ejecución del código se mantiene')
finally: 
    print ('se ha producido un error')