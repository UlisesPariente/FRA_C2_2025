#una empresa de logistica tiene 3 repartidores en avellaneda
#necesita registrar las entregas realizadas en los ultimos 5 dias de la semana

#se debe almacenar en una matriz de 5x3 o 3x5

# desarrollar menu con las siguientes opciones 
#-carga datos
#-mostrar matriz
#-total por repartidor

FILAS = 3
COLUMNAS = 5

dias = ["Lunes","Martes","Miercoles","Jueves","Viernes"]

def Cargar_Dato (mat):
    print (f"Cargar Datos")
    
    for i in range (FILAS):
        print (f"Repartidor {i+1}")
        for j in range (COLUMNAS):
            valor_valido = False
            
            while valor_valido == False:
                dato = int (input(f"Ingresar cantidad de paquetes: "))
                if dato >= 0:
                    mat[i][j] = dato
                    valor_valido = True
                else:
                    print (f"Valor invalido, intente nuevamente")

                    
        
def Mostrar_Dato (mat):
    print (f"Muestra de entregas")
    
    for i in range (FILAS):
        print  (f"Repartidor {i+1}")
        for j in range (COLUMNAS):
            print(f"{dias[j]}: {mat[i][j]}")
    

def Total_por_repartidor (mat):
    acumulador = [0]*3
    for i in range ( FILAS):
        for j in range(COLUMNAS):
            acumulador[i] += mat[i][j]
    
    return acumulador


entregas = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]

salir = False
while salir == False:
    print(f"Menu Principal\n[1] Cargar\n[2] Mostrar\n[3] Total por repartidor\n[4] Sair")    
    
    opcion = int(input (f"Ingrese opcion: "))
    match opcion:
        
        case 1:
            Cargar_Dato(entregas)
        
        case 2:
            Mostrar_Dato(entregas)
        
        case 3:
            Totales=Total_por_repartidor(entregas)
            print (f"Total por repartidor")
            for i in range (FILAS):
                print (f"Repartidor {i+1}: {Totales[i]}")
        case 4:
            salir=True