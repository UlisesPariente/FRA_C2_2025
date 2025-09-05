
def Desea_continuar():
    continuar=str(input("Desea continuar?(Y/N) "))
    while True:
        if continuar == "Y" or continuar =="y":
            return True
        elif continuar =="N" or continuar =="n":
            return False
        else:
            print (f"Disculpa no entendi.")
            
#○ calcular_precio(atraccion) → devuelve el precio de la atracción.
def Calcular_precio_atracciones (Atraccion):
    match Atraccion:
        case 1:
            return 800
        case 2:
            return 1500
        case 3:
            return 1200
        
#○ puede_subir(edad, atraccion) → devuelve True/False según si puede acceder a la atracción.    
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
    
#○ mostrar_atracciones() → muestra el menú de atracciones.        
def mostrar_atracciones():
    atraccion=str(input("Seleccione alguna de las opciones:\n[1]-Carrucel-\n[2]-Montaña Rusa-\n[3]-Casa de Terror-\n"))
    return atraccion     


#○ registrar_visita() → pide datos del visitante, procesa las atracciones elegidas y retorna el resumen.
def registra_visita():
    resumen = []
    nombre= str(input(f"Ingrese su nombre: "))
    edad= int (input(f"Ingrese la edad de {nombre}: "))
    resumen.append(nombre,edad)
    flag_atracciones=True
    while flag_atracciones:
        atracciones= mostrar_atracciones()
        match atracciones:
            case "1":
                atracciones = "Carrusel"
            case "2":
                atracciones = "Montaña Rusa"
            case "3":
                atracciones = "Casa de Terror"
        if Desea_continuar() == False:
            flag_atracciones=False
        resumen.append(atracciones)
    return resumen

#○ mostrar_resumen(resumen) → imprime en pantalla la información del visitante.
def mostrar_resumen(resumen):
    print (f"Nombre del visitante: {resumen[0]}\nEdad de {resumen[0]}: {resumen[1]}\nLas atracciones elegidas son:")
    for i in range (resumen[1],len(resumen)):
        print(f"\n{resumen[i]}")