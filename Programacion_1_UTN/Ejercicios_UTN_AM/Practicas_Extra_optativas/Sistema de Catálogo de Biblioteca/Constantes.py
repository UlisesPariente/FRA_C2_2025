CANTIDAD_DE_LIBROS = 20
EJEMPLARES = [0] * CANTIDAD_DE_LIBROS
TITULOS = [""] * CANTIDAD_DE_LIBROS
CONTADOR = 0


def carga_de_datos():
    Dato = input ("Ingrese el dato a cargar: ")
    return Dato 

#3. Opciones del menú:
#1. Cargar títulos y ejemplares
#Permitir al usuario ingresar hasta 20 títulos y la cantidad de ejemplares para cada uno.
def Cargar_titulos_y_ejemplares():
        print (f"\n////Titulo////")
        TITULOS [CONTADOR] = carga_de_datos()
        print (f"\n////Ejemplares de {TITULOS[CONTADOR]}////")
        EJEMPLARES [CONTADOR] = carga_de_datos()
        CONTADOR += 1
    
#2. Mostrar catálogo completo
#Listar cada título con su número de ejemplares.
#Ejemplo: El Señor de los Anillos → 5 copias
def Mostrar_catalogo_completo():
    for i in range (CANTIDAD_DE_LIBROS):
        print (f"\n{i+1}_ {TITULOS[i]} -> {EJEMPLARES[i]} copias")

#3. Consultar disponibilidad
#Pedir al usuario un título y mostrar cuántas copias tiene.
def Consultar_disponibilidad ():
    titulo_a_buscar = str(input("Ingrese el titulo a buscar: "))
    for i in range (len(TITULOS)):
        if titulo_a_buscar == TITULOS[i]:
            print (f"Se encontro el titulo {titulo_a_buscar} -> {EJEMPLARES} copias")
            

#4. Listar títulos agotados
#Mostrar solo aquellos títulos que tengan 0 copias.
def listar_titulos_agotados():
    for i in range (len(TITULOS)):
        if EJEMPLARES[i] == 0:
            print(f"\n{TITULOS} AGOTADO")
           

#5. Agregar un nuevo título
#Permitir al usuario agregar un nuevo libro y su cantidad de ejemplares si no se superó el máximo de 20.
def agregar_un_nuevo_titulo(): 
    for i in range (len(TITULOS)):
        if "" == TITULOS[i]:
            Titulo_nuevo = str(input(f"Ingrese el libro que desee añadir: "))
            Ejemplares_nuevo = int(input(f"Ingrese los ejemplares de {Titulo_nuevo}: "))
            TITULOS[i]=Titulo_nuevo
            EJEMPLARES[i]=Ejemplares_nuevo
            print (f"Se añadio correctamente") 
                   

#6. Actualizar ejemplares (préstamo / devolución)
#Permitir al usuario modificar el número de ejemplares de un libro existente.
def actualizar_ejemplares():
    Titulo_prestamo = str(input("Ingrese el libro que regreso: "))
    cantidad_prestamo = int(input("Ingrese la cantidad que regresaron: "))
    for i in range (CANTIDAD_DE_LIBROS):
        if TITULOS[i] == Titulo_prestamo:
            EJEMPLARES[i] += cantidad_prestamo
            print ("\nSe actualizo correctamente.") 