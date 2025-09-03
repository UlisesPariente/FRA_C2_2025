#Semana 2: Refactorización y mejora del sistema del Parque 🎢
#El Parque de Diversiones PythonLand quiere mejorar su sistema de gestión.
#Actualmente, el programa permite registrar un visitante, consultar qué atracciones puede usar y calcular el costo de su visita.
#En esta práctica se debe:
#1. Refactorización en funciones
#● Crear funciones para:
#○ mostrar_atracciones() → muestra el menú de atracciones.
#○ puede_subir(edad, atraccion) → devuelve True/False según si puede acceder a la atracción.
#○ calcular_precio(atraccion) → devuelve el precio de la atracción.
#○ registrar_visita() → pide datos del visitante, procesa las atracciones elegidas y retorna el resumen.
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

def Calcular_precio_atracciones (Atraccion):
    match Atraccion:
        case 1:
            return 800
        case 2:
            return 1500
        case 3:
            return 1200
        
    
def puede_subir(edad, atraccion):
    if edad <= 6:
        if atraccion == 1:
            return True
        else:
            return False
    elif edad<=12:
        if atraccion != 3:
            return False
        else:
            return True
    else:
        return True
        
def mostrar_atracciones():
    atraccion=str(input("Seleccione alguna de las opciones:\n-Carrucel-\n-Montaña Rusa-\n-Casa de Terror-\n"))
    return atraccion     
#○ registrar_visita() → pide datos del visitante, procesa las atracciones elegidas y retorna el resumen.

def Desea_continuar():
    continuar=str(input("Desea continuar?(Y/N) "))
    while True:
        if continuar == "Y" or continuar =="y":
            return True
        elif continuar =="N" or continuar =="n":
            return False
        else:
            print (f"Disculpa no entendi.")

def registra_visita():
    resumen = []
    nombre= str(input(f"Ingrese su nombre: "))
    edad= int (input(f"Ingrese la edad de {nombre}: "))
    resumen.append(nombre,edad)
    flag_atracciones=True
    while flag_atracciones:
        atracciones= mostrar_atracciones()
        if Desea_continuar() == False:
            flag_atracciones=False
        resumen.append(atracciones)
    return resumen

#○ mostrar_resumen(resumen) → imprime en pantalla la información del visitante.

def mostrar_resumen(resumen):
    print (f"Nombre del visitante: {resumen[0]}\nEdad de {resumen[0]}: {resumen[1]}\nLas atracciones elegidas son:")
    for i in range (resumen[1],len(resumen)):
        print(f"\n{resumen[i]}")
    
def MENU_PYTHONLAND():
    while True:
        print("//////////////////////////\nBienvenido a PYTHONLAND\n//////////////////////////")
        flag_atracciones=True
        while flag_atracciones:
            mostrar_atracciones()

           
        

