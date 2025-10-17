#Práctica Semana 1: Inicio del sistema de gestión del Parque de Diversiones 🎢
#El Parque de Diversiones "PythonLand" necesita un programa inicial para registrar la entrada de visitantes.
#El sistema debe:
#1. Ingreso de datos secuenciales
#○ Pedir el nombre y edad de un visitante.
#○ Pedir cuántas atracciones quiere usar (por ahora, el parque tiene solo 3 atracciones: Montaña
#Rusa, Casa del Terror y Carrusel).
ATRACCIONES = [["Montaña Rusa",1500], ["Casa del Terror",1200], ["Carrusel",800]]

def ingreso_datos_secuenciales():
    Nombre_del_Visitante = input ("Ingrese el nombre del visitante: ")
    flag_inicio =True
    while True:
        while True:
            if Nombre_del_Visitante == "":
                Nombre_del_Visitante= input("No llego a entenderse el nombre del visitante, desea ingresarlo nuevamente? Y/N ")
                if Nombre_del_Visitante == "Y" or "y":
                    Nombre_del_Visitante = input("Perfecto, como te llamas entonces?\n")
                    break
                else:
                    print ("Hasta la proxima, lo esperamos")
                    flag_inicio =False
                    break
            else:
                break
        if flag_inicio == False:
            break
        
        edad_del_visitante = int(input(f"Ingrese la edad de {Nombre_del_Visitante}: "))
        if edad_del_visitante < 0:
            edad_del_visitante = input(f"edad registrada no valida, intente nuevamente\nCuantos años tenes? ")

        print(f"Hola {Nombre_del_Visitante}, a que atraccion deseas subir hoy?\nTenemos:")
        for i in range (len(ATRACCIONES)):
            print (f"[{i+1}] {ATRACCIONES[i]} = ${ATRACCIONES[i]}")
        accion = input()
ingreso_datos_secuenciales()
#2. Uso de condicionales
#○ Determinar si el visitante puede subir a la Montaña Rusa (solo si tiene 12 años o más).
#○ Si el visitante tiene menos de 6 años, solo puede subir al Carrusel.
#○ Los demás pueden acceder a todas las atracciones.
#3. Uso de ciclos
#○ Preguntar por cada atracción que el visitante desea usar y mostrar si puede subir o no según
#su edad.
#○ Calcular el costo total de las entradas (ejemplo: Montaña Rusa = $1500, Casa del Terror =
#$1200, Carrusel = $800).
#4. Salida de resultados
#○ Mostrar un resumen con el nombre del visitante, la lista de atracciones que eligió, cuáles pudo
#usar y el costo total a pagar.
