# Factorial de un numero

def factorial (n):
    #siempre lo primero es definir el caso base (condicion para que la funcion deje de llamarse a si misma)
    if n == 0:
        return 1
    
    #caso recursivo (aca es donde la funcion se llama a si misma para que realice la tarea)
    # factorial de un numero es cuando multiplicamos el numero por todos los anteriores hasta el 0
    return n * factorial (n-1)

def factorial_v2 (n):
    print (f"Llamado a factorial: {(n)}") 
    if n == 0:
        print ("Caso base alcanzado: factoral (0) = 1")
        return 1
    
    resultado = n * factorial_v2 (n-1)
    print (f"Retornando factorial {(n)} = {resultado}")
    return resultado

#numero =int (input("Ingrese el numero"))
#factorial_v2 (numero)

def suman_numeros (n,nivel = 0 ):
    #IMPRIME la llamada actual con inventado segun el nivel de profundidad recursiva
    print (f"  " * nivel + f"Llamando a suma_numeros {(n)}")
     # caso base
    if n == 0 :
        return 0
    # return 0 porque si es 1 afecta a la suma
    
    #llamamos a la funcion de n-1
    resultado_parcial = suman_numeros (n-1,nivel+1)
    
    resultado_total = n + resultado_parcial
    print ("  "*nivel+f"Retorna {n} + {resultado_parcial} = {resultado_total}")
    return resultado_total

#num = int (input("ingresar un numero:  "))
#print (F"Resultado final : {suman_numeros (num)}")

def suma_directa_de_numeros (n):
    if n == 0:
        return 0
    return n + suma_directa_de_numeros (n-1)

#num = int(input("numero a sumar: "))
#print (f"Resultado final  =  {suma_directa_de_numeros(num)}")

#Recorrido de lista

def buscar (lista, valor):
    #caso base 
    if len(lista) == 0:
        return False
    
    # caso base 2
    if lista [0] == valor:
        return True
    
    #caso recursivo
    #si el primer elemento (0) no es el buscado, se llama nuevamente a la funcion
    return buscar (lista[1:] , valor)
#los dos puntos(:) hace que ignore el item que tiene delante para saltarse al siguiente

lista_programa = ["Hola","Chau",15,6.4]
#valor = input("Ingresar valor a buscar: ")
#print (buscar(lista_programa,valor))


def hanoi (n,origen, destino ,auxiliar):
    # n == cantirdad de piezas
    # origen  ==  torre A donde comienza nuestros platos
    # destino == es la torre en la que debemos la nueva pila 
    # auxiliar == torre del medio que se usa para apoyo de las mismas.
    
#nunca se puede poner un plato mas grande encima de uno mas chico 
    
    if n == 1: # caso base 
        print (f"Mover disco desde {origen} a {destino}")
    else: 
        #caso recursivo en el caso de que no sea el primer caso
        #paso 1 mover los (n-1) discos superiores desde la torre de origen a la torre auxiliar
        #usando destino como apoyo
        #primero se pone un disco chiquito a la del destino paraque se pueda luego usar la auxiliar para las grandes y completar el esquema
        hanoi (n-1,origen,destino,auxiliar)
        
        #paso 2 mover el disco restante (el mas grande) desde el origen hasta el destino
        print (f"mover disco de {origen} a {destino}")
        
        #paso 3 mover los (n-1) discos que quedaron en la torre auxiliar hacia la torre destino usando torre de origen como apoyo
        hanoi (n-1, origen,destino,auxiliar)

discos = int (input("Ingresar cantidad de discos: "))
print (f"Movimientos necesarios para resolver torre de hanoi con {discos} discos: ")
hanoi (discos, "torre A", "Torre B", "Torre C" )