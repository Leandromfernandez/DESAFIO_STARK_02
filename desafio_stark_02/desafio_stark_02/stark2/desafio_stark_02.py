from data_stark import lista_personajes

"""
Desafío #02:
Usando como base lo realizado en el anterior desafío realizar los siguientes
informes en un menú
A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género NB
B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
género NB
G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
I. Listar todos los superhéroes agrupados por color de ojos.
J. Listar todos los superhéroes agrupados por tipo de inteligencia
NOTA: Se debe aplicar el tema Funciones visto en clase para cada opción del menú 
"""


def mostrar_heroe_nb(lista_personajes: list):
    contador_nb = 0
    for personaje in lista_personajes:
        genero = personaje['genero']
        if genero == "NB":
            contador_nb += 1
            nombre_nb = personaje['nombre']
            mensaje = f'N° {contador_nb}\n{nombre_nb} es de genero "NB"'
            print(mensaje)
    if contador_nb <= 0:
        print('No hay heroes del genero NB. ')
# B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F


def mostrar_heroina_mas_alta(lista_personajes: list):
    altura_max = None
    for personaje in lista_personajes:
        genero = personaje['genero']
        nombre = personaje['nombre']
        altura = round(float(personaje['altura']))
        if genero == "F":
            if altura_max == None or altura > altura_max:
                altura_max = altura
                nombre_mas_alta = f'El nombre de la heroina mas alta es {nombre}'
    print(nombre_mas_alta)
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M


def mostrar_heroe_mas_alto(lista_personajes: list):
    altura_max = None
    for personaje in lista_personajes:
        genero = personaje['genero']
        nombre = personaje['nombre']
        altura = round(float(personaje['altura']))
        if genero == "M":
            if altura_max == None or altura > altura_max:
                altura_max = altura
                nombre_mas_alta = f'El nombre del heroe mas alto es {nombre}'
    print(nombre_mas_alta)


# D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
def mostrar_heroe_mas_debil(lista_personajes: list):
    fuerza_min = None
    for personaje in lista_personajes:
        fuerza = int(personaje['fuerza'])
        nombre = personaje['nombre']
        genero = personaje['genero']
        if genero == "M":
            if fuerza_min == None or fuerza < fuerza_min:
                fuerza_min = fuerza
                nombre_fuerza_min = f'El mas debil es: {nombre},y su fuerza es: {fuerza_min} '
    print(nombre_fuerza_min)
# E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB


def mostrar_mas_debil_nb(lista_personajes: list):
    fuerza_min = None
    contador_nb = 0
    for personaje in lista_personajes:
        fuerza = int(personaje['fuerza'])
        nombre = personaje['nombre']
        genero = personaje['genero']
        if genero == "NB":
            contador_nb += 1
            if fuerza_min == None or fuerza < fuerza_min:
                fuerza_min = fuerza
                nombre_fuerza_min = f'El mas debil es: {nombre},y su fuerza es: {fuerza_min} '
    if contador_nb <= 0:
        print('No hay heroes del genero NB. ')
    else:
        print(nombre_fuerza_min)
# F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB


def mostrar_promedio_fuerzas_nb(lista_personajes: list):
    contador_nb = 0
    acumulador_fuerza_nb = 0
    promedio_fuerza_nb = 0
    for personaje in lista_personajes:
        genero = personaje['genero']
        fuerza = int(personaje['fuerza'])
        if genero == "NB":
            contador_nb += 1
            acumulador_fuerza_nb += fuerza
    if contador_nb >= 1:
        promedio_fuerza_nb = acumulador_fuerza_nb / contador_nb
        print(
            f'El promedio de las fuerzas de los heroes de genero NB es: {promedio_fuerza_nb} \nHay {contador_nb} heroes NB')
    else:
        print('No hay heroes del genero NB para promediar. ')
