#estan compuesto por clave y valor
#claves son unicas en los dictionarios, mediante la clave podemos acceder a la misma
#en este caso ese usa la clave de forma de indice para acceder al dictionario

#para generar un diccionario son estos metodos
diccionario = dict()
diccionario = {}
#clave seria lo que esta antes de los ":" y el valor es lo que le sigue
diccionario_persona =  {
    "nombre" : "Salvador",
    "edad" : 26,
    "estado" : True
}
lista_personas = [
    {"nombre" : "Salvador",
     "edad" : 26,
     "estado" : True},
    {"nombre" : "Maria",
     "edad" : 30,
     "estado" : False}
]

#-----------------------------

# KEYS
# es un objeto iterable pero no es una lista
#ESTO ES PARA OBTENER TODAS LAS CLAVES EN EL DICCIONARIO
claves = diccionario_persona.keys()
lista_claves = list(claves)

#-----------------------------

#VALUES
# es un objeto iterable pero no es una lista
# EN ESTE CASO ES SOLO PARA OBTENER LOS VALORES IGNORANDO LAS KEYS
valores = diccionario_persona.values()
lista_valores = list(valores)

#-----------------------------

#ITEMS
# es un bjeto iterable de un diccionario
# EN ESTE CASO HACE INMUTABLES LOS VALORES PERO MUESTRA TODOS LOS VALORES TANTO LOS KEYS COMO VALUES EN FORMATO DE DUPLAS 
pares =  diccionario_persona.items()
lista_pares = list(pares)

#-----------------------------

#solo muestra los valores de los diccionarios
for i in diccionario_persona.values():
    print (i)
    
#-----------------------------
#se accede a las claves con "[]" para que sea mas comodo a la hora de las claves
nombre = diccionario_persona["nombre"]

#-----------------------------

#PARA AGREGAR UNA CLAVE Y VALOR EN EL DICCIONARIO
# SE AGREGA A LO ULTIMO del diccionario
diccionario_persona ["carrera"] = "TUP"

