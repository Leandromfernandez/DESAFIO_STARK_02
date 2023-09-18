""" Desafío #02:
Usando como base lo realizado en el anterior desafío realizar los siguientes
informes en un menú

A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género NB

B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F

C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M

D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M

E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB

F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB

G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.

H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.

I. Listar todos los superhéroes agrupados por color de ojos.

J. Listar todos los superhéroes agrupados por tipo de inteligencia

NOTA: Se debe aplicar el tema Funciones visto en clase para cada opción del menú """

from data_stark import lista_personajes

#A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
def mostar_heroes_nb(lista_personajes:list) -> list:
    """ Recibe una lista de personajes - devuelve los nombre NB que se encuentren en la mista """
    lista_nombre_nb = []
    contador_nb = 0
    for personaje in lista_personajes:
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
def mostrar_heroina_mas_alta(list:list): 
    altura_femenino_max = None    
    for personaje in lista_personajes:
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
    for personaje in lista_personajes:
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
    for personaje in lista_personajes:
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
    for personaje in lista_personajes:
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

mostrar_heroe_nb_debil(lista_personajes)




        

        

        



            
  


    
            
    