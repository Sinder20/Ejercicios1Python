#  	3. Introducir un numero por teclado. Que nos diga si es par o impar

num= int(input("Ingrese un número entero: "))

if num%2!=0:
    print("El número " + "'"+str(num) + "'" + " que ingresó es 'IMPAR'")
else:
    print("El número "+str(num)+" que ingresó es 'PAR'")