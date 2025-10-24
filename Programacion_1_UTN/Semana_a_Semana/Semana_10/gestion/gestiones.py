from utilidades import validaciones as validar

def mostrar_catalogo (catalogo):
    if validar.validar_catalogo_vacio(catalogo):
        return
    print("\nCATALOGO DE JUEGOS")
    print("╔"+"-"*27+"╦"+"-"*7+"╦"+"-"*7+"╦"+"-"*7+"╗")
    print(f"{"NOMBRE": ^ 25} ║ {"MIN": ^ 5} ║ {"MAX": ^ 5} ║ {"APT": ^ 5}")
    print("╚"+"-"*27+"╩"+"-"*7+"╩"+"-"*7+"╝")
    #< : alinea hacia izquierda
    #> : alinea hacia la derecha
    #^ : centra texto
    for i, juego in enumerate(catalogo):
        print(f"{juego["nombre"]:^25} ║ {juego["min"]:^5} ║ {juego["max"]:^5} ║ {juego["atp"]:^5}")
        print("╚"+"-"*27+"╩"+"-"*7+"╩"+"-"*7+"╝")
    
def buscar_juego(catalogo):
    nombre_juego = input("Ingrese juego a mostrar: ")
    for i in range (len(catalogo)):
        if catalogo[i]["nombre"].lower().strip() == nombre_juego.lower().strip():
            return i
    return -1
    
def ingresar_o_modificar_juego(nuevo=True,catalogo=None,nombre_archivo="Juegos.csv"):
    
    if not nuevo:
        #Mostrar vatalogo
        #mostrar_catalogo (catalogo)
        #Necesitamos la posicion del juego a modificar
        mostrar_catalogo(catalogo)
        posicion = buscar_juego(catalogo)
        if posicion == -1:
            print("No se encontro el juego ingresado...")
            return
    else:
        posicion = -1
    
    nombre=input("Nombre de juego: ")
    while not validar.validar_texto_vacio(nombre):
        print("Nombre no puede estar vacio....")
        nombre=input("Nombre de juego: ")
        
    
    min_jugadores = input ("Cantidad minima de jugadores: ")
    while not validar.validar_numero(min_jugadores) and validar.validar_positivo(min_jugadores):
        print("Debes ingresar un numero entero...")
        min_jugadores = input("Cantidad minima de jugadores: ")
        
    max_jugadores=input("cantidad maxima de jugadores: ")
    while not validar.validar_numero(max_jugadores) and validar.validar_positivo (max_jugadores):
        print("Debe ingresar numero entero...")
        max_jugadores=input("Cantidad maxima de jugadores: ")
        
    apto = input("Es apto todo publico? (S/N)\n").lower()
    while apto not in ["S","N"]:
         print ('Debe ingresar "S" o  "N"')
         apto =input("Es apto todo publico? (S/N)\n").lower()
    
    #Python toma como dato verdadero aquellos que tengan un valor sobre el cero, el vacio y el falso
        #cadena="Nombre" :verdadero
        #numero=5 : verdadero
        #lista = [2,"julio"] : verdadero
        #Booleano = true: verdadero
    #Python toma como falso aquellos que esten vacios, sean cero o sean false.
        #cadena = "" : falso
        #numero = 0  : falso
        #decimal = 0.0 : falso
        #listas = [0,0.0,""] : falso
        
    if apto == "s":
        apto_texto ="Si"
    elif apto == "n":
        apto_texto = "No"
        
    juego={
        "nombre" : nombre,
        "min" : min_jugadores,
        "max" : max_jugadores,
        "apto" : apto_texto
    }
    
    if nuevo :
      pass
        #agregar un nuevo juego
    else:
        pass
        #usar posicion para modificar un juego existente
        #guardar el catalogo nuevo