#🎵 Playlist de Lady Gaga - Gestor de Videos en YouTube 🎶
#Lady Gaga es una de las artistas más influyentes del pop, con una extensa lista de reproducciones en YouTube. Para facilitar el análisis y manipulación de su contenido, desarrollaremos un software que permita gestionar su lista de videos.
#A través de un menú interactivo, los usuarios podrán visualizar, ordenar, buscar y analizar la información de cada video de la lista.
#📌 Funcionalidades del Software
#🔹 1. Normalización de Datos
#El formato original de los datos no está estandarizado, por lo que se deben normalizar utilizando funciones preexistentes. Cada video deberá contener la siguiente información correctamente estructurada:
#Título (str): Nombre del tema.
#Colaboradores (list): Lista de artistas invitados (si los hay).
#Vistas (int): Cantidad de reproducciones en números enteros.
#Duración (int): Duración del video en segundos.
#Link (str): Enlace directo al video en YouTube.
#Fecha de lanzamiento (date): Fecha de publicación del video.
playlist_lady_gaga = [
    {
        "Tema": "Colby O'Donis | Akon - Just Dance",
        "Vistas": "300 millones",
        "Duracion": "4:01",
        "Link Youtube": "https://www.youtube.com/watch?v=2Abk1jAONjw",
        "Fecha lanzamiento": "2008-04-08"
    },
    {
        "Tema": "Poker Face",
        "Vistas": "1200 millones",
        "Duracion": "3:57",
        "Link Youtube": "https://www.youtube.com/watch?v=bESGLojNYSo",
        "Fecha lanzamiento": "2008-09-26"
    },
    {
        "Tema": "Eh, Eh (Nothing Else I Can Say)",
        "Vistas": "50 millones",
        "Duracion": "2:55",
        "Link Youtube": "https://www.youtube.com/watch?v=6yP4Nm86yk0",
        "Fecha lanzamiento": "2009-01-10"
    },
    {
        "Tema": "LoveGame",
        "Vistas": "100 millones",
        "Duracion": "3:36",
        "Link Youtube": "https://www.youtube.com/watch?v=lv5RJ1q8u3I",
        "Fecha lanzamiento": "2009-03-24"
    },
    {
        "Tema": "Paparazzi",
        "Vistas": "300 millones",
        "Duracion": "3:28",
        "Link Youtube": "https://www.youtube.com/watch?v=d2smz_1L2_0",
        "Fecha lanzamiento": "2009-07-06"
    },
    {
        "Tema": "Bad Romance",
        "Vistas": "1300 millones",
        "Duracion": "4:54",
        "Link Youtube": "https://www.youtube.com/watch?v=qrO4YZeyl0I",
        "Fecha lanzamiento": "2009-10-26"
    },
    {
        "Tema": "Beyoncé | Kanye West - Telephone",
        "Vistas": "500 millones",
        "Duracion": "3:40",
        "Link Youtube": "https://www.youtube.com/watch?v=EVBsypHzF3U",
        "Fecha lanzamiento": "2010-01-26"
    },
    {
        "Tema": "Alejandro",
        "Vistas": "400 millones",
        "Duracion": "4:34",
        "Link Youtube": "https://www.youtube.com/watch?v=niqrrmev4mA",
        "Fecha lanzamiento": "2010-04-20"
    },
    {
        "Tema": "Born This Way",
        "Vistas": "400 millones",
        "Duracion": "4:20",
        "Link Youtube": "https://www.youtube.com/watch?v=wV1FrqwZyKw",
        "Fecha lanzamiento": "2011-02-11"
    },
    {
        "Tema": "Judas",
        "Vistas": "300 millones",
        "Duracion": "4:09",
        "Link Youtube": "https://www.youtube.com/watch?v=wagn8Wrmzuc",
        "Fecha lanzamiento": "2011-04-15"
    },
    {
        "Tema": "The Edge of Glory",
        "Vistas": "200 millones",
        "Duracion": "5:20",
        "Link Youtube": "https://www.youtube.com/watch?v=QeWBS0JBNzQ",
        "Fecha lanzamiento": "2011-05-09"
    },
    {
        "Tema": "You and I",
        "Vistas": "150 millones",
        "Duracion": "5:07",
        "Link Youtube": "https://www.youtube.com/watch?v=X9YMU0WeBwU",
        "Fecha lanzamiento": "2011-08-23"
    },
    {
        "Tema": "Applause",
        "Vistas": "400 millones",
        "Duracion": "3:32",
        "Link Youtube": "https://www.youtube.com/watch?v=GuJQSAiODqI",
        "Fecha lanzamiento": "2013-08-12"
    },
    {
        "Tema": "R. Kelly | Christina Aguilera - Do What U Want",
        "Vistas": "100 millones",
        "Duracion": "3:47",
        "Link Youtube": "https://www.youtube.com/watch?v=1Ek5QdDjeQ4",
        "Fecha lanzamiento": "2013-10-21"
    },
    {
        "Tema": "G.U.Y.",
        "Vistas": "80 millones",
        "Duracion": "3:52",
        "Link Youtube": "https://www.youtube.com/watch?v=PNu_-deVemE",
        "Fecha lanzamiento": "2014-03-28"
    },
    {
        "Tema": "Perfect Illusion",
        "Vistas": "200 millones",
        "Duracion": "3:02",
        "Link Youtube": "https://www.youtube.com/watch?v=9Y8Vx7wr93s",
        "Fecha lanzamiento": "2016-09-09"
    },
    {
        "Tema": "Million Reasons",
        "Vistas": "600 millones",
        "Duracion": "3:25",
        "Link Youtube": "https://www.youtube.com/watch?v=8NUBicVpW9s",
        "Fecha lanzamiento": "2016-10-06"
    },
    {
        "Tema": "Joanne (Where Do You Think You're Goin'?)",
        "Vistas": "50 millones",
        "Duracion": "4:39",
        "Link Youtube": "https://www.youtube.com/watch?v=7HmiFxqdgq4",
        "Fecha lanzamiento": "2018-02-22"
    },
    {
        "Tema": "Bradley Cooper | Lukas Nelson - Shallow",
        "Vistas": "1900 millones",
        "Duracion": "3:37",
        "Link Youtube": "https://www.youtube.com/watch?v=bo_efYhYU2A",
        "Fecha lanzamiento": "2018-09-27"
    },
    {
        "Tema": "Always Remember Us This Way",
        "Vistas": "700 millones",
        "Duracion": "3:30",
        "Link Youtube": "https://www.youtube.com/watch?v=5XK4v2fgMPU",
        "Fecha lanzamiento": "2018-10-05"
    },
    {
        "Tema": "Stupid Love",
        "Vistas": "300 millones",
        "Duracion": "3:13",
        "Link Youtube": "https://www.youtube.com/watch?v=5L6xyaeiV58",
        "Fecha lanzamiento": "2020-02-28"
    },
    {
        "Tema": "Ariana Grande | Dua Lipa - Rain On Me",
        "Vistas": "700 millones",
        "Duracion": "3:02",
        "Link Youtube": "https://www.youtube.com/watch?v=AoAm4om0wTs",
        "Fecha lanzamiento": "2020-05-22"
    },
    {
        "Tema": "BLACKPINK | Selena Gomez - Sour Candy",
        "Vistas": "500 millones",
        "Duracion": "2:37",
        "Link Youtube": "https://www.youtube.com/watch?v=8kJ7qD5q6Qk",
        "Fecha lanzamiento": "2020-05-28"
    },
    {
        "Tema": "911",
        "Vistas": "100 millones",
        "Duracion": "2:52",
        "Link Youtube": "https://www.youtube.com/watch?v=4I0D2lO9JhA",
        "Fecha lanzamiento": "2020-09-18"
    },
    {
        "Tema": "Hold My Hand (Top Gun: Maverick)",
        "Vistas": "50 millones",
        "Duracion": "3:45",
        "Link Youtube": "https://www.youtube.com/watch?v=Y4cRx19nhJg",
        "Fecha lanzamiento": "2022-05-03"
    },
    {
        "Tema": "The Weeknd | Elton John - Electric Dreams",
        "Vistas": "10 millones",
        "Duracion": "3:45",
        "Link Youtube": "https://www.youtube.com/watch?v=ficticio2024",
        "Fecha lanzamiento": "2024-03-15"
    },
    {
        "Tema": "Dua Lipa | Bruno Mars - Neon Hearts",
        "Vistas": "25 millones",
        "Duracion": "4:12",
        "Link Youtube": "https://www.youtube.com/watch?v=ficticio2024b",
        "Fecha lanzamiento": "2024-07-20"
    },
    {
        "Tema": "Ariana Grande | The Weeknd - Starlight",
        "Vistas": "15 millones",
        "Duracion": "3:50",
        "Link Youtube": "https://www.youtube.com/watch?v=ficticio2024c",
        "Fecha lanzamiento": "2024-11-01"
    },
    {
        "Tema": "Dua Lipa | Sia - Electric Love",
        "Vistas": "20 millones",
        "Duracion": "3:30",
        "Link Youtube": "https://www.youtube.com/watch?v=ficticio2025a",
        "Fecha lanzamiento": "2025-02-14"
    },
    {
        "Tema": "The Weeknd | Ariana Grande - Midnight Sky",
        "Vistas": "30 millones",
        "Duracion": "4:00",
        "Link Youtube": "https://www.youtube.com/watch?v=ficticio2025b",
        "Fecha lanzamiento": "2025-06-10"
    }
]

