#Validar que los textos no esten en blanco, o que los numeros son numeros y cada archivo este en forma para seguir

#

def validar_numero(texto):
    return texto.isdigit()
# ISDIGIT HACE:
#le mando un texto que es STR y retorna en verdadero si ese STR es un DIGITO
#Chequea si lo que tiene adentro un digito y no una letra del alfabeto 

def validar_texto_vacio (texto):
    return texto.strip () != ""
# Strip lo que hace es sacarle todos los espacios que tenga antes o despues la columna de caracteres
#Si esta vacio el dato retorna un false de lo contrario un true

def validar_catalogo_vacio (lista):
    if len(lista) == 0:
        print ("No hay juegos registrados...")
        return False
    return True

# preguntamos que si el tanaño de nuestra lista es = 0 osea no hay elementos de la lista, y de lo contrario retorna true diciendo que hay elementos en la lista

def validar_positivo(numero):
    valor = int (numero)
    return valor > 0 