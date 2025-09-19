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

array_eje5 = [0]*10°
for i in range (len(array_eje5)):
    if num == array_eje5[i]:
        print (f"se enconcontr en la posicion {i} del array")
    else:
        print (f"No se encuentra")
        
           
#Cargar un array de 7 números enteros. D
#6. Mayor y su posición:eterminar el valor más alto y en qué posición se
#encuentra.
#7. Invertir orden:
#Cargar un array de 6 enteros y mostrarlo invertido, es decir, desde el último al primero.
#8. Comparar dos arrays:
#Cargar dos arrays de 5 elementos cada uno. Comparar si ambos son iguales elemento a elemento
#y mostrar un mensaje indicando si son o no iguales.
#9. Intercambiar elementos pares por ceros:
#Cargar un array de 10 enteros. Reemplazar todos los elementos pares por cero y mostrar el array
#resultante.
#10. Función para buscar la primera aparición de un valor:
#Escribir una función que reciba un array de enteros y un número a buscar. La función debe retornar
#la posición de la primera aparición de ese número o -1 si no se encuentra.