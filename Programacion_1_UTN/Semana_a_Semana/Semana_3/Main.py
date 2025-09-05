import funciones

flag_inicio=True
while flag_inicio:
    opciones= str(input (f"----------------------------\nMENU PRINCIPAL\n----------------------------\n[1] Registrar Turno\n[2] Calcular Pago\n[3] Mostrar mensaje de agradecimiento\n[4] Salir\n"))
    match opciones:
        case "1":
            no,tu=(funciones.pedir_turno())
            print (funciones.registrar_turno(no,tu))
        case "2":
            hr, tu = funciones.pedir_pago
            print (funciones.calcular_pago(hr,tu))
        case "3":
            funciones.mensaje_agradecimiento()
        case "4":
            print (f"Adios, nos vemos luego")
            flag_inicio = False
        case _:
            print(f"Opcion invalida, ingrese de nuevo")