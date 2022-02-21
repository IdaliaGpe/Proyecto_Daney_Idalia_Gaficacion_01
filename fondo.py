from OpenGL.GL import *
from glew_wish import *

import glfw
import colision as col
import math
import main_juego as man

#Base
posicion_plataforma = [0.0, -0.90, 0.0]
#Meta
posicion_meta = [0.95, -0.55, 0.0]
width_cuadrado_blanco = 0.05
height_cuadrado_blanco = 9.0

#Obstaculos
posicion_obstaculo_triangulo1 = [-0.6, -0.55, 0.0]
posicion_obstaculo_triangulo2 = [-0.5, -0.55, 0.0]
posicion_obstaculo_cuadrado1 = [-0.1, -0.55, 0.0]
posicion_obstaculo_cuadrado2 = [-0.0, -0.55, 0.0]
posicion_obstaculo_cuadrado3 = [-0.6, 0.09, 0.0]
posicion_obstaculo_triangulo3 = [-0.6, -0.0, 0.0]

posicion_obstaculo_triangulo4 = [0.5, -0.55, 0.0]
posicion_obstaculo_triangulo5 = [0.6, -0.55, 0.0]
posicion_obstaculo_cuadrado4 = [0.4, -0.55, 0.0]

lista_obstaculos = [posicion_obstaculo_triangulo1, posicion_obstaculo_triangulo2, posicion_obstaculo_cuadrado1, posicion_obstaculo_cuadrado2, 
posicion_obstaculo_cuadrado3, posicion_obstaculo_triangulo4, posicion_obstaculo_triangulo5, posicion_obstaculo_cuadrado4]

circualo_obstaculo_c3 = [-0.6, 0.09, 0.0]

