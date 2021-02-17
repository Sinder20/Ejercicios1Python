#  	9. Crear una lista aleatoria de 10 numeros, partiendo del numero ingresado por el usuario

import random

num=int(input("Ingrese un número para iniciar con la lista aleatoria: "))

contador=0
lista=[num]

while contador<=8:
    lista.append(random.randint(0,50))
    contador+=1


print(lista)