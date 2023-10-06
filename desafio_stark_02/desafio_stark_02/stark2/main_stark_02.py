from funciones_stark_2 import *
from data_stark import lista_personajes

while True:
    print('Menu de opciones')
    print('Opcion A - Imprimir nombres heroes de genero NB.')
    print('Opcion B - Mostrar heroina mas alta.')
    print('Opcion C - Mostrar heroe mas alto.')
    print('Opcion D - Mostrar heroe mas debil.')
    print('Opcion E - Mostrar heroe mas debil de genero NB')
    print('Opcion F - Mostrar promedio de FUERZA de genero NB.')
    print('Opcion G - Mostrar tipo de color de ojos.')
    print('Opcion H - Mostrar cantidad de tipo de color de pelo.')
    print('Opcion I - Salir.')

    respuesta = input('Ingrese la opcion deseada: ').upper()

    if respuesta == "A":
        mostrar_heroe_nb(lista_personajes)
    elif respuesta == "B":
        mostrar_heroina_mas_alta(lista_personajes)
    elif respuesta == "C":
        mostrar_heroe_mas_alto(lista_personajes)
    elif respuesta == "D":
        mostrar_heroe_mas_debil(lista_personajes)
    elif respuesta == "E":
        mostrar_mas_debil_nb(lista_personajes)
    elif respuesta == "F":
        mostrar_promedio_fuerzas_nb(lista_personajes)
    elif respuesta == "G":
        mostrar_tipo_color_ojos(lista_personajes)
    elif respuesta == "H":
        mostrar_cantidad_colores_pelo(lista_personajes)
    elif respuesta == "I":
        break
    else:
        print("La opcion elegida es inválida!. ")
