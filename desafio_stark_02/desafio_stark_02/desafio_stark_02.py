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

from funciones_data_02 import *
from data_stark import lista_personajes


#I. Listar todos los superhéroes agrupados por color de ojos.

# Crear un diccionario vacío para agrupar personajes por tipo de inteligencia
personajes_por_inteligencia = {}

# Iterar a través de la lista de personajes y agruparlos por tipo de inteligencia
for personaje in lista_personajes:
    nombre = personaje["nombre"]
    inteligencia = personaje["inteligencia"]
        
    if inteligencia in personajes_por_inteligencia:
        personajes_por_inteligencia[inteligencia].append(nombre)
    else:
        personajes_por_inteligencia[inteligencia] = [nombre]

# Imprimir la lista de personajes agrupados por tipo de inteligencia
for inteligencia, lista_personajes in personajes_por_inteligencia.items():
    print(f"Tipo de inteligencia: {inteligencia}")
    for personaje in lista_personajes:
        print(f" - {personaje}")



    
    
    


    



    
        
        
        




        

        

        



            
  


    
            
    