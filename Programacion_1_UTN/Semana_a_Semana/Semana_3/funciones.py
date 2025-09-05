def pedir_turno():
    nombre = str(input(f"Ingrese su nombre: "))
    turno = str (input(f"Ingrese su turno: "))
    return nombre, turno

def registrar_turno(nombre, turno):
    if turno == "d" or turno == "n":
        return (f"turno registrado {nombre} trabajara en turno {turno}")
    else:
        return (f"Turno invalido, solo se permite d o n")
      
def pedir_pago():
    horas =int(input("Ingrese cantidad de horas trabajadas: "))
    turno = (input (f"Ingrese su turno trabajado:(d/n) "))
    return horas,turno

def calcular_pago(horas, turno):
    if turno == "d":
        return horas * 100
    elif turno == "n":
        return horas * 150
    else:
        return 0
    

def mensaje_agradecimiento ():
    print(f"Gracias por usar el sistema")
    