def draw_fondo(posicion_cuadrado, window, posicion_respawn):
    #META
    glPushMatrix()
    glTranslatef(posicion_meta[0], posicion_meta[1], 0.0)
    glBegin(GL_QUADS)

    # #cerrar juego
    if col.colision(posicion_cuadrado, posicion_meta, posicion_cuadrado[3], width_cuadrado_blanco, posicion_cuadrado[4], height_cuadrado_blanco):
        glfw.set_window_should_close(window, 1)

    glColor3f(40/255, 50/255, 100/255)
    glVertex3f(-width_cuadrado_blanco, height_cuadrado_blanco, 0.0)
    glVertex3f(width_cuadrado_blanco, height_cuadrado_blanco, 0.0)
    glVertex3f(0.05,-0.05,0.0)
    glVertex3f(-0.05,-0.05,0.0)
    glEnd()

    glPopMatrix()

    #Triangulo1
    glPushMatrix()
    glTranslatef(posicion_obstaculo_triangulo1[0], posicion_obstaculo_triangulo1[1], 0.0)
    glBegin(GL_TRIANGLES)

    #Establecer color
    glColor3f(1,1,0)

    #Manda vertices a dibujar
    glVertex3f(-0.05,-0.05,0)
    glVertex3f(0,0.05,0)
    glVertex3f(0.05,-0.05,0)

    glEnd()
    glPopMatrix()

    # Triangulo2
    glPushMatrix()
    glTranslatef(posicion_obstaculo_triangulo2[0], posicion_obstaculo_triangulo2[1], 0.0)
    glBegin(GL_TRIANGLES)

    #Establecer color
    glColor3f(0.184,0.361,0.145)

    #Manda vertices a dibujar
    glVertex3f(-0.05,-0.05,0)
    glVertex3f(0,0.05,0)
    glVertex3f(0.05,-0.05,0)

    glEnd()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(posicion_obstaculo_cuadrado1[0], posicion_obstaculo_cuadrado1[1], 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.158,0.368,0.456)

    glVertex3f(-0.05,0.05,0.0)
    glVertex3f(0.05,0.05,0.0)
    glVertex3f(0.05,-0.05,0.0)
    glVertex3f(-0.05,-0.05,0.0)
    glEnd()
    glPopMatrix()
    #
    glPushMatrix()
    glTranslatef(posicion_obstaculo_cuadrado2[0], posicion_obstaculo_cuadrado2[1], 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.621,0.61,0.48)

    glVertex3f(-0.05,0.15,0.0)
    glVertex3f(0.05,0.15,0.0)
    glVertex3f(0.05,-0.05,0.0)
    glVertex3f(-0.05,-0.05,0.0)
    glEnd()
    glPopMatrix()
    #

    glPushMatrix()
    glTranslatef(posicion_obstaculo_cuadrado3[0], posicion_obstaculo_cuadrado3[1], 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.167,0.003,0.359)

    glVertex3f(-0.05,0.05,0.0)
    glVertex3f(0.05,0.05,0.0)
    glVertex3f(0.05,-0.05,0.0)
    glVertex3f(-0.05,-0.05,0.0)
    glEnd()
    glPopMatrix()
    #
    
    glPushMatrix()
    glTranslatef(posicion_obstaculo_triangulo3[0], posicion_obstaculo_triangulo3[1], 0.0)
    glRotatef(180.0,1,0,0)
    glBegin(GL_TRIANGLES)

    #Establecer color
    glColor3f(0.257,0.972,1)

    #Manda vertices a dibujarS
    glVertex3f(-0.05,-0.05,0)
    glVertex3f(0,0.05,0)
    glVertex3f(0.05,-0.05,0)

    glEnd()
    glPopMatrix()
    #
    #circunferecia 
    glPushMatrix()
    glTranslatef(circualo_obstaculo_c3[0], circualo_obstaculo_c3[1], 0.0)
    glBegin(GL_POLYGON)

    #A sin(2 pi f t + f)
    glColor3f(0.457,0.019,0.957)
    for angulo in range(0,359,5):
        glVertex3f(0.03*math.cos(angulo * math.pi / 180), 0.03*math.sin(angulo * math.pi / 180), 0)
    glEnd()
    glPopMatrix()

    #Triangulo1
    glPushMatrix()
    glTranslatef(posicion_obstaculo_triangulo4[0], posicion_obstaculo_triangulo4[1], 0.0)
    glBegin(GL_TRIANGLES)

    #Establecer color
    glColor3f(0.453,0.451,0.56)

    #Manda vertices a dibujar
    glVertex3f(-0.05,-0.05,0)
    glVertex3f(0,0.05,0)
    glVertex3f(0.05,-0.05,0)

    glEnd()
    glPopMatrix()

    #Triangulo1
    glPushMatrix()
    glTranslatef(posicion_obstaculo_triangulo5[0], posicion_obstaculo_triangulo5[1], 0.0)
    glBegin(GL_TRIANGLES)

    #Establecer color
    glColor3f(0.63,0.450,0.14)

    #Manda vertices a dibujar
    glVertex3f(-0.05,-0.05,0)
    glVertex3f(0,0.05,0)
    glVertex3f(0.05,-0.05,0)

    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(posicion_obstaculo_cuadrado4[0], posicion_obstaculo_cuadrado4[1], 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.45,0.1,0.186)

    glVertex3f(-0.05,0.15,0.0)
    glVertex3f(0.05,0.15,0.0)
    glVertex3f(0.05,-0.05,0.0)
    glVertex3f(-0.05,-0.05,0.0)
    glEnd()
    glPopMatrix()

    for obs in lista_obstaculos:
        if col.colision(posicion_cuadrado, obs, posicion_cuadrado[3], 0.05, posicion_cuadrado[4], 0.05):
            posicion_cuadrado = man.get_posicion_incial()


    #PLATAFORMA
    glPushMatrix()
    glTranslatef(posicion_plataforma[0], posicion_plataforma[1], 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(-1.0,0.30,0.0)
    glVertex3f(1.,0.30,0.0)
    glVertex3f(1.0,-0.30,0.0)
    glVertex3f(-1.0,-0.30,0.0)
    glEnd()

    glPopMatrix()
    return posicion_cuadrado