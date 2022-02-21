from OpenGL.GL import *
from glew_wish import *

import glfw
import colision as col
import math
import main_juego as man

#FONDO LINEAS
d_posicion_c1 = [-0.6, 0, 0.0]
d_posicion_c2 = [-0.90, 0.3, 0.0]
d_posicion_c3 = [-0.90, -0.3, 0.0]
d_posicion_c4 = [-0.2, 0, 0.0] #ho
d_posicion_c5 = [-0.5, 0.0, 0.0]
d_posicion_c6 = [-0.5, 0.5, 0.0]
d_posicion_c7 = [-0.1, 0.2, 0.0]
d_posicion_c8 = [-0.1, -0.2, 0.0]
d_posicion_c9 = [0.2, 0.14, 0.0] #ho
d_posicion_c10 = [0.29, 0.5, 0.0]
d_posicion_c11 = [0.6, 0, 0.0] #ho
d_posicion_c12 = [0.7, 0.0, 0.0]
d_posicion_c13 = [0.7, -0.4, 0.0]
d_posicion_c14 = [0.4, 0.8, 0.0]

#FONDOS CUADROS
posicion_cuadrado_G = [0.0, 0.6, 0.0]
posicion_cuadrado_G2 = [0.35, 0.648, 0.0]

posicion_trianguloA = [-0.1, 0.39, 0.0]
posicion_trianguloA2 = [0.0, 0.39, 0.0]
posicion_trianguloA3 = [0.1, 0.39, 0.0]
posicion_trianguloA4 = [0.2, 0.488, 0.0]
posicion_trianguloA5 = [0.3, 0.488, 0.0]
posicion_trianguloA6 = [0.4, 0.488, 0.0]
posicion_trianguloA7 = [0.5, 0.488, 0.0]

#FONDO ROMBO
posicion_rombo = [-0.6, 0.05, 0.0]
posicion_rombo2 = [-0.6, 0.05, 0.0]

#TRIANGULOS ADORNOS
posicion_trianguloA2_1 = [-0.1, 0.81, 0.0]
posicion_trianguloA2_2 = [0.0, 0.835, 0.0]
posicion_trianguloA2_3 = [0.1, 0.849, 0.0]
posicion_trianguloA2_4 = [0.2, 0.785, 0.0]
posicion_trianguloA2_5 = [0.3, 0.785, 0.0]

##
##
##
##

