#  4. Hacer un programa que imprima el mayor y el menor de una serie de cinco numeros que vamos introduciendo por teclado
#  Por medio de if
'''num1= int(input("Ingrese el primer número: "))
num2= int(input("Ingrese el segundo número: "))
num3= int(input("Ingrese el tercer número: "))
num4= int(input("Ingrese el cuarto número: "))
num5= int(input("Ingrese el quinto número: "))

if num1<num2 and num1<num3 and num1<num4 and num1<num5:
    print("El número menor es: ", num1)
elif num2<num1 and num2<num3 and num2<num4 and num2<num5:
    print("El número menor es: ", num2)
elif num3<num1 and num3<num2 and num3<num4 and num3<num5:
    print("El número menor es: ", num3)
elif num4<num1 and num4<num2 and num4<num3 and num4<num5:
    print("El número menor es: ", num4)
elif num5<num1 and num5<num2 and num5<num3 and num5<num4:
    print("El número menor es: ", num5)

if num1>num2 and num1>num3 and num1>num4 and num1>num5:
    print("El número mayor es: ", num1)
elif num2>num1 and num2>num3 and num2>num4 and num2>num5:
    print("El número mayor es: ", num2)
elif num3>num1 and num3>num2 and num3>num4 and num3>num5:
    print("El número mayor es: ", num3)
elif num4>num1 and num4>num2 and num4>num3 and num4>num5:
    print("El número mayor es: ", num4)
elif num5>num1 and num5>num2 and num5>num3 and num5>num4:
    print("El número mayor es: ", num5) '''

#  Por medio de lista
lista = []
cantidad = int(input("¿Cuántos números deseas ingresar? "))
mayor= 0
menor= 0
i= 1

while(cantidad > 0):
    numero = int(input("Número #"+ str(i) +": "))
    lista.append(numero)
    i = i+1
    cantidad= cantidad - 1

mayor= max(lista)
menor= min(lista)

print("Los números que ingresó son: ", lista)
print("El número mayor es: ", mayor)
print("El número menor es: ", menor)