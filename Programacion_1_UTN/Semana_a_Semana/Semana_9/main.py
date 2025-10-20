
#Archivos
# * todo lo que guardamos en ele momento el programa elimina los datos al cerrar la data 
#pero los archivos hace que todo dato que ingresemos en el programa se guarden en el tiempo 
#haciendo que cuando cierres el programa perduren todos los datos en lo largo del tiempo

# APERTURA DEL ARCHIVO
# METODO //  funcion open (nombre o ruta del archivo, modo de apertura)

"""
    Parametros
        1. nombre o ruta del archivo
        
        2. modo de apertura 
            * r (read//leer)
            * w (write//escribir) "si el archivo no existe lo crea // si existe lo pisa"
            es decir sobreescribe y perdemos informacion anterior
            * a (append//agregar) "si el archivo existe lo agrega al final // si no existe lo crea"

    Cierre de archivo 
    * "siempre que se abra un archivo tiene que cerrarce para que no haya futuros errores"
        * METODO: 
            * close() 
"""
archivo = open ("personas.txt","w")
"""
tanto el nombre como el metodo son STR
    *al ser "w" pisa el anterior, perdiendo todo dato anterior!!!!!!
TXT: son archivos de texto no puede algo de caracter raros solo caracteres al ser archvos de texto
"""
archivo.write("voy a pisar")
archivo.writelines(["Pedro","Lopez","Mar Del Plata"])
# Podemos mandar una lista literal o declarando tambien una lista y colocamdno dentro del parentesis
# CUIDADO PORQUE PONE DE FORMA LITERAL TODOS LOS ELEMENTOS DE LA LISTA JUNTOS SIN SEPARACION.
archivo.write("\n")
archivo.writelines (["Pedro\n", "Lopez\n", "Mar del Plata\n"])
#se coloca el "\n" para que puedan separar cada variable de la lista
archivo.close()


#_______________________LECTURA___________________
nombre_archivo = "Personas.txt"
modo_lectura = "r"
arc=open (nombre_archivo,modo_lectura)
texto = arc.read()
#trae todo el contenido del texto
print(f"El contenido del archivo es: \n{texto}")

arc.close()

#____________________APPEND//AGREGAR AL FINAL_____________________
"""
with es una sentencia unica
cierra automaticamente el archivo // NO hace falta el close() en este caso

en el caso de haber una coneccion de archivo abierto de forma constante no se usaria este metodo


"""
with open (nombre_archivo,"a") as a:
    a.write ("agrego algo al final")


#___________________EJEMPLO___________________
#realizar un programa en donde solicite los nombres de los alumnos de un curso y los guarde en un archivo TXT.
# el corte de los ingreso se da con un nombre en blanco
# el programa debe pedir al usuario un nombre y mostrartodos los nombres almacenados, excepto los que coincidan con el ingresado
import funciones
#Cargar nombres
Nombre_Archivo = "nombres.txt"
funciones.cargar_nombres(Nombre_Archivo)

#pedir nombres para filtrar 
nombre_excluir= input("Ingrese nombre para filtrar:\n")

# mostrar contenido filtrado
funciones.mostrar_excepto_excluido(Nombre_Archivo,nombre_excluir)