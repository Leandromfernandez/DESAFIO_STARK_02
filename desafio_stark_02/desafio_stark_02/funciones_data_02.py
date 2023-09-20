def mostar_heroes_nb(lista:list) -> list:
    """ Recibe una lista de personajes - devuelve los nombre NB que se encuentren en la mista """
    lista_nombre_nb = []
    for personaje in lista:
        if personaje['genero'] == "NB":        
            nombre_nb = personaje['nombre']        
            lista_nombre_nb.append(nombre_nb)
    return lista_nombre_nb

#A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
def mostar_heroes_nb(lista:list) -> list:
    """ Recibe una lista de personajes - devuelve los nombre NB que se encuentren en la mista """
    lista_nombre_nb = []
    contador_nb = 0
    for personaje in lista:
        if personaje['genero'] == "NB":
            contador_nb += 1
            nombre_nb = personaje['nombre']        
            lista_nombre_nb.append(nombre_nb)    
    if contador_nb <= 0:
        mensaje = print("No hay heroes de genero NB")
    else:
        mensaje =(f'Los heroes de genero NB son los siguiente {lista_nombre_nb}')
    return mensaje

####################################################################################################
# B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
def mostrar_heroina_mas_alta(lista:list): 
    altura_femenino_max = None    
    for personaje in lista:
        if personaje['genero'] == "F":
            alturas = float(personaje['altura'])
            if altura_femenino_max == None or alturas > altura_femenino_max:
                altura_femenino_max = alturas
                nombre_femenino_max = personaje['nombre']
    print(f'La heroina mas alta es {nombre_femenino_max} y su altura es: {altura_femenino_max} Cm.')

####################################################################################################
#C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
def mostrar_heroe_mas_alto(lista:list):
    altura_masculino_max = None    
    for personaje in lista:
        if personaje['genero'] == "M":
            alturas = float(personaje['altura'])
            if altura_masculino_max == None or alturas > altura_masculino_max:
                altura_masculino_max = alturas
                nombre_masculino_max = personaje['nombre']
    print(f'El heroe mas alto es {nombre_masculino_max} y su altura es: {altura_masculino_max} Cm.')

####################################################################################################
#D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
def mostrar_heroe_mas_debil(lista:list): 
    fuerza_min = None
    for personaje in lista:
        if personaje['genero'] == "M":
            fuerza = int(personaje['fuerza'])
            if fuerza_min == None or fuerza < fuerza_min:
                fuerza_min = fuerza
                nombre_mas_debil = personaje['nombre']
    print(f'El heroe mas debil es {nombre_mas_debil} y su fuerza es {fuerza_min}')

####################################################################################################
#E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
def mostrar_heroe_nb_debil(lista:list):
    fuerza_min_nb = None
    contador_nb = 0
    for personaje in lista:
        if personaje['genero'] == "NB":
            fuerza = int(personaje['fuerza'])
            if fuerza_min_nb == None or fuerza < fuerza_min_nb:
                contador_nb += 1
                fuerza_min_nb = fuerza
                nombre_mas_debil_nb = personaje['nombre']    
    if contador_nb >= 1:
        mensaje = print(f'El heroe mas debil NB es {nombre_mas_debil_nb} y su fuerza es {fuerza_min_nb}')
    else:
        mensaje = print("No hay heores de genero NB")
    return mensaje

####################################################################################################
#F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB
def muestrar_promedio_fuerzas_nb(lista:list):
    acumulador_fuerzas = 0
    contador_nb = 0
    for personaje in lista:
        if personaje['genero'] == "NB":
            contador_nb += 1
            fuerza_nb = int(personaje['fuerza'])
            acumulador_fuerzas = acumulador_fuerzas + fuerza_nb    
    promedio_fuerzas_nb = acumulador_fuerzas / contador_nb
    mensaje = print(f'El promedio de la fuerza de los heroes de genero NB ES {promedio_fuerzas_nb}')
    return mensaje
    
# G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.            
def mostrar_tipo_color_ojos(lista:list):
    
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
        mensaje = print(f'CON COLOR DE OJOS {color} HAY {cantidad} SUPERHEROES')

    return mensaje

#H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
def mostrar_cantidad_colores_pelo(lista:list):
    
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
        mensaje = print(f'CON COLOR DE PELO {color} HAY {cantidad} SUPERHEROES')
    
    return mensaje   