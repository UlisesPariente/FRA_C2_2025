import random

inicio_caras = 1
din_caras= 6

dado= random.randint ( inicio_caras,din_caras)

#print(dado)

lista_dados = []
for i in range  (2):
    lista_dados.append(random.randint(inicio_caras,din_caras))
#print (lista_dados)

numero_decimal = random.uniform(3,10)
print (numero_decimal)

#para numeros int usamos la radint y de lo contrario un float uniform

#para seleccionar un elemento al azar de la lista
lista_nombre = ["Oscar","Carlos","Matias","Yanina"]

#print (random,choice(lista_nombres))

mazo = ["1♥️","2♥️","3♥️","4♥️","5♥️","6♥️","7♥️","8♥️","9♥️","J♥️","Q♥️","K♥️"]

random.shuffle(mazo) # se mezclan rtodos los datos de la lista

print (mazo)

mano = random.sample (mazo,5)