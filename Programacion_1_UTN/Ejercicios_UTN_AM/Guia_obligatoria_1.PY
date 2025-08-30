#1.Escribir una función llamada saludar(nombre) que reciba un nombre como parámetro e imprima un saludo. Luego, el programa debe pedir el nombre del usuario y llamar a la función.
"""def saludar (name):
    print("Hola",name)
nombre = str (input("Ingrese un nombre:"))
saludar (nombre)"""
#2. Escribir una función operaciones(num1, num2) que reciba dos números y muestre su suma, resta y multiplicación. Luego, el programa debe pedir dos números al usuario y llamar a la función.
"""def suma_multiplicacion (num1,num2):
    suma = num1 +num2
    multiplicacion= num1*num2
    print ("",num1,"+",num2,"=",suma,"\n",num1,"x",num2,"=",multiplicacion)
num_ejemplo_1 = float(input("Ingrese un numero: "))
num_ejemplo_2 = float(input("Ingrese un numero: "))
suma_multiplicacion(num_ejemplo_1,num_ejemplo_2)"""
#3. Definir una función area_triangulo que reciba la base y la altura de un triángulo y devuelva su área. Luego, el programa debe pedir los valores y mostrar el resultado. Fórmula: area = (b * h) / 2.
"""def area_triangulo(base,altura):
    area= (base*altura)/2
    print ("El area del triangulo es: ",area_triangulo(base,altura))
    return area"""
#4. Crear una función buscar_mayor que reciba tres números y devuelva los tres números ordenados de mayor a menor. Luego, el programa debe pedir los números y mostrar los números ordenados.
"""def buscar_mayor():
    for i in range (3):
        num = float (input("Ingrese 3 numeros: "))
        if i == 0:
            num_mayor=num
            num_menor=num
            num_medio=num
            
        elif num>=num_mayor:
            num_mayor=num
        
        elif num_menor>=num:
            num_menor=num
    print ("Los numeros ingresados de forma ordenada son:\n",num_mayor,"\n",num_medio,"\n",num_menor)
buscar_mayor()"""
#5. Definir una función es_par(numero) que reciba un número y devuelva True si es par y False si es impar. Luego, el programa debe pedir un número y mostrar si es par o impar usando la función.
"""def es_par(num):
    
    if num%2 == 0:
        print ("Es par")
        return True
    else:
        print("Es impar")
        return False
        
    
num= float(input("Ingrese un numero: "))
es_par(num)"""
#6. Crear una función convertir_minutos(minutos) que reciba una cantidad de minutos y devuelva cuántas horas y minutos sobran.
"""def convertir_minutos(minutos):
    contador_horas = 0
    while True:
        if minutos >=60:
            contador_horas += 1
            minutos -= 60
        elif minutos == 0 and contador_horas>0:
            return contador_horas
        elif minutos != 0 and contador_horas ==0:
            return minutos
        else:
            return contador_horas, minutos
convertir_minutos(128)      """ 
            
#7. Escribir una función verificar_acceso(edad) que reciba la edad de una persona y determine si es mayor de edad (18 años o más) devolviendo un booleano. Luego, el programa debe pedir la edad al usuario y mostrar un mensaje apropiado.
"""def verificar_acceso(edad):
    if edad >=18:
        print("Mayor de edad\nAcceso autorizado")
        return True
    else:
        print("Menor de edad\nAcceso denegado")
        return False
edad=int (input("Ingrese la edad: "))
verificar_acceso(edad)    """
#8. Crear una función llamada calcular_edad(anio_nacimiento) que reciba el año de nacimiento y devuelva la edad actual (sin considerar el mes de nacimiento). Luego, el programa debe pedir el año de nacimiento del usuario y mostrar la edad calculada.
def calcular_edad(año_nacimiento):
    edad_actual = 2025-año_nacimiento
    return edad_actual
año_nacimiento= int(input("Ingresar el año de nacimiento: "))
print("La edad que deberia tener es:",calcular_edad(año_nacimiento))