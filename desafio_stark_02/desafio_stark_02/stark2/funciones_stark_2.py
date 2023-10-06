from data_stark import lista_personajes


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
# G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.


def mostrar_tipo_color_ojos(lista: list):

    lista_color_ojos = []
    conteo_colores = {}

    for personaje in lista:
        color_ojos_personajes = personaje['color_ojos']
        lista_color_ojos.append(color_ojos_personajes)

    for color in lista_color_ojos:
        if color in conteo_colores:
            conteo_colores[color] += 1
        else:
            conteo_colores[color] = 1

    for color, cantidad in conteo_colores.items():
        mensaje = print(
            f'CON COLOR DE OJOS {color} HAY {cantidad} SUPERHEROES')

    return mensaje


def mostrar_cantidad_colores_pelo(lista: list):

    lista_color_pelo = []
    conteo_colores_pelo = {}
    for personaje in lista:
        color_pelo = personaje['color_pelo']
        lista_color_pelo.append(color_pelo)

    for color in lista_color_pelo:
        if color in conteo_colores_pelo:
            conteo_colores_pelo[color] += 1
        else:
            conteo_colores_pelo[color] = 1

    for color, cantidad in conteo_colores_pelo.items():
        mensaje = print(
            f'CON COLOR DE PELO {color} HAY {cantidad} SUPERHEROES')

    return mensaje
