#Práctica Semana 1: Inicio del sistema de gestión del Parque de Diversiones 🎢
#El Parque de Diversiones "PythonLand" necesita un programa inicial para registrar la entrada de visitantes. El sistema debe:

#1. Ingreso de datos secuenciales 
# ○ Pedir el nombre y edad de un visitante. 
# ○ Pedir cuántas atracciones quiere usar (por ahora, el parque tiene solo 3 atracciones: Montaña Rusa, Casa del Terror y Carrusel).

#2. Uso de condicionales 
# ○ Determinar si el visitante puede subir a la Montaña Rusa (solo si tiene 12 años o más). 
# ○ Si el visitante tiene menos de 6 años, solo puede subir al Carrusel. 
# ○ Los demás pueden acceder a todas las atracciones.

#3. Uso de ciclos 
# ○ Preguntar por cada atracción que el visitante desea usar y mostrar si puede subir 
# o no según su edad. 
# ○ Calcular el costo total de las entradas (ejemplo: Montaña Rusa = $1500, Casa del Terror = $1200, Carrusel = $800).

#4. Salida de resultados 
# ○ Mostrar un resumen con el nombre del visitante, la lista de atracciones que eligió, cuáles pudo usar y el costo total a pagar.
flag_cierre=True
Montaña_Rusa = 1500
Casa_del_terror = 1200
Carrusel = 800

while flag_cierre:
    nombre = str(input("Ingrese el nombre del visitante: "))
    edad= int(input("\nIngrese la edad del mismo: "))
    contador =0
    costo_total_ingreso=0
    Atracciones_ingresadas=""
    while contador<3:
        if edad <=6 :
            print("\nAvisarle que al ser menor de 7 años, el unico juego que puede participar es el Carrusel\n")
            costo_total_ingreso += Carrusel
            Atracciones_ingresadas+="Carrusel"
            break
        
        flag_match = True
        while flag_match:
            atracciones = str(input("\nIngresar de a una atraccion a cual quiere ingresar: ")) 
            Atracciones_ingresadas+="\n"
            Atracciones_ingresadas+=atracciones
            match atracciones:
                
                case "Carrusel":
                    costo_total_ingreso += Carrusel
                    flag_match =False  
                                    
                case "Montaña Rusa":
                    costo_total_ingreso += Montaña_Rusa
                    flag_match =False
                case "Casa del Terror":
                    costo_total_ingreso += Casa_del_terror
                    flag_match =False                
                case _:
                    print ("\nNo se pudo registrar la atraccion asignada por favor reintentar:")
        
        contador +=1
        
        if edad <=12:
            if  atracciones != "Casa del Terror":
                print("\nPerfecto podra ingresar a la atraccion")
                
            else:
                print("\nNecesita ser mayor de 12 años para poder ingresar")
                
        else:
            print ("\nPerfecto podra ingresar a la atraccion")
            
        
        Continuar = str(input("\nDesea ingresar a otra atraccion?(Y/N) "))
        if Continuar == "N" or Continuar == "n":
            break
        else:
            print ("\nPerfecto continuemos.")
            
    print ("\n----------",nombre,"----------\nCosto de entrada:",costo_total_ingreso,"\nAtracciones elegidas:",Atracciones_ingresadas)

    Continuar = str(input("\nDesea ingresar a otra Persona?(Y/N) "))
    if Continuar == "N" or Continuar == "n":
        flag_cierre=False
    else:
        print ("\nPerfecto continuemos.")