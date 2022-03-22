from OpenGL.GL import *
from glew_wish import *
from Modelo import *

import glfw
import math

class Obstaculos(Modelo):

        def __init__(self):

            super().__init__(posicion_z = 0.0)

            self.obstaculo_x = -0.6
            self.obstaculo_x_1 = -0.5
            self.obstaculo_x_2 = -0.1
            self.obstaculo_x_3 = -0.0
            self.obstaculo_x_4 = 0.5

            self.obstaculo_y_1 = 0.09

            #posicion rectangulo 2
            self.obstaculo_r2_x = 0.4
            self.obstaculo_r2_y = -0.55

            #Posiciones plataforma
            self.posicion_plataforma_x = 0.0
            self.posicion_plataforma_y = -0.9

        def dibujar(self):

            #Cuadrito del rombo
            glPushMatrix()
            glTranslatef(self.obstaculo_x, self.obstaculo_y_1, self.posicion_z)
            glBegin(GL_QUADS)
            glColor3f(0.167,0.003,0.359)

            glVertex3f(-0.05,0.05,0.0)
            glVertex3f(0.05,0.05,0.0)
            glVertex3f(0.05,-0.05,0.0)
            glVertex3f(-0.05,-0.05,0.0)
            glEnd()
            glPopMatrix()
            
            glPushMatrix()
            glTranslatef(self.obstaculo_x, self.obstaculo_x_3, self.posicion_z)
            glRotatef(180.0,1,0,0)
            glBegin(GL_TRIANGLES)

            #Establecer color
            glColor3f(0.257,0.972,1)

            #Manda vertices a dibujar
            glVertex3f(-0.05,-0.05,0)
            glVertex3f(0,0.05,0)
            glVertex3f(0.05,-0.05,0)

            glEnd()
            glPopMatrix()
            #
            #circunferecia 
            glPushMatrix()
            glTranslatef(self.obstaculo_x, self.obstaculo_y_1, self.posicion_z)
            glBegin(GL_POLYGON)

            #A sin(2 pi f t + f)
            glColor3f(0.457,0.019,0.957)
            for angulo in range(0,359,5):
                glVertex3f(0.03*math.cos(angulo * math.pi / 180), 0.03*math.sin(angulo * math.pi / 180), 0)
            glEnd()
            glPopMatrix()

            #PLATAFORMA
            glPushMatrix()
            glTranslatef(self.posicion_plataforma_x, self.posicion_plataforma_y, self.posicion_z)
            glBegin(GL_QUADS)
            glColor3f(0.0, 0.0, 0.0)
            glVertex3f(-1.0,0.30,0.0)
            glVertex3f(1.,0.30,0.0)
            glVertex3f(1.0,-0.30,0.0)
            glVertex3f(-1.0,-0.30,0.0)
            glEnd()

            glPopMatrix()