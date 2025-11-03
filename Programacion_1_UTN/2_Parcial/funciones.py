import random
Puntos_GENERALA = [["[UNO]",0],["[DOS]",0],["[TRES]",0],["[CUATRO]",0],["[CINCO]",0],["[SEIS]",0],["[ESCALERA (20)]",0],["[FULL (30)]",0],["[POKER (40)]",0],["[GENERALA (50)]",0]]
def puntuaciones ():
    print("═════════════════════════\n\tPLANTILLA DE PUNTAJES\n═════════════════════════\n")
    Puntos_totales = 0
    for i in range (len(Puntos_GENERALA)):
        print (f" {Puntos_GENERALA[i][0]}\t:{Puntos_GENERALA[i][1]}")
        Puntos_totales += Puntos_GENERALA[i][1]
    print(f"═════════════════════════\nPUNTAJE TOTAL: {Puntos_totales}\n═════════════════════════\n")
    return Puntos_GENERALA, Puntos_totales
puntuaciones()

Nombre_de_dados = ["Luffy","Zoro","Nami","Robin","Usopp"]
def tirada_de_dados ():
    dados = []
    dado_permanentes =[]*5
    for i in range (5):
        numero_del_dado = random.randint (1,6)
        dados.append (numero_del_dado) 
        print (f"[{dados[i]}{Nombre_de_dados[i]}]")
        
    for i in range (3):
        dado_que_desea_mantener = str(input("Indique por el nombre cual dado desea mantener(de querer salir utilizar '*'): ")).lower()
        if dado_que_desea_mantener == "*":
            break
        for i in range (len(Nombre_de_dados)):
            if dado_que_desea_mantener == Nombre_de_dados[i]:
                dado_permanentes [i] = dados[i]
