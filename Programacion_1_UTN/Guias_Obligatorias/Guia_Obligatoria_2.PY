#Semana 2: Refactorización y mejora del sistema del Parque 🎢
#El Parque de Diversiones PythonLand quiere mejorar su sistema de gestión.
#Actualmente, el programa permite registrar un visitante, consultar qué atracciones puede usar y calcular el costo de su visita.
#En esta práctica se debe:
#1. Refactorización en funciones
#● Crear funciones para:
#○ mostrar_atracciones() → muestra el menú de atracciones.
#○ puede_subir(edad, atraccion) → devuelve True/False según si puede acceder a la atracción.
#○ calcular_precio(atraccion) → devuelve el precio de la atracción.
#○ registrar_visita() → pide datos del visitante, procesa las atracciones elegidas y retorna el
#resumen.
#○ mostrar_resumen(resumen) → imprime en pantalla la información del visitante.
#2. Modularización
#● Guardar el código en dos archivos:
#○ main.py (ejecución principal).
#○ parque.py (donde van las funciones).
#3. Paquete
#● Crear un paquete llamado gestion_parque y dentro incluir parque.py.
#● El main.py debe importar desde el paquete.
#4. Colores con colorama
#● Instalar un entorno virtual con venv.
#● Instalar la librería colorama.
#● Usar colores en la salida (ejemplo: mensajes de error en rojo, éxito en verde, menú en amarillo).
#5. Nueva funcionalidad
#● Agregar la opción de calcular un descuento del 10% si el visitante compra 3 o más atracciones.
def Confirmaciones(dato_a_confirmar):
    while True:
        confirmacion= str(input(f"Usted marco {dato_a_confirmar}\nEs correcto?(Y/N) "))
        if confirmacion == "n" or confirmacion=="N":
            dato_a_confirmar = input("Vuelva a ingresar el dato por favor: ")
        elif confirmacion == "y" or confirmacion=="Y":
            print (f"Excelente en ese caso continuemos.")
            break
        else:
            print (f"Disculpa no le entendi, intente nuevamente por favor.\n")

def continuar(dato_a_confirmar):
    while True:
        break

def menu():
    print("//////////////////////////\nBienvenido a PYTHONLAND\n//////////////////////////")
    flag_match=True
    while flag_match:
        atracciones=int(input(f"\nIndique a que atraccion desea ingresar:\n[1] Carrucel\n[2]Montaña Rusa\n[3]Casa de Terror\n"))
        
        Confirmaciones(atracciones)
        
        match atracciones:
            case 1:
                print ()
            case 2:
                print()
            case 3:
                print()    
        
        
menu()
