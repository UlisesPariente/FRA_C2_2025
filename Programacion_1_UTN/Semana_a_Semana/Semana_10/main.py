#formato archivo csv
import gestion as g
"""
NOMBRE,MIN JUG,MAX JUG,ATP
Monopoly,2,6,Si
Uno,2,6,No
"""

nombre_archivo = "Juego.cvs"

opcion = ""
while opcion!="4":
    print("\n==== Gestion Juego de Mesa ====\n[1] Ingresar un nuevo juego\n[2] Mostrar catalogo de juegos\n[3] Modificar un juego existente\n[4] Salir")
    opcion =  str(input("Ingresar opcion: "))
    match opcion:
        case "1": 
            g.ingresar_o_modificar_juego