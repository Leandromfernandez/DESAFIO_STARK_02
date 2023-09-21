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

while True:
    print(f'Menu de opciones')
    print(f'Opcion A - Imprimir el nombre de cada superhéroe de género NB')
    print(f'Opcion B - Mostrar heroina mas alta.')
    print(f'Opcion C - Recorrer la lista y determinar cuál es el superhéroe más alto de género M.')
    print(f'Opcion D - Recorrer la lista y determinar cuál es el superhéroe más débil de género M')
    print(f'Opcion E - Recorrer la lista y determinar cuál es el superhéroe más débil de género NB')
    print(f'Opcion F - Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB')
    print(f'Opcion G - Mostrar cuántos superhéroes tienen cada tipo de color de ojos.')
    print(f'Opcion H - Mostrar cuántos superhéroes tienen cada tipo de color de pelo.')
    print(f'Opcion I - Listar todos los superhéroes agrupados por color de ojos.')    
    print(f'Opcion J - Listar todos los superhéroes agrupados por tipo de inteligencia')    
    print(f'Opcion K - SALIR')    
    respuesta =input('Ingrese la opcion deseada: ').upper()   
    
    if respuesta == "A":
        mostar_heroes_nb(lista_personajes)
    elif respuesta == "B":
      mostrar_heroina_mas_alta(lista_personajes)
    elif respuesta == "C":
        mostrar_heroe_mas_alto(lista_personajes)        
    elif respuesta == "D":
        mostrar_heroe_mas_debil(lista_personajes)      
    elif respuesta == "E":
        mostrar_heroe_nb_debil(lista_personajes)
    elif respuesta == "F":
        muestrar_promedio_fuerzas_nb(lista_personajes)
    elif respuesta == "G":
        mostrar_tipo_color_ojos(lista_personajes)       
    elif respuesta == "H":
        mostrar_cantidad_colores_pelo(lista_personajes)
    elif respuesta == "I":
        muestra_grupos_color_ojos(lista_personajes)
    elif respuesta == "J":
        muestra_agrupados_por_inteligencia(lista_personajes)
    elif respuesta == "K":
        print(F'Hasta Pronto! ')
        break
    else:
        print("Opcion no valida. Ingrese nuevamente!. ")



    
        
        
        




        

        

        



            
  


    
            
    