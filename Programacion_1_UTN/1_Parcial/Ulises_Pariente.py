#Nombre : ULISES PARIENTE
#DNI : 43057298
#Legajo : 117307

MAX=10
LISTA_ALUMNOS = [""]*MAX
LISTA_LIBROS = [0]*MAX
LISTA_COMENTARIOS = [""]*MAX

def ingresar_datos(lista_nombres,lista_book,lista_coment):
    for i in range (MAX):
        print (f"{i+1}° Alumno.")
        while True:
            nombre = str (input("Ingrese el nombre del alumno: "))
            if nombre == "":
                print (f"No se detecto un nombre asignado\nvuelva a intentarlo.")
            else:
                lista_nombres [i] = nombre
                break
            
        while True:    
            libros = int (input(f"Cantidad de libros que leyo {nombre}: "))
            if libros >0 and libros < 21:
                lista_book [i]= libros
                break
            else:
                print(f"La cantidad ingresada ({libros}) es invalida, debe de ser entre 1a 20.\nVuelva a intentarlo.")
        
        while True:
            coment = str (input(f"Ingrese un comentario del libro {libros}: "))
            if coment == "":
                print ("No se detecto un comentario asignado.\nVuelva a intentarlo.")
            else:
                lista_coment [i]= coment
                break
        
        while True:
            desea_continuar = str(input(f"\nDesea continuar? Y/N "))
            if desea_continuar == "Y" or desea_continuar == "y":
                break
            elif desea_continuar == "N" or desea_continuar =="n":
                print(f"\nFinalizando el proceso de cargado de datos")
                break
            else:
                print(f"\nDisculpe pero no se detecto una respuesta correcta.\nVuelva a intentarlo.")
        if desea_continuar == "N" or desea_continuar=="n":
            break
        
    return (lista_nombres,lista_book,lista_coment)
 

def mostrar_habitos_de_lectura (lista_nombres,lista_book,lista_coment):
    acumulador = 0 
    contador = 0
    for i in range (MAX):
        if lista_nombres[i] == "":
            break    
        print (f"______________________\n{i+1}° Alumno:\n Nombre: {lista_nombres[i]}\n Cantidad de libros leidas: {lista_book[i]}\n Comentario: {lista_coment[i]}\n______________________")
        contador += 1
        acumulador += lista_book[i]
    promedio = acumulador / contador
    print(f"El promedio de los libros q ue leyeron todos los alumnos es de {promedio}\n") 
        

def Ordenar_alumnos_por_cantidad_de_libros_leidos(lista_nombres,lista_book,lista_coment):
    for i in range (MAX):
        for j in range (MAX-i-1):
            if lista_book[j] < lista_book[j+1]:
                lista_book[j], lista_book[j+1] = lista_book[j + 1], lista_book[j]
                lista_nombres[j], lista_nombres[j+1] = lista_nombres [j+1], lista_nombres [j]
                lista_coment[j], lista_coment[j+1] = lista_coment[j + 1], lista_coment[j]

while True:
    menu = int (input(f"Bienvenido al Registros de habitos de lectura\n[1] Ingresar datos de los alumnos\n[2] Mostrar habitos de lectura\n[3] Ordenar alumnos por cantidad de libros leidos\n[4] Salir\n"))
    match menu:
        case 1:
            ingresar_datos (LISTA_ALUMNOS,LISTA_LIBROS,LISTA_COMENTARIOS)
        
        case 2:
            mostrar_habitos_de_lectura(LISTA_ALUMNOS,LISTA_LIBROS,LISTA_COMENTARIOS)
        
        case 3:
            Ordenar_alumnos_por_cantidad_de_libros_leidos(LISTA_ALUMNOS,LISTA_LIBROS,LISTA_COMENTARIOS)
            mostrar_habitos_de_lectura(LISTA_ALUMNOS,LISTA_LIBROS,LISTA_COMENTARIOS)
            
        case 4:
            print (f"Muchas gracias por utilizar el programa, hasta la proxima")
            break