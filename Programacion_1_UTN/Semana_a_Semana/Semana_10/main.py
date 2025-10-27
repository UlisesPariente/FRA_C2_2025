#Catalogo de juegos, en la cual tiene una lista de juegos donde tenga el minimo de jugadores que permite, y el maximo del mismo
#y un bool donde diga si es apto para publico.

#Formato archivo CSV
#
#
# todos los datos del registro donde se separan por comas
#el archivo lo va a guardar por comas
#las comas va a separar los campos para que puedan cargarse como si fuera un excel
#CSV es un archivo mas ligero que el comun y permite tener diferentes aplicaciones (Compatible con todo)
# 
#

'''
NOMBRE,MIN JUG,MAX JUG,ATP
Monopoly,2,6,Si
Uno,2,6,Si
'''



nombre_archivo = "juego.csv"

opcion = ""

while opcion != "4":
    print (f"\n==== Gestion juegos de mesa ====")
    print (f"1. Ingresar un nuevo juego")
    print (f"2. Mostrar catalogo de juegos")
    print (f"3. Modificar un juego existente")
    print (f"4. Salir")
    opcion = input(f"Ingresar opcion: ")
    
    match opcion:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4: 
            pass
        case _:
            print ("Opcion invalida, vuelva a ingresar....\n")
            
            