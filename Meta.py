from OpenGL.GL import *
from glew_wish import *
from Modelo import *

import glfw
import math

class Meta(Modelo):

    closed = False

    def __init__(self):

        super().__init__(0.95,-0.55,0.0,1.0,0.0)

        #Colisiones
        self.extremo_derecho = 0.1
        self.extremo_izquierdo = 0.05
        self.extremo_inferior = 0.09
        self.extremo_superior = 0.9

    def dibujar(self):

        #META
        glPushMatrix()
        glTranslatef(self.posicion_x, self.posicion_y, self.posicion_z)
        glBegin(GL_QUADS)


        glColor3f(40/255, 50/255, 100/255)
        glVertex3f(-0.05, 9.0, 0.0)
        glVertex3f(0.05, 9.0, 0.0)
        glVertex3f(0.05,-0.05,0.0)
        glVertex3f(-0.05,-0.05,0.0)
        glEnd()

        glPopMatrix()

        self.dibujar_bounding_box()