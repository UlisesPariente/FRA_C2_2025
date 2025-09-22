def burbuja_ascendente(vec):
    tamaño = len(vec) #tamaño del vector
    for i in range (tamaño-1):
        for j in range (tamaño-i-1): 
            #porque cuando demos la vuelt le tenemos que restar el tamaño
            if vec[j] > vec[j+1]:
                vec[j], vec[j+1] = vec[j + 1], vec[j]
    
def burbuja_descendente(vec):
    tamaño = len(vec) #tamaño del vector
    for i in range (tamaño-1):
        for j in range (tamaño-i-1): 
            #porque cuando demos la vuelt le tenemos que restar el tamaño
            if vec[j] < vec[j+1]:
                vec[j], vec[j+1] = vec[j + 1], vec[j]

def burbuja_mejorada_numeros(vec):
    tam=len(vec)
    for i in range (tam-1):
        intercambio=False
        for j in range (tam-i-1):
            if vec[j] > vec[j+1]:
                vec[j], vec[j+1] = vec[j+1], vec[j]
                intercambio =True
        
        if not intercambio:
            print(i)
            break
        
def burbuja_mejorada_palabras(vec):
    tam=len(vec)
    for i in range (tam-1):
        intercambio=False
        for j in range (tam-i-1):
            
            if vec[j].lower() > vec[j+1].lower():
                vec[j], vec[j+1] = vec[j+1], vec[j]
                intercambio =True
        
        if not intercambio:
            print(i)
            break
        