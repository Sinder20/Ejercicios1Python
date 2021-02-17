# 	8. Realizar la tabla de multiplicar de un numero entre 0 y 10
print("* * * Programa que muestra la tabla de multiplicar de un número entre 0 y 10 * * *")

comprobar= True

while comprobar==True:

    num=int(input("Ingrese un número entre 0 y 10 de la tabla que desea: "))

    if num>=0 and num<=10:

        for i in range(11):
            print(num, "*", i, "=", num*i)

            comprobar = False

    else:
        print("El número ingresado no es correcto. Inténtelo nuevamente.")