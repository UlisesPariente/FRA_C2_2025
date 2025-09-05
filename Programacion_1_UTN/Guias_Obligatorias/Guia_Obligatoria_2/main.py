import paquete
#4. Colores con colorama
#● Instalar un entorno virtual con venv.
#● Instalar la librería colorama.
#● Usar colores en la salida (ejemplo: mensajes de error en rojo, éxito en verde, menú en amarillo).

#5. Nueva funcionalidad
#● Agregar la opción de calcular un descuento del 10% si el visitante compra 3 o más atracciones.

    
def MENU_PYTHONLAND():
    flag_inicio=True
    while flag_inicio:
        print("//////////////////////////\nBienvenido a PYTHONLAND\n//////////////////////////")
        
        visitante= paquete.registra_visita()
        paquete.mostrar_resumen(visitante)
        if paquete.Desea_continuar() == False:
            print("\nHasta la proxima visita, adios")
            flag_inicio=False
        else:
            print(f"\nExelente sigamos regitrando a el siguiente visitante\n")
