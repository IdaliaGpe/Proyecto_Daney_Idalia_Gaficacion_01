def colision(posicion_1, posicion_2, max_width_1, max_width_2, max_height_1, max_height_2):
    
    colisionando = False
    print()
    print("Pos 1= ", posicion_1) 
    print("Pos 2= ", posicion_2) 

    print("Pos 1-= ", posicion_1[0] - max_width_1) 
    print("Pos 1+= ", posicion_1[0] + max_width_1) 
    print("Pos 2-= ", posicion_2[0] - max_width_2) 
    print("Pos 2+= ", posicion_2[0] + max_width_2) 
    # posicion x
    if (posicion_1[0] + max_width_1 > posicion_2[0] - max_width_2 
    and posicion_1[0] - max_width_1 < posicion_2[0] + max_width_2 
    # posicion y
    and posicion_1[1] + max_height_1> posicion_2[1] - max_height_2 
    and posicion_1[1] - max_height_1< posicion_2[1] + max_height_2):
        colisionando = True
    return colisionando
