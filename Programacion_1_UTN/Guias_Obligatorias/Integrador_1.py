#Práctica Semana 1: Inicio del sistema de gestión del Parque de Diversiones 🎢
#El Parque de Diversiones "PythonLand" necesita un programa inicial para registrar la entrada de visitantes.
#El sistema debe:
#1. Ingreso de datos secuenciales
#○ Pedir el nombre y edad de un visitante.
#○ Pedir cuántas atracciones quiere usar (por ahora, el parque tiene solo 3 atracciones: Montaña
#Rusa, Casa del Terror y Carrusel).
ATRACCIONES = [["Montaña Rusa",1500], ["Casa del Terror",1200], ["Carrusel",800]]


def Montaña_Rusa_Verificador_Edad(edad):
    if edad >= 12:
        print (f"» En tu caso cumplis con la edad requerida para la Montaña Rusa")
        return True
    else:
        print(f"» En tu caso NO cumplis con la edad minima para la Montaña Rusa")
        return False
    
    
def Carrusel_restriccion_de_edad(edad):
    if edad<6:
        print (f"» En tu caso solo podras concluir al carrusel")
        return True
    else:
        return False
        
def calculador_de_precios_TOTAL (atracciones):
    acumulador = 0 
    if len(atracciones) == 0:
        return (f"$0 (No ingreso a ninguna atraccion)")
    else:    
        for i in range (len(atracciones)):
            acumulador += atracciones[i][1]
        return (f"${acumulador}")
    
        
def ingreso_datos_secuenciales():
    
    Nombre_del_Visitante = str(input ("» Ingrese el nombre del visitante: \n"))
    while True:
        if Nombre_del_Visitante == "":
            Nombre_del_Visitante= str(input("» No llego a entenderse el nombre del visitante, desea ingresarlo nuevamente? Y/N\n "))
            if Nombre_del_Visitante == "Y" or Nombre_del_Visitante == "y":
                Nombre_del_Visitante = str(input("» Perfecto, como te llamas entonces?\n"))
                break
            if Nombre_del_Visitante == "N" or Nombre_del_Visitante == "n":
                print ("» Hasta la proxima, lo esperamos")
                break
            else:
                print ("» Disculpa no se entendio lo escrito, intente nuevamente")
        
        else:
            break
        
        
    edad_del_visitante = int(input(f"» Ingrese la edad de {Nombre_del_Visitante}:\n"))
    if edad_del_visitante < 0:
        edad_del_visitante = int(input(f"Edad registrada no valida, intente nuevamente\nCuantos años tenes?\n"))


    

    print(f"\n═════════════════════════════════════\n» Hola {Nombre_del_Visitante}, a que atraccion deseas subir hoy?\nTenemos:")
    atracciones_del_visitante=[]
    numero = 3
    for i in range (numero):
        while True:
            for i in range (len(ATRACCIONES)):
                print (f"» [{i+1}] {ATRACCIONES[i][0]} = ${ATRACCIONES[i][1]}")
            print (f"¤ Para salir ingresar 0 ¤")
            atraccion_a_subir = int(input())
            if atraccion_a_subir >3:
                numero += 1
                print (f"» Atraccion invalida, intente nuevamente con una de las 3 opciones.")
            elif atraccion_a_subir == 0:
                break
                

#2. Uso de condicionales    
#○ Determinar si el visitante puede subir a la Montaña Rusa (solo si tiene 12 años o más).
            
            if Montaña_Rusa_Verificador_Edad(edad_del_visitante) == False:
                if atraccion_a_subir == 1:
                    print("» Acceso denegado\nSeleccione otra atraccion")
                       
            else:
                print ("» Acceso permitido")
                break
    
#○ Si el visitante tiene menos de 6 años, solo puede subir al Carrusel.
#○ Los demás pueden acceder a todas las atracciones.
            
            if Carrusel_restriccion_de_edad(edad_del_visitante) == True:
                if atraccion_a_subir == 1 or atraccion_a_subir == 2:
                    print ("» Acceso denegado.\nSeleccione otra atraccion")
                    
                else:
                    print("» Acceso permitido.")
                    break
        if atraccion_a_subir > 0 and atraccion_a_subir < 4:
            atracciones_del_visitante.append(ATRACCIONES[atraccion_a_subir-1])   
        
        
        continuar = str(input("\nDesea ingresar otra atraccion? Y/N\n"))
        if continuar == "N" or continuar == "n":
            break
        if continuar == "Y" or continuar =="y":
            print ("\n═════════════════════════════════════\n")
        else:
            print ("\nSe detecto un caracter irreconocible, vuelva a tratar.")            

#3. Uso de ciclos
#○ Calcular el costo total de las entradas (ejemplo: Montaña Rusa = $1500, Casa del Terror =$1200, Carrusel = $800).
    print(f"\n═════════════════════════════════════\n» Nombre: {Nombre_del_Visitante}\n»Edad: {edad_del_visitante}\n» Atracciones que desea ingresar:")
    for i in range (len(atracciones_del_visitante)):
        print (f"   » {atracciones_del_visitante[i][0]}")
    print(f"» Precio total a pagar es {calculador_de_precios_TOTAL(atracciones_del_visitante)}\n═════════════════════════════════════")
    

ingreso_datos_secuenciales()

    
#4. Salida de resultados
#○ Mostrar un resumen con el nombre del visitante, la lista de atracciones que eligió, cuáles pudo
#usar y el costo total a pagar.
