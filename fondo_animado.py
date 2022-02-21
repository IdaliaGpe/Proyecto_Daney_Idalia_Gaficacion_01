from OpenGL.GL import *
from glew_wish import *

import glfw
import colision as col
import math
import main_juego as man

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

def draw_fondo_animado():

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