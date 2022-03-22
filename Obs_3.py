from OpenGL.GL import *
from glew_wish import *
from Modelo import *

class Obs_3(Modelo):

        def __init__(self):

            super().__init__(0.4, -0.55, 0.0)

            #Colisiones
            self.extremo_derecho = 0.15
            self.extremo_izquierdo = 0.05
            self.extremo_inferior = 0.05
            self.extremo_superior = 0.10

            self.obstaculo_y = -0.55
            self.obstaculo_x_4 = 0.5

            self.obstaculo_r2_x = 0.4
            self.obstaculo_r2_y = -0.55

        def dibujar(self):

            #Triangulo3
            glPushMatrix()
            glTranslatef(+self.obstaculo_r2_x, self.obstaculo_r2_y, self.posicion_z)
            glBegin(GL_TRIANGLES)

            #Establecer color
            glColor3f(0.453,0.451,0.56)

            #Manda vertices a dibujar
            glVertex3f(-0.05,-0.05,0)
            glVertex3f(0,0.05,0)
            glVertex3f(0.05,-0.05,0)

            glEnd()
            glPopMatrix()

            glPushMatrix()
            glTranslatef(self.obstaculo_x_4, self.obstaculo_y, self.posicion_z)
            glBegin(GL_QUADS)
            glColor3f(0.368,0.0,0.007)

            glVertex3f(-0.05,0.15,0.0)
            glVertex3f(0.05,0.15,0.0)
            glVertex3f(0.05,-0.05,0.0)
            glVertex3f(-0.05,-0.05,0.0)
            glEnd()
            glPopMatrix()
            
            #self.dibujar_bounding_box()