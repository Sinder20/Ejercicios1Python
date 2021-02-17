#  7. 	Hacer un programa que al ingresar un numero indique si es numero primo o no

print("* * * Programa que te dice si un número es primo o no * * *")
num= int(input("Ingrese un número: "))

if num>1:
    cont=0
    i=2
    while i<num and cont==0:
        resto=num%i
        if resto==0:
            cont+=1
        i+=1
    if cont==0:
        print("El {} es un número primo".format(num))
    else:
        print("El {} no es un número primo".format(num))
else:
    print("El {} no es un número primo".format(num))