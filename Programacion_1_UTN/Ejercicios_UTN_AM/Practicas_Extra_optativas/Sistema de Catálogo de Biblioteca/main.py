import Constantes
#3. Opciones del menú:
#1. Cargar títulos y ejemplares
#Permitir al usuario ingresar hasta 20 títulos y la cantidad de ejemplares para cada uno.

while flag_exit:
    
    for i in range (Constantes.CANTIDAD_DE_LIBROS):
        print (f"\n////Titulo////")
        Constantes.TITULOS [i] = Constantes.carga_de_datos()
        print (f"\n////Ejemplares////")
        Constantes.EJEMPLARES [i] = Constantes.carga_de_datos()
    
    
        while True:
            exit = str(input("\n-Desea continuar? (Y/N) "))
            if exit == "n" or "N":
                flag_exit = False
                print (f"\nFinalizando el proceso.")
                break
            elif exit == "Y" or "y":
                print (f"\nPerfecto continuemos")
            else:
                print (f"\nDisculpa no entendi.")
        if flag_exit == False:
            break
        
#2. Mostrar catálogo completo
#Listar cada título con su número de ejemplares.
#Ejemplo: El Señor de los Anillos → 5 copias
for i in range (Constantes.CANTIDAD_DE_LIBROS):
    print (f"\n{i+1}_ {Constantes.TITULOS[i]} -> {Constantes.EJEMPLARES[i]} copias")
#3. Consultar disponibilidad
#Pedir al usuario un título y mostrar cuántas copias tiene.
titulo_a_buscar = str(input("Ingrese el titulo a buscar: "))
for i in range (len(Constantes.TITULOS)):
    if titulo_a_buscar == Constantes.TITULOS[i]:
        print (f"Se encontro el titulo {titulo_a_buscar} -> {Constantes.EJEMPLARES} copias")
#4. Listar títulos agotados
#Mostrar solo aquellos títulos que tengan 0 copias.
for i in range (len(Constantes.TITULOS)):
    if Constantes.EJEMPLARES[i] == 0:
        print(f"\n{Constantes.TITULOS} AGOTADO")
#5. Agregar un nuevo título
#Permitir al usuario agregar un nuevo libro y su cantidad de ejemplares si no se superó el máximo
#de 20.

#6. Actualizar ejemplares (préstamo / devolución)
#Permitir al usuario modificar el número de ejemplares de un libro existente.
#7. Salir
#Ejemplo de listas paralelas:
#titulos = ["El Señor de los Anillos", "Orgullo y Prejuicio", "Matar un Ruiseñor"]
#ejemplares = [5, 3, 7]
#Puntos clave:
#● Usar listas estáticas de tamaño fijo ([""] * 20 y [0] * 20).
#● Manejar correctamente los índices para mantener sincronizados títulos y ejemplares.
#● Evitar sobrepasar el límite de 20 elementos.
#● Modularizar usando funciones para cada opción del menú.
