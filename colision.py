def colision(posicion_1, posicion_2, max_width_1, max_width_2, max_height_1, max_height_2):
    colisionando = False

    if (posicion_1[0] + max_width_1 > posicion_2[0] - max_width_2 
    and posicion_1[0] - max_width_1 < posicion_2[0] + max_width_2 
    
    #Posicion y
    and posicion_1[1] + max_height_1 > posicion_2[1] - max_height_2 
    and posicion_1[1] - max_height_1 < posicion_2[1] + max_height_2):
        colisionando = True

    return colisionando

# def colision_respawn(posicion_cuadrado, posicion_obstaculo):
#     colision_respawn = False

#     #Posicion x
#     if (posicion_cuadrado[0] + posicion_obstaculo[0] > posicion_cuadrado[0] - posicion_obstaculo[0]
#     and posicion_cuadrado[0] - posicion_obstaculo[0] < posicion_cuadrado[0] + posicion_obstaculo[0]
    
#     #Posicion y
#     and posicion_cuadrado[1] + posicion_obstaculo[1] >  posicion_cuadrado[1] - posicion_obstaculo[1]
#     and posicion_cuadrado[1] - posicion_obstaculo[1] < posicion_cuadrado[1] + posicion_obstaculo[1]):
#         colision_respawn = True

#     return colision_respawn