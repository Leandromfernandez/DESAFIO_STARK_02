def mostar_heroes_nb(lista_personajes:list) -> list:
    """ Recibe una lista de personajes - devuelve los nombre NB que se encuentren en la mista """
    lista_nombre_nb = []
    for personaje in lista_personajes:
        if personaje['genero'] == "NB":        
            nombre_nb = personaje['nombre']        
            lista_nombre_nb.append(nombre_nb)
    return lista_nombre_nb