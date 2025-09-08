vec_numeros = [0] * 5 
vec_nombre = [""] * 5
vec_decimales = [0,0] *5 

# Manera que tiene la app para que pueda multiplicar las listas

cantidad_de_elementos = len(vec_decimales)#retorna la cantidad de elementos que tiene la lista

#Ingrese nota para cada posicion de la lista
for nota in range (len(vec_decimales)):
    vec_decimales[nota]= float(input("ingrese nota: "))

#Mostrar las notas
for nota in range (len (vec_decimales)):
    print (f"Nota {nota+1}: {vec_decimales[nota]}")

#promedio de notas
suma_nota=0
for nota in range (len(vec_decimales)):
    suma_nota += vec_decimales[nota]
promedio_alumno= suma_nota /len(vec_decimales)


#manera de validacion para ver si os valores rigen con algunos ffactores 
vec_estados = ["aprobado","Regular","libre"]
bandera_libre = False

for nota in range (len (vec_decimales)):
    if vec_decimales[nota]<4:
        estado = vec_estados[2]
        bandera_libre=True
        break
    
if not bandera_libre:
    if promedio_alumno>=7:
        estado= vec_estados [0]
    elif promedio_alumno >=4:
        estado =vec_estados[1]
        
print (f"estado del alumno {estado}")

def cargar_nota_alumno( i:len):
    print (f"Alumno {i+1}")
    programacion= float (input("Ingrese la nota de programacion: "))
    ingles = float (input("Ingrese la nota de ingles: "))
    return programacion, ingles

