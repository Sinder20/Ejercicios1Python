#  	1. Hacer un programa que imprima los numeros impares hasta el 100 y que imprima cuantos impares hay

k=0
for i in range(1, 101):
    if i%2!=0:
        print(i)
        k=k+1

print("Cantidad de Números impares:",k)