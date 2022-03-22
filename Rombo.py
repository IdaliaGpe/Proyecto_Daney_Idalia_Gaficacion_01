from OpenGL.GL import *
from glew_wish import *
from Modelo import *

class Rombo(Modelo):

    rotacion = 0
    velocidad_angular = 135.0
    rotacion1 = 0
    
    def __init__(self):
        super().__init__(-0.6, 0.05, 0.0, 0.0, 1, 135, 0.0, 0.0)
        #Posiciones
        self.posicion_anterior = 0.0

    def dibujar(self):
        ##Rombo
        glPushMatrix()

        glTranslatef(self.posicion_x, self.posicion_y, 0.0)
        glRotatef(self.rotacion,0.0,0.0,1.0)
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
        glTranslatef(self.posicion_x, self.posicion_y, self.posicion_z)
        glRotatef(self.rotacion1, 0.0,0.0, 1.0)
        glScalef(1.9,1.9,0)

        glBegin(GL_QUADS)
        glColor3f(0.368,0.380,1.0)

        glVertex3f(-0.05,0.05,0.0)
        glVertex3f(0.05,0.05,0.0)
        glVertex3f(0.05,-0.05,0.0)
        glVertex3f(-0.05,-0.05,0.0)
        glEnd()
        glPopMatrix()

    def actualizar(self, tiempo_delta):

        cantidad_rotacion = self.velocidad_angular * tiempo_delta
        self.rotacion = self.rotacion + cantidad_rotacion
        
        if self.rotacion > 360.0:
            self.rotacion = self.rotacion - 360.0

        cantidad_rotacion1 = -self.velocidad_angular * tiempo_delta
        self.rotacion1 = self.rotacion1 + cantidad_rotacion1

        if self.rotacion  > 360.0:
               self.rotacion1 = self.rotacion1 - 360.0