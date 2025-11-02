def puntuaciones ():
    print("═════════════════════════\n\tPLANTILLA DE PUNTAJES\n═════════════════════════\n")
    Puntos_GENERALA = [["[UNO]",":",0],["[DOS]",":",0],["[TRES]",":",0],["[CUATRO]",":",0],["[CINCO]",":",0],["[SEIS]",":",0],["[FULL]",":",0],["[POKER]",":",0],["[GENERALA]",":",0]]
    Puntos_totales = 0
    for i in range (len(Puntos_GENERALA)):
        Puntos_totales += Puntos_GENERALA[i][2]
    print(f"═════════════════════════\n\tPUNTAJE TOTAL: {Puntos_totales}\n═════════════════════════\n")
    return Puntos_GENERALA, Puntos_totales