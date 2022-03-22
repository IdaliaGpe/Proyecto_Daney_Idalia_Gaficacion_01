from OpenGL.GL import *
from glew_wish import *
from Modelo import *

import glfw
import math

class Meta(Modelo):

    closed = False

    def __init__(self):

        super().__init__(posicion_z = 0.0)

        #Colisiones
        self.extremo_derecho = 0.05
        self.extremo_izquierdo = -0.05
        self.extremo_inferior = -0.05
        self.extremo_superior = 0.9

        #Meta
        self.posicion_meta_x = 0.95 
        self.posicion_meta_y = -0.55

        self.tamaño_1 = 0.05
        self.tamaño_2 = 9.0

    def dibujar(self, window):

        #META
        glPushMatrix()
        glTranslatef(self.posicion_meta_x, self.posicion_meta_y, self.posicion_z)
        glBegin(GL_QUADS)

        if not self.closed:
            glfw.set_window_should_close(window, 1)

        glColor3f(40/255, 50/255, 100/255)
        glVertex3f(-self.tamaño_1, self.tamaño_2, self.posicion_z)
        glVertex3f(self.tamaño_1, self.tamaño_2, self.posicion_z)
        glVertex3f(0.05,-0.05,0.0)
        glVertex3f(-0.05,-0.05,0.0)
        glEnd()

        glPopMatrix()