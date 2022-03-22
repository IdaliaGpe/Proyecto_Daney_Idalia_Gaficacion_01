from OpenGL.GL import *
from glew_wish import *
from Modelo import *

class Obs_1(Modelo):

        def __init__(self):

            super().__init__(-0.6, -0.55, 0.0)

            #Colisiones
            self.extremo_derecho = 0.15
            self.extremo_izquierdo = 0.05
            self.extremo_inferior = 0.05
            self.extremo_superior = 0.05

            self.obstaculo_y = -0.55
            self.obstaculo_y_1 = 0.09

            self.obstaculo_x = -0.6
            self.obstaculo_x_1 = -0.5

        def dibujar(self):

            #Triangulo1
            glPushMatrix()
            glTranslatef(self.obstaculo_x, self.obstaculo_y, self.posicion_z)
            glBegin(GL_TRIANGLES)

            #Establecer color
            glColor3f(1,1,0)

            #Manda vertices a dibujar
            glVertex3f(-0.05,-0.05, 0)
            glVertex3f(0.0 ,0.05, 0)
            glVertex3f(0.05,-0.05, 0)

            glEnd()
            glPopMatrix()

            # Triangulo2
            glPushMatrix()
            glTranslatef(self.obstaculo_x_1, self.obstaculo_y, self.posicion_z)
            glBegin(GL_TRIANGLES)

            #Establecer color
            glColor3f(0.184,0.361,0.145)

            #Manda vertices a dibujar
            glVertex3f(-0.05,-0.05,0)
            glVertex3f(0,0.05,0)
            glVertex3f(0.05,-0.05,0)

            glEnd()
            glPopMatrix()

            #self.dibujar_bounding_box()