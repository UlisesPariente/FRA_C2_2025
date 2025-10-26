#Semana 2: Refactorización y mejora del sistema del Parque 🎢
#El Parque de Diversiones PythonLand quiere mejorar su sistema de gestión.
#Actualmente, el programa permite registrar un visitante, consultar qué atracciones puede usar y calcular el costo de su visita.
#En esta práctica se debe:
#1. Refactorización en funciones
#● Crear funciones para:
#○ mostrar_atracciones() → muestra el menú de atracciones.
ATRACCIONES = [["Montaña Rusa",1500], ["Casa del Terror",1200], ["Carrusel",800]]
atracciones_visitante = []
def mostrar_atracciones ():
    print (f"El Parque de Diversiones tiene abiertas de momento las atracciones:\n")
    for i in range(len(ATRACCIONES)):
        print (f"{[i+1]} {ATRACCIONES[i][0]}  ->  ${ATRACCIONES[i][1]}")

#○ puede_subir(edad, atraccion) → devuelve True/False según si puede acceder a la atracción.
def puede_subir (edad, atraccion):
    
    if edad >= 12:
        if atraccion == ATRACCIONES[0][0]:
            return True
        else:
            return False
    
    if edad <= 6:
        if atraccion == ATRACCIONES[2][0]:
            return True
        else:
            return False
        

#○ calcular_precio(atraccion) → devuelve el precio de la atracción.
def calcular_precio (atraccion):
    acumulador = 0
    for i in range (len (atracciones_visitante)):
        acumulador += atracciones_visitante[i][1]
    return acumulador

#○ registrar_visita() → pide datos del visitante, procesa las atracciones elegidas y retorna el resumen.
def registrar_visita ():
    nombre_del_visitante = str(input(f"Indique su nombre:\n"))
    edad_del_visitante = int (input(f"Indique la edad de {nombre_del_visitante}\n"))
    
    while True:
        atraccion_a_subir = int(input(f"Usando los numeros asignados, indique a que juego desea ingresar:\n"))
        atracciones_visitante.append(ATRACCIONES[atraccion_a_subir-1])
        
        continuar = str(input("Desea ingresar otra atraccion? Y/N\n")).lower()
        if continuar == "N".lower():
            break 
    resumen = [nombre_del_visitante, edad_del_visitante, atracciones_visitante]    
    
    return resumen
#○ mostrar_resumen(resumen) → imprime en pantalla la información del visitante.
def mostrar_resumen (resumen):
    
    print (f"» Nombre: {resumen[0]}\n» Edad: {resumen[1]}\n» Atracciones:")
    for i in range (len(resumen[2])):
        print (F"\t- {resumen[2[i][0]]}")
        
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