Titulo = []
Colaboradores = []
Vistas = []
Duracion = []
Link = []
Fecha_de_lanzamiento = []

def Normalizacion_de_Datos ():
    for i in range (len(playlist_lady_gaga)):
        Cancion = playlist_lady_gaga[i]
        tema = Cancion["Tema"]
        
        flag_tema = False
        for i in range (len(tema)):
            if tema[i] != "-":
                True
            elif tema [i] == "-":
                lugar_del_separador = i
                break
        if flag_tema == True:
            titulo_del_tema = tema
        else:
            for i in range (lugar_del_separador+1,len(tema)):
                titulo_del_tema += tema[i]
        
        
        Titulo.append(titulo_del_tema)
        
        
        
        Colaboradores.append (Cancion["Tema"])
        
        
        Vistas.append (Cancion (int["Vistas"]))
        Duracion.append (Cancion(int["Duracion"]))
        Link.append (Cancion["Link Youtube"])
        Fecha_de_lanzamiento.append (Cancion ["Fecha lanzamiento"])
    
    return Titulo, Colaboradores, Vistas, Duracion, Link, Fecha_de_lanzamiento

Normalizacion_de_Datos()
#🔹 2. Mostrar Lista de Temas
#Se presentará la lista de todos los temas en formato tabular. No es necesario mostrar todos los datos, solo los esenciales (por ejemplo, título y duración).

