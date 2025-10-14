# set se puede analizar como un conjunto, no permite duplicado de datos , si hay mas de un elemento va a entender que son el mismo 

#si queremos declarar un set siempre es por llaves {}
numeros_pares ={0,2, 4, 6}
numeros_impares = {0,1,3,5}

conjunto_vacio = set () #para declarar un set vacio se usa PARENTESIS

# metodos  mas importantes
#-----------------------------

#union () 
#Se utiliza para unir los conjuntos antes asignados
#ambas versiones estan bien usadas dependiento de lo que resulte mas comodo puede usarse una u otra 
conjunto_total = numeros_pares.union(numeros_impares)
conjunto_total = numeros_pares | numeros_impares

#-----------------------------

# add()
#agrega a lo ultimo del set
conjunto_total.add (3)
#en este caso no se agrega el tres porque detecta que esta presente el valor antes dado, no pueden haber valores iguales en el mismo conjunto
conjunto_total.add (15)
#en este caso lo agregaria a lo ultimo ya que no esta presente en el conjuto

#-----------------------------

#discard ()
conjunto_total.discard(15)
# si el elemento no existe NO TIRA ERROR

#-----------------------------

# remove ()
conjunto_total.remove(15)
#si el elemento no existe en el conjunto TIRA ERROR

#-----------------------------

#pop()
#elimina un element pero retornandolo por una ultima vez antes de eliminarlo
conjunto_total.add(15)
elemento = conjunto_total.pop(15)

#-----------------------------

#difference
# retorna solo los elementos que hay en un solo conjunto
conjunto_diferencia =  numeros_impares.difference(numeros_pares) #{1,3,5}
conjunto_diferencia_2 = numeros_pares.difference(numeros_impares) #{2,4,6}
#IMPORTANTE EL ORDEN DE LOS CONJUNTOS, retorna los elementos del primero conjuntos pero que no estan en el segundo
# Otra manera de escribir
conjunto_diferencia = numeros_impares - numeros_pares


#-----------------------------

#intersection()
#lo mismo que las intersecciones en los conjuntos, lo que retorna es aquellos valores que tienen iguales ambos conjuntos (la interseccion entre los dos)
conjunto_inter = numeros_pares.intersection(numeros_impares)
conjunto_inter = numeros_pares & numeros_impares

#-----------------------------

#clear()
# borra todos los elementos que hay en el conjunto
conjunto_total.clear() 
#pero manteniendo el set

#-----------------------------

#Pasaje de lista a conjuto y biseversa
lista = [1,5,1,3,4,8,8,10]
conjunto_lista = set(lista)
lista_sin_duplicados = list(conjunto_lista)
#se filtran los duplicados sin necesidad de una linea de codigo mas engorrosa

#-----------------------------

#update()
conjunto_extra = {10,20,30}
conjunto_extra.update (lista_sin_duplicados)
#lo que hicimos es agregar varios elementos al mismo tiempo en el conjunto extra, es como hacer un add, pero podemos agregar elementos varios en la linea de codigo

#-----------------------------