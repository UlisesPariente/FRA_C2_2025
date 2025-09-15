import Constantes


while Constantes.flag_exit:
    menu = int(input(f"Bienvenido a la biblioteca\nSeleccione una de las opciones:\n[1] Cargar titulos y ejemplares\n[2] Mostrar catalogo completo\n[3] Consultar disponibilidad\n[4] Listar títulos agotados\n[5] Agregar un nuevo título\n[6] Actualizar ejemplares\n[7] Salir"))
    match menu: 
        case 1:
            Constantes.Cargar_titulos_y_ejemplares()
        case 2:
            Constantes.Mostrar_catalogo_completo()
        case 3:
            Constantes.Consultar_disponibilidad()
        case 4:
            Constantes.listar_titulos_agotados()
        case 5:
            Constantes.agregar_un_nuevo_titulo()
        case 6:
            Constantes.actualizar_ejemplares()
        case 7:
            print (f"/////////////////\nFinalizando el programa\n/////////////////")
            break
    
#7. Salir
#Ejemplo de listas paralelas:
#titulos = ["El Señor de los Anillos", "Orgullo y Prejuicio", "Matar un Ruiseñor"]
#ejemplares = [5, 3, 7]
#Puntos clave:
#● Usar listas estáticas de tamaño fijo ([""] * 20 y [0] * 20).
#● Manejar correctamente los índices para mantener sincronizados títulos y ejemplares.
#● Evitar sobrepasar el límite de 20 elementos.
#● Modularizar usando funciones para cada opción del menú.
    
    
       
 
