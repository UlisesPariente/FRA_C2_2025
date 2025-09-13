#Funciones 
#1 Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
def ingreso_numeros_enteros ():
    num = int(input("Ingrese un numero enrtero: "))
    return num
#2 Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
def ingrese_numero_flotante ():
    num = float (input("Ingree numero flotante: "))
    return num
#3 Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 
def ingrese_una_cadena ():
    cadena = str(input("Ingrese una cadena de caracteres: "))
    return cadena
#4 Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 
def area_de_un_triangulo(base,altura):
    area = (base*altura)/2
    return area
#5 Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
def area_de_un_circulo (radio):
    area = (3.14*radio)**2
    return area
#6 Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando  si el número es par o impar.
def indicador_numero_par (numero):
    if numero %2 == 0:
        return (f"Es par")
    else:
        return (f"")
#7 Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.
#8 Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
#9 Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.
#10 Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.
#11 Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.
#12 Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10.
#13 Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.
