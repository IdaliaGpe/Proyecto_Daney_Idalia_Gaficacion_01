def colision(posicion_1, posicion_2, max_width_1, max_width_2, max_height_1, max_height_2):
    colisionando = False

    #Posicion x
    if (posicion_1[0] + max_width_1 > posicion_2[0] - max_width_2 
    and posicion_1[0] - max_width_1 < posicion_2[0] + max_width_2 
    
    #Posicion y
    and posicion_1[1] + max_height_1> posicion_2[1] - max_height_2 
    and posicion_1[1] - max_height_1< posicion_2[1] + max_height_2):
        colisionando = True
        
    return colisionando
