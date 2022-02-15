from sre_constants import JUMP
from OpenGL.GL import *
from glew_wish import *

import glfw
import colision as col
import main_juego as man

posicion_plataforma = [0.0, -0.90, 0.0]
posicion_meta = [0.95, -0.55, 0.0]

def draw_fondo(posicion_cuadrado, window):

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

    glBegin(GL_LINE_LOOP)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(-1.0,0.30,0.0)
    glVertex3f(1.,0.30,0.0)
    glVertex3f(1.0,-0.30,0.0)
    glVertex3f(-1.0,-0.30,0.0)
    glEnd()

    glPopMatrix()

    #META
    glPushMatrix()
    glTranslatef(posicion_meta[0], posicion_meta[1], 0.0)
    glBegin(GL_QUADS)

    #Establecer color    
    if col.colision(posicion_cuadrado, posicion_meta):
        glfw.set_window_should_close(window, 1)

    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.05,0.05,0.0)
    glVertex3f(0.05,0.05,0.0)
    glVertex3f(0.05,-0.05,0.0)
    glVertex3f(-0.05,-0.05,0.0)
    glEnd()

    # glBegin(GL_LINE_LOOP)
    # glColor3f(0.0, 0.0, 0.0)
    # glVertex3f(-0.05,0.05,0.0)
    # glVertex3f(0.05,0.05,0.0)
    # glVertex3f(0.05,-0.05,0.0)
    # glVertex3f(-0.05,-0.05,0.0)
    # glEnd()

    glPopMatrix()