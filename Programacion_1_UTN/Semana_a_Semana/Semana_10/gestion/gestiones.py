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
    while not validar.validar_numero(min_jugadores) and validar.validar_positivo(min_jugadores):
        print (F"Debe ingresar un numero entero...")
        min_jugadores = input(f"Cantidad minima de jugadores: ")
    
    max_jugadores = input(f"Cantidad maxima de jugadores: ")
    while not validar.validar_numero(max_jugadores)and validar.validar_positivo(max_jugadores):
        print (F"Debe ingresar un numero entero...")
        max_jugadores = input(f"Cantidad maxima de jugadores: ")
        
    apto =  input (f"Es apto publico? (S/N)").lower()
    while apto not in ["s","n"]:
        print (f'Debe ingresar "s" o "n"')
        apto = input(f"Es apto publico? (S/N) ").lower()
    # Pyhton toma todo dato verdadero aquellos que tengan un valor sobre el 0, el vacio y el False, siempre que este sobre encima de eso lo toma como verdadero
        #cadena = "NOMBRE"  ->  TRUE
        #numero = 5         ->  TRUE
        #Lista  = ["NOMBRE",4,2.3] -> TRUE
        
    # Python toma como falso los datos que esten vacios, que sean 0 o que sean falso 
        # cadena = ""          -> FALSE
        # numero = 0 // 0.0    -> FALSE
        # lista  = [0,0.0,""]  -> FALSE
 
    if apto == "si":
        apto_texto = "Si"
    elif apto == "no":
        apto_texto = "No"
        
    juego = {
        "nombre" : nombre,
        "min" : min_jugadores,
        "max" : max_jugadores,
        "atp" : apto_texto
}
        