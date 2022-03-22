from OpenGL.GL import *
from glew_wish import *
from Modelo import *

class Obs_2(Modelo):

        def __init__(self):

            super().__init__(-0.1, -0.55, 0.0)

            #Colisiones
            self.extremo_derecho = 0.15
            self.extremo_izquierdo = 0.05
            self.extremo_inferior = 0.05
            self.extremo_superior = 0.10

            self.obstaculo_y = -0.55

            self.obstaculo_x = -0.1
            self.obstaculo_x_1 = -0.0

        def dibujar(self):
            glPushMatrix()
            glTranslatef(self.obstaculo_x, self.obstaculo_y, self.posicion_z)
            glBegin(GL_QUADS)
            glColor3f(0.158,0.368,0.456)

            glVertex3f(-0.05,0.05,0.0)
            glVertex3f(0.05,0.05,0.0) 
            glVertex3f(0.05,-0.05,0.0)
            glVertex3f(-0.05,-0.05,0.0)
            glEnd()
            glPopMatrix()
            glPushMatrix()
            glTranslatef(self.obstaculo_x_1, self.obstaculo_y, self.posicion_z)
            glBegin(GL_QUADS)
            glColor3f(0.621,0.61,0.48)

            glVertex3f(-0.05,0.15,0.0)
            glVertex3f(0.05,0.15,0.0)
            glVertex3f(0.05,-0.05,0.0)
            glVertex3f(-0.05,-0.05,0.0)
            glEnd()
            glPopMatrix()
            
            #self.dibujar_bounding_box()