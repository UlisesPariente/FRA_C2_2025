
ELEMENTO_STRING = 0 
ELEMENTO_ENTERO = 1
ELEMENTO_FLOAT = 2
ELEMENTO_BOOL = 3

#Vector de 4 elementos, el primer elemento es el 0 y sera a n-1 la cantidad total de elementos:
#                      0       1   2     3
 
Vector_de_prueba = ["cadena", 200, 2.3, False]
#Puedo añadir tanto str // int // float como guste

print (Vector_de_prueba[2]) # == 2.3

print (Vector_de_prueba[ELEMENTO_FLOAT]) # == 2.3

for i in range (len(Vector_de_prueba)):
    if i%2==0:
        print (Vector_de_prueba[i])
        
vector_nuevo = [0] * 10 #esto es para que pueda multiplicar la cantidad de datos en la lista == 
#              [0,0,0,0,0,0,0,0,0,0]
vector_nuevo[2] = True # le reemplaza el valor de 0 inicializado en la linea 21 por un BOOL 
#              [0,0,True,0,0,0,0,0,0,0]
#se puede reemplazar de la manera que quisieramos, ya sea BOOL,STR,INT,FLOAT

#                        0       1    2        3
matriz_personas = [["Eugenia",  23,  True,  "femenino"],  #0
                   ["Carlos",   32,  False, "masculino"], #1 
                   ["Patricia", 45,  True,  "femenino"],  #2
                   ]#etc...
#se puede ver asi la matriz para que resulte comodo al visual pero seria todo junto. Para acceder a un dato en particular teneos que poner la (Fila,columna)

matriz_personas[1][1] = 20 #reemplazamos la edad de Carlos de 32 --> 20 accediendo a la fila y luego a la columna de donde se encuentra el dato 



# //////////////////////////////////////

# ESTAS CONSTANTES ES IMPORTANTE EMPEZAR A UTILIZARLAS PARA PODER MODIFICAR SOLO EN UN LUGAR Y NO EN TODAS LAS LINEAS DE CODIGO QUE UTILICE LOS VALORES, DE ULTIMA UTILIZO UNA PLANILLA EXCLUSIVA PARA LAS CONSTANTES ASI SE PUEDE ENCONTRAR DE UNA MANERA MAS SENCILLA Y NO EN LA MISMA PLANILLA PARA QUE QUEDE INVASIVO 

COLUMNA_NOMBRE = 0
COLUMNA_EDAD = 1
COLUMNA_ESTADO = 2
COLUMNA_GENERO = 3


#///////////////////////////////////////////


matriz_personas [1][COLUMNA_EDAD] = 20

for fila in range (len(matriz_personas)):
    print (matriz_personas[fila][COLUMNA_NOMBRE])
                               
#Lo unico que printea seria los nombres de la matriz_persona ya que solo indicamos que el interes nuestro estaba en la columna 0
for fila in range (len(matriz_personas)):
    print (f"{fila+1}. Nombre: {matriz_personas[fila][COLUMNA_NOMBRE]} - Edad: {matriz_personas[fila][COLUMNA_EDAD]} - Genero: {matriz_personas[fila][COLUMNA_GENERO]}")


#Para entrar en cada una las variables de la matriz para corregir algo o verificar datos que hay en cada vector anidado
for fila in range (len(matriz_personas)):
    for columna in range (len(fila)):
        print (matriz_personas[fila][columna])
        
def cargar_matriz (cant_filas:int) -> list: 
    mat = [[0,0,0,0] for _ in range([cant_filas])]
    for i in range (len(mat)):
        print (f"Cargar datos personas: ")
        nombre =  input ("Ingresar nombre: ")
        edad =  int (input("Ingresar edad: "))
        estado = (True)
        genero = ("Ingrese genero: ")
    return mat

matriz_personas = cargar_matriz (2)