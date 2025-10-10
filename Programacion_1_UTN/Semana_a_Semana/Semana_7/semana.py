#se declara la lista vacia
lista_de_objetos = [] 
lista_de_objetos = list()

#------------------------------
lista_de_objetos.append("vaso") 
#agrega un elemento al final de la lista
#------------------------------
lista_de_objetos.extend ("kiwi")
#agrega un elemento al inicio de la lista
#------------------------------
lista_de_objetos.insert (1,"kiwi") 
#inserta un elemento a una posicion deseada
#------------------------------
lista_de_objetos.remove ("kiwi") 
#elimina un elemento para borrar pero unicamente se tiene que mandar el parametro no la ubicacion
#ademas elimina el primero que encuentre
#------------------------------
objeto = lista_de_objetos.pop (1)
#elimina pero retorna lo eliminado por una unica vez en la posicion asignada
#------------------------------
lista_de_objetos.clear 
#elimina todos los elementos de la lista
#------------------------------
objeto = lista_de_objetos.index ("kiwi",1)  
#devuelve la posicion 
#se puede asignar un inicio y final (elemento, inicio, final)
#------------------------------
numeros = [3,1,4,2]
numeros.sort ()
print(numeros) #[1,2,3,4]
#se ordena de menor a mayor tanto los INT como STR
#la unica condicion es que no sean mezclados 
#------------------------------
lista_de_objetos.reverse()
#da vuelta todos los elementos de la lista
#------------------------------
tupla = ("nombre", "43057298")
#tupla = tuple("nombre", "43057298")

nombre=tupla [0]
print (nombre)

#la tupla no se puede cambiar son inmutables 
#para no correr el riesgo de que alguien los cambie