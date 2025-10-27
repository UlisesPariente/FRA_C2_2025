#En este modulo es donde vamos a usar nuestras validaciones
from Utilidades import Validacion as validar

# nosotros como parametro inicial, lo que vamos a hacer es que el parametro es None porque si no se envia vamos a poner que el catalogo no esta, en el caso de no recibi es darle la opcion al restro del programa para que el catalogo sea Nulo
# como parametro de base se lo pone como true porque si nosogtros le mandamos un falso para reemplazar al nuevo lo que sucede es modificar, de lo contrario continua siendo true

# NUEVO == TRUE -> agrega un juego en modo "a"
# NUEVO == FALSE -> modifica un juego existente, previamente obtenemos todo el monetenido del archito y sobre escribimos con modo "w"

def ingresar_o_modificar_juego (nuevo = True,catalogo = None, nombre_archivo = "juegos.csv"):
    
    if not nuevo:
        # mostramos catalogo
        #Mostrar_catalogo (catalogo):
        # necesitamos la posicion para modificar
        pass
    
    # solicitar datos 
    nombre = input (F"Nombre de Juego: ")
    while not validar.validar_texto_vacio(nombre):
        print (f"Nombre no puede estar vacio...")
        nombre =input ("Nombre de juego: ")
    
    min_jugadores = input(f"Cantidad minima de jugadores: ")
    while not validar.validar_numero(min_jugadores):
        print (F"Debe ingresar un numero entero...")
        min_jugadores = input(f"Cantidad minima de jugadores: ")
    
    max_jugadores = input(f"Cantidad minima de jugadores: ")
    while not validar.validar_numero(max_jugadores):
        print (F"Debe ingresar un numero entero...")
        max_jugadores = input(f"Cantidad minima de jugadores: ")
        