#🔹 3. Ordenar Temas
#Los videos se ordenarán por duración, de mayor a menor.
#🔹 4. Promedio de Vistas
#Se calculará y mostrará el promedio de vistas de todos los videos en millones.
#🔹 5. Máxima Reproducción
#Se listará el video (o los videos) con la mayor cantidad de vistas.
#🔹 6. Mínima Reproducción
#Se listará el video (o los videos) con la menor cantidad de vistas.
#🔹 7. Búsqueda por Código
#El usuario ingresará un código de video y el programa mostrará todos los detalles asociados a ese video.
#
#🔹 8. Listar por Colaborador
#El usuario ingresará el nombre de un colaborador (de una lista de colaboradores existentes) y el programa mostrará todos los videos en los que haya participado.
#🔹 9. Listar por Mes de Lanzamiento
#El usuario ingresará un mes y se listarán todos los temas lanzados en ese mes, sin importar el año.
#🔹 10. Salir
#Finalizar la ejecución del programa.
#📌 Requisitos del Desarrollo
#✅ Estructura Modular: Cada funcionalidad deberá estar programada en funciones específicas para facilitar la reutilización del código.
#✅ Manejo de Datos: Validar correctamente los formatos de entrada y realizar conversiones cuando sea necesario.
#✅ Interfaz Clara: Los menús y las opciones deberán ser intuitivos y fáciles de usar.
#✅ Optimización de búsquedas: Garantizar eficiencia en las consultas sobre la lista de videos.
#LINK AL ARCHIVO
