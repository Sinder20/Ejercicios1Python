#  2. Hacer un programa que solo nos permita introducir S o N

op= str(input("Ingrese 'S' o 'N' (en mayúsculas): "))

if op=='S':
    print("Ustede escogió la opción: "+ op)
elif op=='N':
    print("Usted escogió la opción: "+ op)

else:
    print("Opción inválida")
