import random
#1 Cargar y mostrar array:
#Declarar un array de 5 enteros. Cargarlo por teclado y mostrar su contenido por pantalla usando un
#ciclo for.
numeros_enteros =[0]*5
for i in range (len(numeros_enteros)):
    Dato = int (input("Ingrese numero: "))
    numeros_enteros [i] = Dato

print (f"Numeros enteros cargados: ")
for i in range (len(numeros_enteros)):
    print (f"[{numeros_enteros[i]}]")
#2. Sumar todos los elementos:
#Declarar un array de 10 enteros. Cargarlo por teclado. Calcular y mostrar la suma de todos los
#elementos.
array_entero = [0]*10
suma_de_elementos =0

for i in range (len(array_entero)):
    num = int (input("Ingrese el numero a cargar: "))
    array_entero [i] = num
    suma_de_elementos += array_entero [i]
print (f"suma de elementos del array {suma_de_elementos}")

#3. Promedio de valores:
#Declarar un array de 6 números reales (floats). Cargarlo por teclado. Calcular y mostrar el promedio
#de los valores.

array_eje_3 = [0]*6
acumulador = 0
for i in range (len (array_eje_3)):
    num= float (input("Ingrese numeros float: "))
    acumulador += num
    array_eje_3 [i]= num
print (f"Promedio {acumulador/len(array_eje_3)}")

#4. Contar mayores a un valor:
#Cargar un array de 8 enteros. Contar cuántos son mayores al valor 100 e informar el resultado.
array_eje4 = [0]*8
contador = 0
for i in range (len(array_eje4)):
    num = input ("Ingrese numeros: ")
    array_eje4 [i] = num
    if num > 100:
        contador += 1
print (f"Cantidad de numeros mayores a 100, ingresados es de {contador}")


#5. Buscar un valor:
#Cargar un array de 10 enteros. Solicitar al usuario un número y verificar si se encuentra en el array.
#Informar la posición en caso afirmativo, o indicar que no se encuentra.
FLAG = False

array_eje5 = [0]*10
for i in range (len(array_eje5)):
    if num == array_eje5[i]:
        donde = array_eje5 [i]
        FLAG=True
        break
if FLAG == True:
    print (f"se enconcontr en la posicion {donde} del array")   
else:
    print (f"No se encuentra")
           
#Mayor y su posición:
#Cargar un array de 7 números enteros. Determinar el valor más alto y en qué posición se
#encuentra.
array_eje6 =[0]*7

for i in range (len (array_eje6)):
    num = int (input("Cargar dato: "))
    array_eje6 [i] = num
    if i == 0:
        num_max = num
    elif num > num_max:
        num_max =num 
        donde = i+1
print (f"Numero mas alto: {num_max}\nPosicion: {donde}")           
#7. Invertir orden:
#Cargar un array de 6 enteros y mostrarlo invertido, es decir, desde el último al primero.
array_7 = [0]*6
for i in range (len (array_7)):
    num = int(input("Cargar datos: "))
    array_7 [i]= num
for i in range (len(array_7),-1,-1):
    print (f"{array_7[i]}") 
#8. Comparar dos arrays:
#Cargar dos arrays de 5 elementos cada uno. Comparar si ambos son iguales elemento a elemento
#y mostrar un mensaje indicando si son o no iguales.
array_8A = [0]*5
array_8B = [0]*5
for i in range (len(array_8A)): 
    num=int (input("Cargar datos para primer array: "))
    array_8A [i]=num
for i in range (len(array_8B)): 
    num=int (input("Cargar datos para primer array: "))
    array_8B [i]=num
contador = 0
for i in range (5):
    if array_8A [i] == array_8B[i]:
        contador +=1
if contador == 5:
    print (f"Comparten los mismos elementos")
#9. Intercambiar elementos pares por ceros:
#Cargar un array de 10 enteros. Reemplazar todos los elementos pares por cero y mostrar el array
#resultante.
array_9 = [0]*10
for i in range (len(array_9 )):
    num = int (input("Cargar datos: "))
    if num % 2 == 0:
        array_9[i]= 0
    array_9[i]=num
print (f"{array_9}")
#10. Función para buscar la primera aparición de un valor:
#Escribir una función que reciba un array de enteros y un número a buscar. La función debe retornar
#la posición de la primera aparición de ese número o -1 si no se encuentra.
