from OpenGL.GL import *
from glew_wish import *
from Modelo import *

import glfw
import math

class Obstaculos(Modelo):

        def __init__(self):

            super().__init__(posicion_z = 0.0)

            #Colisiones
            self.extremo_derecho = 0.05
            self.extremo_izquierdo = -0.05
            self.extremo_inferior = -0.05
            self.extremo_superior = 0.15

            #Posiciones
            self.posicion_x = -0.9
            self.posicion_y = -0.55
            self.posicion_y_1 = 0.0
            self.posicion_anterior = 0.0

            #Meta
            self.posicion_meta_x = 0.95 
            self.posicion_meta_y = -0.55

            self.velocidad_x = 0.6
            self.velocidad_y = 0.7

            self.tamaño_1 = 0.05
            self.tamaño_2 = 9.0
            self.tamaño_3 = -0.90

            self.obstaculo_y = -0.55
            self.obstaculo_y_1 = 0.09

            self.obstaculo_x = -0.6
            self.obstaculo_x_1 = -0.5
            self.obstaculo_x_2 = -0.1
            self.obstaculo_x_3 = -0.0
            self.obstaculo_x_4 = 0.5

            #posicion rectangulo 2
            self.obstaculo_r2_x = 0.4
            self.obstaculo_r2_y = -0.55

            #Posiciones plataforma
            self.posicion_plataforma_x = 0.0
            self.posicion_plataforma_y = -0.9

            self.lista_obstaculos = [self.tamaño_1, self.tamaño_2, self.obstaculo_y, self.obstaculo_y_1, self.obstaculo_x, self.obstaculo_x_1,
            self.obstaculo_x_2, self.obstaculo_x_3, self.obstaculo_x_4]


        def dibujar(self):
            #META
            glPushMatrix()
            glTranslatef(self.posicion_meta_x, self.posicion_meta_y, self.posicion_z)
            glBegin(GL_QUADS)

            glColor3f(40/255, 50/255, 100/255)
            glVertex3f(-self.tamaño_1, self.tamaño_2, self.posicion_z)
            glVertex3f(self.tamaño_1, self.tamaño_2, self.posicion_z)
            glVertex3f(0.05,-0.05,0.0)
            glVertex3f(-0.05,-0.05,0.0)
            glEnd()

            glPopMatrix()

            #Triangulo1
            glPushMatrix()
            glTranslatef(self.obstaculo_x, self.obstaculo_y, self.posicion_z)
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
            
            glPushMatrix()
            glTranslatef(self.obstaculo_x_2, self.obstaculo_y, self.posicion_z)
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
            glTranslatef(self.obstaculo_x_3, self.obstaculo_y, self.posicion_z)
            glBegin(GL_QUADS)
            glColor3f(0.621,0.61,0.48)

            glVertex3f(-0.05,0.15,0.0)
            glVertex3f(0.05,0.15,0.0)
            glVertex3f(0.05,-0.05,0.0)
            glVertex3f(-0.05,-0.05,0.0)
            glEnd()
            glPopMatrix()
            #
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
            #
            
            glPushMatrix()
            glTranslatef(self.obstaculo_x, self.obstaculo_x_3, self.posicion_z)
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
            glTranslatef(self.obstaculo_x, self.obstaculo_y_1, self.posicion_z)
            glBegin(GL_POLYGON)

            #A sin(2 pi f t + f)
            glColor3f(0.457,0.019,0.957)
            for angulo in range(0,359,5):
                glVertex3f(0.03*math.cos(angulo * math.pi / 180), 0.03*math.sin(angulo * math.pi / 180), 0)
            glEnd()
            glPopMatrix()

            #Triangulo3
            glPushMatrix()
            glTranslatef(self.obstaculo_x_4, self.obstaculo_y, self.posicion_z)
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
            glTranslatef(+self.obstaculo_x, self.obstaculo_y, self.posicion_z)
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
            glTranslatef(+self.obstaculo_r2_x, self.obstaculo_r2_y, self.posicion_z)
            glBegin(GL_QUADS)
            glColor3f(0.368,0.0,0.007)

            glVertex3f(-0.05,0.15,0.0)
            glVertex3f(0.05,0.15,0.0)
            glVertex3f(0.05,-0.05,0.0)
            glVertex3f(-0.05,-0.05,0.0)
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