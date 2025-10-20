def cargar_nombres (nombre_archivo:str)->None:
    with open (nombre_archivo,"a") as archivo:
        while True:
            nombres = input ("Ingresar nombres (En blanco para finalizar):\n").strip()
            if nombres == "":
                print("Finalizando el cargado de nombres")
                break
            archivo.write(nombres+"\n") 
            
def mostrar_excepto_excluido(archivo:str,nombre:str)->None:
    with open (archivo,"r") as a:
        lista_nombres:list = a.readline()
        print("== Nombres almacenados ==")
        for n in lista_nombres:
            if n.strip().lower() != nombre.strip().lower():
                print(n)

#strip para que pueda borrar los espacios en las STR