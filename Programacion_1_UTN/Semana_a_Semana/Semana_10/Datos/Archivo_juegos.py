#crear toda la logica del archivo
import os
def cargar_catalogo (nombre_archivo):
    catalogo = []
#utiliza la funcion OS para verificar que exista, esto logicamente si exitste va a ser un tru y si no existe va a ser un false
    if not os.path.exists(nombre_archivo):
        #si el archivo no existe retorna la lista vacia.
        print ("El archivo no existe aun... ")
        return catalogo

#abrir archivo en modo "r" (lectura)

    with open(nombre_archivo, "r") as archivo:
        encabezado = archivo.readline () # se lee primer linea (nombre de columna y descarta
        
        for line in archivo:
            line.strip()# primero elimina las posibilidades de los espacios en vacio al principio o final del campo
            