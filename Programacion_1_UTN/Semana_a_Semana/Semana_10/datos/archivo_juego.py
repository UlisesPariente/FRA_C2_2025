import os
import utilidades.validaciones as val

def cargar_catalogo (nombre_del_archivo):
    catalogo = []
    #se verifica si existe el archivo, de existir returna en un true
    #por eso se usa un NOT para validar en el caso contrario, asi sabe que retornar
    if not os.path.exists (nombre_del_archivo):
        print ("El archivo no existe aun....")
        return catalogo

    #abrir arcbivo en modo "r" (lectura)
    
    with open(nombre_del_archivo,"r") as archivo:
        encabezado = archivo.readline() #se lee la primera linea que es el encabezado ( nombre de columnas) y se descarta
        
        for linea in archivo:
            linea.strip() #primero eliminamos la posibilidad de algun espacio  vacio
            if val.validar_texto_vacio (linea): # solo procesa si la linea no esta vacia.
                partes:list = linea.split() # cada elemento de la fila sea un elemento separado que en una lista (generando una lista inexistente)
                """
                    Monopoly,2,6,Si
                    partes  = ["Monopoly","2","6","Si"]
                    
                """