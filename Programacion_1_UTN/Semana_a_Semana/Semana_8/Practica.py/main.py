# Listas dinamicas
# 1 mutables
# 2 heterogenias
# 3 ordenadas 
# 4 indexables

ejemplo_lista = []
ejemplo_lista = list()
ejemplo_lista = [159,True,"cadena"]

# Tuplas
# 1 inmutables
# 2 ordenadas
# 3 heterogenias
# 4 indexables
# 5 iterables
"""
unas vez declaradas no se pueden cambiar el contenido de las mismas
para cambiar el contenido de las tuplas tenemos que crear una nueva para luego modificarlas 

"""
ejemplo_tuplas = ("nombre", 85)

#pasaje de tupla a lista y biceversa
nueva_tupla = tuple(ejemplo_lista)

nueva_lista = list(nueva_tupla)
nueva_lista = ["Pedro",35]
tupla_modificada = tuple(nueva_lista)

# Conjuntos 
# 1 No ordenados
# 2 No admite repetidos
# 3 Heterogenios - No se recomienda ya que no es una buena practica
# 4 No indexables
# 5 Mutables
# 6 Son iterables

ejemplo_conjunto = set()
ejemplo_conjunto = {1,4,6} #es un diccionario NO un conjuto

#pasaje de lista a conjunto 
print ("___________________")
lista_lenguajes=[]
while True:
    lenguaje = input("Ingrese lenguajes: ")
    if lenguaje == " ":
        break
    lista_lenguajes.append(lenguaje)
set_lenguaje = set(lista_lenguajes)
#print (set_lenguaje)
"""
se utiliza el set para que muestre solamente los valores unicos, osea que no sea ningun dato repetido
ya que los set (conjuntos) solo muestran o se quedan con los elementos unicos sin repeticiones
muy util para evitar usar una linea de codigo y verificar cada elemento que hay en la lista
"""
lista_ordenada = list (set_lenguaje)
lista_ordenada.sort()
#print(lista_ordenada)

"""
el elemento sort es para que se ordene los elementos de forma numerica o alfabetica
"""

# Diccionarios
# 1 Mutables 
# 2 Ordenados


ejemplo_diccionario = {}
ejemplo_diccionario = dict()
ejemplo_diccionario = {
    "peliculas" : ["Terminator", "Harry Potter", "Avatar"],
    "series" : {"Friends", "dragon ball"},
    "precios" : (2000,2500),
    "categorias" : {1:"terror",2:"comeddia", 3 : "suspenso"}
}

ejemplo_diccionario["URL"]="www.sitio.com"
ejemplo_diccionario["peliculas"].append("Sustancia")
ejemplo_diccionario["series"].add("Lost")
print (ejemplo_diccionario["categorias"][1])
print(ejemplo_diccionario)
"""
se manejan por pares pareja valor, ejemplo una clave numerica para ingresar al valor de la clase
separando entre (:) y las comas para separar los pares
"""
for i in ejemplo_diccionario["categorias"].values():
    print (i)
