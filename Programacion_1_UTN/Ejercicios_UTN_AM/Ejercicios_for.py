#For
#
#Mostrar los números ascendentes desde el 1 al 10
for i in range(10):
    print (f"{i+1}")
#Mostrar los números descendentes desde el 10 al 1
for i in range (10,0,-1):
    print (f"{i}")
#Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.
num = int(input(f"Ingrese un numero: "))
for i in range (0,num+1):
    print (i)
#Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:
#
	#5 x 0 = 0
	#5 x 1  = 5
	#5 x 2 = 10
	#5 x 3  = 15 …
num=int (input(f"Ingrese un numero: "))
for i in range (11):
    print(f"{num} x {i} = {num*i}")
#Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.
acumulador = 0
for i in range (1,11):
    num=float (input(f"\nIngrese un numero (para finalizar el proceso antes de tiempo ingrese 0): "))
    acumulador+=num
    if num == 0:
        print (f"\nFinalizando proceso")
        i-=1
        break
promedio = acumulador/ i
print (f"Datos esenciales:\nSuma de numeros ingresados: {acumulador}\nPromedio de los numeros ingresados: {promedio}")
#Imprimir los números múltiplos de 3 entre el 1 y el 10.
for i in range (10):
    if i%3==0:
        print (i)
        
#Mostrar los números pares que hay desde la unidad hasta el número 50.
for i in range (50):
    if i%2==0:
        print (i)
#Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:
#
#
#Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.
#Ingresar un número. Determinar si el número es primo o no.
#Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.