def draw_fondo_animado(rotacion_rombo, rotacion_rombo1):

    glPushMatrix()
    glTranslatef(d_posicion_c1[0], d_posicion_c1[1], 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.628,0.121,1.0)

    glVertex3f(-0.01,1.0,0.0)
    glVertex3f(0.01,1.0,0.0)
    glVertex3f(0.01,-0.55,0.0)
    glVertex3f(-0.01,-0.55,0.0)
    glEnd()
    glPopMatrix()

    ##Ver
    glPushMatrix()
    glTranslatef(d_posicion_c2[0], d_posicion_c2[1], 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.628,0.121,1.0)

    glVertex3f(-0.1,0.01,0.0)
    glVertex3f(0.3,0.01,0.0)
    glVertex3f(0.3,-0.01,0.0)
    glVertex3f(-0.1,-0.01,0.0)
    glEnd()
    glPopMatrix()

    ##Ver
    glPushMatrix()
    glTranslatef(d_posicion_c3[0], d_posicion_c3[1], 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.628,0.121,1.0)

    glVertex3f(-0.1,0.01,0.0)
    glVertex3f(0.3,0.01,0.0)
    glVertex3f(0.3,-0.01,0.0)
    glVertex3f(-0.1,-0.01,0.0)
    glEnd()
    glPopMatrix()

    ##Ho
    glPushMatrix()
    glTranslatef(d_posicion_c4[0], d_posicion_c4[1], 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.628,0.121,1.0)

    glVertex3f(-0.01,1.0,0.0)
    glVertex3f(0.01,1.0,0.0)
    glVertex3f(0.01,-1.0,0.0)
    glVertex3f(-0.01,-1.0,0.0)
    glEnd()
    glPopMatrix()

    ##Ver
    glPushMatrix()
    glTranslatef(d_posicion_c5[0], d_posicion_c5[1], 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.628,0.121,1.0)

    glVertex3f(-0.1,0.01,0.0)
    glVertex3f(0.3,0.01,0.0)
    glVertex3f(0.3,-0.01,0.0)
    glVertex3f(-0.1,-0.01,0.0)
    glEnd()
    glPopMatrix()

    ##Ver
    glPushMatrix()
    glTranslatef(d_posicion_c6[0], d_posicion_c6[1], 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.628,0.121,1.0)

    glVertex3f(-0.1,0.01,0.0)
    glVertex3f(0.3,0.01,0.0)
    glVertex3f(0.3,-0.01,0.0)
    glVertex3f(-0.1,-0.01,0.0)
    glEnd()
    glPopMatrix()

    ##Ver
    glPushMatrix()
    glTranslatef(d_posicion_c7[0], d_posicion_c7[1], 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.628,0.121,1.0)

    glVertex3f(-0.1,0.01,0.0)
    glVertex3f(0.3,0.01,0.0)
    glVertex3f(0.3,-0.01,0.0)
    glVertex3f(-0.1,-0.01,0.0)
    glEnd()
    glPopMatrix()

    ##Ver
    glPushMatrix()
    glTranslatef(d_posicion_c8[0], d_posicion_c8[1], 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.628,0.121,1.0)

    glVertex3f(-0.1,0.01,0.0)
    glVertex3f(0.3,0.01,0.0)
    glVertex3f(0.3,-0.01,0.0)
    glVertex3f(-0.1,-0.01,0.0)
    glEnd()
    glPopMatrix()

    ##Ho
    glPushMatrix()
    glTranslatef(d_posicion_c9[0], d_posicion_c9[1], 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.628,0.121,1.0)

    glVertex3f(-0.01,0.35,0.0)
    glVertex3f(0.01,0.35,0.0)
    glVertex3f(0.01,-0.35,0.0)
    glVertex3f(-0.01,-0.35,0.0)
    glEnd()
    glPopMatrix()

    #Ver
    glPushMatrix()
    glTranslatef(d_posicion_c10[0], d_posicion_c10[1], 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.628,0.121,1.0)

    glVertex3f(-0.1,0.01,0.0)
    glVertex3f(0.3,0.01,0.0)
    glVertex3f(0.3,-0.01,0.0)
    glVertex3f(-0.1,-0.01,0.0)
    glEnd()
    glPopMatrix()

    ##Ho
    glPushMatrix()
    glTranslatef(d_posicion_c11[0], d_posicion_c11[1], 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.628,0.121,1.0)

    glVertex3f(-0.01,1.0,0.0)
    glVertex3f(0.01,1.0,0.0)
    glVertex3f(0.01,-0.55,0.0)
    glVertex3f(-0.01,-0.55,0.0)
    glEnd()
    glPopMatrix()

    #Ver
    glPushMatrix()
    glTranslatef(d_posicion_c12[0], d_posicion_c12[1], 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.628,0.121,1.0)

    glVertex3f(-0.1,0.01,0.0)
    glVertex3f(0.3,0.01,0.0)
    glVertex3f(0.3,-0.01,0.0)
    glVertex3f(-0.1,-0.01,0.0)
    glEnd()
    glPopMatrix()

    #Ver
    glPushMatrix()
    glTranslatef(d_posicion_c13[0], d_posicion_c13[1], 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.628,0.121,1.0)

    glVertex3f(-0.1,0.01,0.0)
    glVertex3f(0.3,0.01,0.0)
    glVertex3f(0.3,-0.01,0.0)
    glVertex3f(-0.1,-0.01,0.0)
    glEnd()
    glPopMatrix()

    #Ver
    glPushMatrix()
    glTranslatef(d_posicion_c14[0], d_posicion_c14[1], 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.628,0.121,1.0)

    glVertex3f(-0.6,0.01,0.0)
    glVertex3f(0.6,0.01,0.0)
    glVertex3f(0.6,-0.01,0.0)
    glVertex3f(-0.6,-0.01,0.0)
    glEnd()
    glPopMatrix()
    #############
    #############FIN DE LINEAS

    #cudrados
    glPushMatrix()
    glTranslatef(posicion_cuadrado_G[0], posicion_cuadrado_G[1], 0.0)
    glRotatef(180,1,1,0)
    glScalef(2,3,0)
    glBegin(GL_QUADS)
    glColor3f(0.167,0.003,0.359)

    glVertex3f(-0.08,0.05,0.0)
    glVertex3f(0.08,0.05,0.0)
    glVertex3f(0.08,-0.05,0.0)
    glVertex3f(-0.08,-0.05,0.0)
    glEnd()
    glPopMatrix()
    ##
    glPushMatrix()
    glTranslatef(posicion_cuadrado_G2[0], posicion_cuadrado_G2[1], 0.0)
    glRotatef(180,1,1,0)
    glScalef(1.4,4.0,0)
    glBegin(GL_QUADS)
    glColor3f(0.167,0.003,0.359)

    glVertex3f(-0.08,0.05,0.0)
    glVertex3f(0.08,0.05,0.0)
    glVertex3f(0.08,-0.05,0.0)
    glVertex3f(-0.08,-0.05,0.0)
    glEnd()
    glPopMatrix()

    #Triangulos azules
    glPushMatrix()
    glTranslatef(posicion_trianguloA[0], posicion_trianguloA[1], 0.0)
    glRotatef(180.0,1,0,0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.5,0.72,0.141)

    glVertex3f(-0.05,-0.05,0)
    glVertex3f(0,0.05,0)
    glVertex3f(0.05,-0.05,0)
    glEnd()
    glPopMatrix()
    ##
    glPushMatrix()
    glTranslatef(posicion_trianguloA2[0], posicion_trianguloA2[1], 0.0)
    glRotatef(180.0,1,0,0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.257,0.97,1)

    glVertex3f(-0.05,-0.05,0)
    glVertex3f(0,0.05,0)
    glVertex3f(0.05,-0.05,0)
    glEnd()
    glPopMatrix()
    ##
    glPushMatrix()
    glTranslatef(posicion_trianguloA3[0], posicion_trianguloA3[1], 0.0)
    glRotatef(180.0,1,0,0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.127,0.072,0.506)

    glVertex3f(-0.05,-0.05,0)
    glVertex3f(0,0.05,0)
    glVertex3f(0.05,-0.05,0)
    glEnd()
    glPopMatrix()
    ##
    glPushMatrix()
    glTranslatef(posicion_trianguloA4[0], posicion_trianguloA4[1], 0.0)
    glRotatef(180.0,1,0,0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.57,0.4,0.465)

    glVertex3f(-0.05,-0.05,0)
    glVertex3f(0,0.05,0)
    glVertex3f(0.05,-0.05,0)
    glEnd()
    glPopMatrix()
    ##
    glPushMatrix()
    glTranslatef(posicion_trianguloA5[0], posicion_trianguloA5[1], 0.0)
    glRotatef(180.0,1,0,0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.21,0.42,0.691)

    glVertex3f(-0.05,-0.05,0)
    glVertex3f(0,0.05,0)
    glVertex3f(0.05,-0.05,0)
    glEnd()
    glPopMatrix()
    ##
    glPushMatrix()
    glTranslatef(posicion_trianguloA6[0], posicion_trianguloA6[1], 0.0)
    glRotatef(180.0,1,0,0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.27,0.9,0.451)

    glVertex3f(-0.05,-0.05,0)
    glVertex3f(0,0.05,0)
    glVertex3f(0.05,-0.05,0)
    glEnd()
    glPopMatrix()
    ##
    glPushMatrix()
    glTranslatef(posicion_trianguloA7[0], posicion_trianguloA7[1], 0.0)
    glRotatef(180.0,1,0,0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.2,0.972,0.851)

    glVertex3f(-0.05,-0.05,0)
    glVertex3f(0,0.05,0)
    glVertex3f(0.05,-0.05,0)
    glEnd()
    glPopMatrix()

    ##
    ##
    ##
    ##Rombo
    glPushMatrix()
    glTranslatef(posicion_rombo[0], posicion_rombo[1], 0.0)
    glRotatef(rotacion_rombo, 0, 0.0, 1.0)
    glScalef(4.9,4.9,0)
    glBegin(GL_QUADS)
    glColor3f(0.0,0.0,1.0)

    glVertex3f(-0.05,0.05,0.0)
    glVertex3f(0.05,0.05,0.0)
    glVertex3f(0.05,-0.05,0.0)
    glVertex3f(-0.05,-0.05,0.0)
    glEnd()
    glPopMatrix()
    ##
    glPushMatrix()
    glTranslatef(posicion_rombo2[0], posicion_rombo2[1], 0.0)
    glRotatef(rotacion_rombo1, 0.0,0.0, 1.0)
    glScalef(1.9,1.9,0)
    glBegin(GL_QUADS)
    glColor3f(0.368,0.380,1.0)

    glVertex3f(-0.05,0.05,0.0)
    glVertex3f(0.05,0.05,0.0)
    glVertex3f(0.05,-0.05,0.0)
    glVertex3f(-0.05,-0.05,0.0)
    glEnd()
    glPopMatrix()
    ##
    ##
    ##
    ##
    ##TRIANGULOS ADORNOS
    #Triangulos2
    glPushMatrix()
    glTranslatef(posicion_trianguloA2_1[0], posicion_trianguloA2_1[1], 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.0,1.0,0.733)

    glVertex3f(-0.05,-0.05,0)
    glVertex3f(0,0.05,0)
    glVertex3f(0.05,-0.05,0)
    glEnd()
    glPopMatrix()
    ##
    glPushMatrix()
    glTranslatef(posicion_trianguloA2_2[0], posicion_trianguloA2_2[1], 0.0)
    glScalef(1,1.5,0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.749,1.0,0.933)

    glVertex3f(-0.05,-0.05,0)
    glVertex3f(0,0.05,0)
    glVertex3f(0.05,-0.05,0)
    glEnd()
    glPopMatrix()
    ##
    glPushMatrix()
    glTranslatef(posicion_trianguloA2_3[0], posicion_trianguloA2_3[1], 0.0)
    glScalef(1,1.8,0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.929,1.0,0.980)

    glVertex3f(-0.05,-0.05,0)
    glVertex3f(0,0.05,0)
    glVertex3f(0.05,-0.05,0)
    glEnd()
    glPopMatrix()
    ##
    glPushMatrix()
    glTranslatef(posicion_trianguloA2_4[0], posicion_trianguloA2_4[1], 0.0)
    glScalef(1,0.5,0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.2,0,0.8)

    glVertex3f(-0.05,-0.05,0)
    glVertex3f(0,0.05,0)
    glVertex3f(0.05,-0.05,0)
    glEnd()
    glPopMatrix()
    ##
    glPushMatrix()
    glTranslatef(posicion_trianguloA2_5[0], posicion_trianguloA2_5[1], 0.0)
    glScalef(1,0.5,0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.0,0,0.95)

    glVertex3f(-0.05,-0.05,0)
    glVertex3f(0,0.05,0)
    glVertex3f(0.05,-0.05,0)
    glEnd()
    glPopMatrix()