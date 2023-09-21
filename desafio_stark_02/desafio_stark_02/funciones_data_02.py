#A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
def mostar_heroes_nb(lista:list) -> list:
    """
    La función `mostar_heroes_nb` toma una lista de personajes y devuelve los nombres de los personajes
    con el género "NB" en la lista.    
    """
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
    # El código busca la superheroína más alta (género "F") en la lista dada. Finalmente, imprime el nombre y la altura de la superheroína más alta.
    altura_femenino_max = None    
    for personaje in lista:
        if personaje['genero'] == "F":
            alturas = float(personaje['altura'])
            if altura_femenino_max == None or alturas > altura_femenino_max:
                altura_femenino_max = alturas
                nombre_femenino_max = personaje['nombre']
    mensaje = print(f'La heroina mas alta es {nombre_femenino_max} y su altura es: {altura_femenino_max} Cm.')
    return mensaje

####################################################################################################
#C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
def mostrar_heroe_mas_alto(lista:list):
# El código busca el superhéroe con mayor altura entre aquellos con el género "M" en la lista dada. Finalmente, imprime el nombre y la altura del superhéroe masculino más alto.
    altura_masculino_max = None    
    for personaje in lista:
        if personaje['genero'] == "M":
            alturas = float(personaje['altura'])
            if altura_masculino_max == None or alturas > altura_masculino_max:
                altura_masculino_max = alturas
                nombre_masculino_max = personaje['nombre']
    mensaje = print(f'El heroe mas alto es {nombre_masculino_max} y su altura es: {altura_masculino_max} Cm.')
    return mensaje

####################################################################################################
#D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
def mostrar_heroe_mas_debil(lista:list):    
    #Encuentra al superhéroe con menor fuerza entre aquellos con el género "M" en la lista dada    
    fuerza_min = None
    for personaje in lista:
        if personaje['genero'] == "M":
            fuerza = int(personaje['fuerza'])
            if fuerza_min == None or fuerza < fuerza_min:
                fuerza_min = fuerza
                nombre_mas_debil = personaje['nombre']
    mensaje = print(f'El heroe mas debil es {nombre_mas_debil} y su fuerza es {fuerza_min}')
    return mensaje

####################################################################################################
#E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
def mostrar_heroe_nb_debil(lista:list):
    # encuentra al superhéroe con menor fuerza ("fuerza") entre aquellos con el género "NB" en la lista dada.
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
   # El código la fuerza promedio de los superhéroes con el género "NB".   
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
    """
    El código cuenta la cantidad de superhéroes para cada color de ojos en la lista proporcionada. Crea
    una lista vacía llamada `lista_color_ojos` para almacenar los colores de ojos de los superhéroes.
    Luego, itera sobre cada superhéroe en la `lista` y recupera su color de ojos (`color_ojos`). El
    color de ojos se adjunta a `lista_color_ojos`.
    """    
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
    #Cuenta la cantidad de superhéroes para cada color de cabello en la lista proporcionada.    
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

#I
def muestra_grupos_color_ojos(lista: list):
    """ 
    El código está creando un diccionario llamado `color_ojos_personajes` para agrupar a los superhéroes
    por su color de ojos. Si el color de ojos ya existe como clave en el diccionario,agrega el nombre a la lista correspondiente. 
    Si el color de ojos aún no es una clave en el diccionario, crea un nuevo par clave-valor con el color de ojos como clave y una lista que contiene
    el nombre como valor. Finalmente, imprime el color de ojos y la correspondiente lista de nombres.
    """
    color_ojos_personajes = {}
    for personajes in lista:
        color_ojos = personajes["color_ojos"]
        nombre = personajes["nombre"]
        if color_ojos in color_ojos_personajes:
            color_ojos_personajes[color_ojos].append(nombre)
        else:
            color_ojos_personajes[color_ojos] = [nombre]    
    for color, nombre in color_ojos_personajes.items():     
       mensaje = print(f"los que tienen ojos {color} son: \n  {nombre}")
    return mensaje

#J
def muestra_agrupados_por_inteligencia(lista:list):
    """ 
     El código está creando un diccionario llamado "inteligencia_personajes" para agrupar a los
     superhéroes por su nivel de inteligencia.Si el nivel de inteligencia ya existe como clave en el diccionario, agrega el nombre a la lista
     correspondiente.
     Si el nivel de inteligencia aún no es una clave en el diccionario, crea un nuevo par clave-valor con el nivel de inteligencia como clave y una lista que contiene el nombre
     como valor. Finalmente, imprime el nivel de inteligencia y la lista de nombres correspondiente. 
     """
    inteligencia_personajes = {}
    for personajes in lista:
        inteligencia = personajes["inteligencia"]
        nombre = personajes["nombre"]
        if inteligencia in inteligencia_personajes:
            inteligencia_personajes[inteligencia].append(nombre)
        else:
            inteligencia_personajes[inteligencia] = [nombre]

    for inteligencia, nombre in inteligencia_personajes.items():     
        mensaje = print(f"los que tienen inteligencia tipo : {inteligencia} son: \n  {nombre}")
    return mensaje
