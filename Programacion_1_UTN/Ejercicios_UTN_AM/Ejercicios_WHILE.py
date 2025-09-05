#Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.
contador =1
while contador<=10:
    print (contador)
    contador+=1
#Mostrar 10 repeticiones de números descendentes desde el 10 al 1.
contador = 10
while contador >=1:
    print (contador)
    contador-=1
#Mostrar la suma de los números desde el 1 hasta el 10.
contador =1
while contador <= 10:
    print (f"{contador}+0={contador}")
    contador+=1 
#Mostrar la suma de los números pares desde el 1 hasta el 10.
contador=0
while contador<=10:
    if contador%2==0:
        print (f"{contador}+0={contador}")
    contador+=1
#Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.

contador = 0
acumulador =0 
while contador<5:
    numero = float(input("Ingrese un numero: "))
    acumulador+=numero
    contador+=1
promedio=acumulador/contador

print (f"Suma de los numeros: {acumulador}\nPromedio de los mismos es de {promedio}")
#Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.
acumulador =0
contador =0
flag_inicio=True
while flag_inicio:
    numero= float(input(f"\nIngrese un numero: "))
    contador +=1
    acumulador += numero
    while True:
        continuar = str(input(f"\nDesea continuar ingresando datos?(Y/N) "))
        if continuar == "y" or continuar =="Y":
            print ("\nDe acuerdo continuemos.\n")
            break
        elif continuar =="N" or continuar =="n":
            print("\nPerfecto en ese caso, calculemos el promedio de todos los datos ingresados\n")
            flag_inicio=False
            break
        else:
            print(f"\nDisculpa no entendi.")
promedio = acumulador /contador
print (f"Suma de los numeros: {acumulador}\nPromedio de los mismos es de {promedio}")
#Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.
acumulador_positivo =0
acumulador_negativo =0
flag_inicio=True
while flag_inicio:
    numero= float(input(f"\nIngrese un numero: "))
    if numero>0:
        acumulador_positivo += numero
    else:
        acumulador_negativo+=numero
    while True:
        continuar = str(input(f"\nDesea continuar ingresando datos?(Y/N) "))
        if continuar == "y" or continuar =="Y":
            print ("\nDe acuerdo continuemos.\n")
            break
        elif continuar =="N" or continuar =="n":
            print("\nPerfecto en ese caso, calculemos el promedio de todos los datos ingresados\n")
            flag_inicio=False
            break
        else:
            print(f"\nDisculpa no entendi.")
print(f"Producto de la suma de los numeros:\nPositivos = {acumulador_positivo}\nNegativos = {acumulador_negativo}")
#Ingresar 10 números enteros. Determinar el máximo y el mínimo.
contador =1
while contador <=10:
    numero= int (input(f"\nIngrese numeros{contador}/10: "))
    if contador ==1:
        maximo = numero
        minimo = numero    
    elif maximo<numero:
        maximo = numero
    elif minimo>numero:
        minimo = numero
    contador += 1
print  (f"Maximo = {maximo}\nMinimo = {minimo}")
    
#Anexo:
#Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y el promedio de los mismos.
contador = 0
acumulador = 0 
flag_inicio=True
while flag_inicio:
    numero=float(input(f"Ingrese un numero: "))
    contador += 1
    acumulador+= numero
    if contador >=5:
        while True:
            continuar = str(input(f"\nDesea continuar ingresando datos?(Y/N) "))
            if continuar == "y" or continuar =="Y":
                print ("\nDe acuerdo continuemos.\n")
                break
            elif continuar =="N" or continuar =="n":
                print("\nPerfecto en ese caso, calculemos el promedio de todos los datos ingresados\n")
                flag_inicio=False
                break
            else:
                print(f"\nDisculpa no entendi.")
promedio = acumulador/contador
print (f"Datos:\nCantiddad de datos ingresados: {contador}\nTotal acumulado: {acumulador}\nPromedio: {promedio}")
#Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los números ingresados y el promedio de los mismos.
contador = 1
acumulador = 0 
flag_inicio=True
while flag_inicio:
    numero=float(input(f"Ingrese un numero: "))
    contador += 1
    acumulador+= numero
    if contador >=5 and contador <=10:
        while True:
            continuar = str(input(f"\nDesea continuar ingresando datos?(Y/N) "))
            if continuar == "y" or continuar =="Y":
                print ("\nDe acuerdo continuemos.\n")
                break
            elif continuar =="N" or continuar =="n":
                print("\nPerfecto en ese caso, calculemos el promedio de todos los datos ingresados\n")
                flag_inicio=False
                break
            else:
                print(f"\nDisculpa no entendi.")
promedio = acumulador/contador
print (f"Datos:\nCantiddad de datos ingresados: {contador}\nTotal acumulado: {acumulador}\nPromedio: {promedio}")
#Integrador While
#Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:
#La suma acumulada de los números negativos.
#La suma acumulada de los números positivos.
#La cantidad de números negativos ingresados.
#El promedio de los números positivos.
#El número positivo más grande.
#El porcentaje de números negativos ingresados, respecto del total de ingresos.
