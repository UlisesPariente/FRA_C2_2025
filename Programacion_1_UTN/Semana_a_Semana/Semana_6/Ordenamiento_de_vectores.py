#Ordenamiento de vectores
#Ordenar o acomodar de forma alfabetica o con algun filtro para que se pueda encontrar los datos de forma mas sencillo
import Funciones

numeros = [5,1,8,2,9,3]

print (f"Antes {numeros}")

Funciones.burbuja_ascendente(numeros)

Funciones.burbuja_descendente(numeros)

Funciones.burbuja_mejorada_numeros(numeros)

print (f"despues: {numeros}")


palabras = ["Notebook","notepad","Celular","TV","TV"]

print (f"antes{palabras}")
Funciones.burbuja_mejorada_palabras(palabras)
print (f"despues {palabras}")

#CODIGO ASCII de cada palabra

