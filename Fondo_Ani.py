from OpenGL.GL import *
from glew_wish import *
from Modelo import *
from cmath import cos, pi, sin

import glfw
import math

class Fondo_Ani(Modelo):

    def __init__(self):

            super().__init__(direccion = 1.0, rotacion = 0.0, angulo = 0.0, velocidad_angular = 135.0, posicion_z = 0.0)

            #Posiciones
            self.posicion_x = 0.0
            self.posicion_y = 0.0
            self.posicion_anterior = 0.0

            #Meta
            self.posicion_meta_x = 0.95 
            self.posicion_meta_y = -0.55

            self.velocidad_x = 0.6
            self.velocidad_y = 0.20

            self.extremo_izquierdo = 0.05
            self.extremo_derecho = 0.05
            self.extremo_inferior = 0.05
            self.extremo_superior = 0.05

            self.posicion_lineas_x_1 = -0.2
            self.posicion_lineas_y_1 = 0.0
            self.posicion_lineas_x_2 = -0.6
            self.posicion_lineas_y_2 = 0.0
            self.posicion_lineas_x_3 = -0.90
            self.posicion_lineas_y_3 = 0.3
            self.posicion_lineas_x_4 = -0.9
            self.posicion_lineas_y_4 = 0.3
            self.posicion_lineas_x_5 = -0.5
            self.posicion_lineas_y_5 = 0.0
            self.posicion_lineas_x_6 = -0.5
            self.posicion_lineas_y_6 = 0.5
            self.posicion_lineas_x_7 = -0.1
            self.posicion_lineas_y_7 = -0.2
            self.posicion_lineas_x_8 = -0.1
            self.posicion_lineas_y_8 = 0.2
            self.posicion_lineas_x_9 = 0.2
            self.posicion_lineas_y_9 = 0.14
            self.posicion_lineas_x_10 = 0.29
            self.posicion_lineas_y_10 = 0.5
            self.posicion_lineas_x_11 = 0.6
            self.posicion_lineas_y_11 = 0.0
            self.posicion_lineas_x_12 = 0.7
            self.posicion_lineas_y_12 = 0.0
            self.posicion_lineas_x_13 = 0.7
            self.posicion_lineas_y_13 = -0.4
            self.posicion_lineas_x_14 = 0.4
            self.posicion_lineas_y_14 = 0.8

            self.posicion_cuadritos_x_1 = 0.0
            self.posicion_cuadritos_y_1 = 0.0
            self.posicion_cuadritos_x_2 = 0.3
            self.posicion_cuadritos_y_2 = -0.2


            self.posicion_1 = 0.14
            self.posicion_2 = 0.29
            self.posicion_3 = -0.90
            self.posicion_4 = 0.7
            self.posicion_5 = 0.4
            self.posicion_6 = 0.8
            self.posicion_7 = 0.2
            self.posicion_8 = 0.648
            self.posicion_9 = 0.39
            self.posicion_10 = 0.488
            self.posicion_11 = 0.05
            self.posicion_12 = 0.81
            self.posicion_13 = 0.835
            self.posicion_14 = 0.849
            self.posicion_15 = 0.785
            self.posicion_16 = 0.0
            self.posicion_17 = 0.6


            self.obstaculo_y = 0.3
            self.obstaculo_y_1 = 0.09

            self.obstaculo_x = -0.6
            self.obstaculo_x_1 = -0.90
            self.obstaculo_x_2 = 0.2
            self.obstaculo_x_3 = 0.5
            self.obstaculo_x_4 = -0.1

            self.fase = 90.0

    ##
    ##
    ##
    ##

    def dibujar(self):

        glPushMatrix()
        glTranslatef(self.posicion_lineas_x_2, self.posicion_lineas_y_2, self.posicion_z)
        glBegin(GL_QUADS)
        glColor3f(0.628,0.121,1.0)

        glVertex3f(-0.01,1.0,0.0)
        glVertex3f(0.01,1.0,0.0)
        glVertex3f(0.01,-0.55,0.0)
        glVertex3f(-0.01,-0.55,0.0)
        glEnd()
        glPopMatrix()

        ##Ho
        glPushMatrix()
        glTranslatef(self.posicion_lineas_x_3 , self.posicion_lineas_y_3, self.posicion_z)
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
        glTranslatef(self.posicion_lineas_x_4, -self.posicion_lineas_y_4, self.posicion_z)
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
        glTranslatef(self.posicion_lineas_x_1, self.posicion_lineas_y_1, self.posicion_z)
        glBegin(GL_QUADS)
        glColor3f(0.628,0.121,1.0)

        glVertex3f(-0.01,1.0,0.0)
        glVertex3f(0.01,1.0,0.0)
        glVertex3f(0.01,-1.0,0.0)
        glVertex3f(-0.01,-1.0,0.0)
        glEnd()
        glPopMatrix()

        ##Ho
        glPushMatrix()
        glTranslatef(self.posicion_lineas_x_5, self.posicion_lineas_y_5, self.posicion_z)
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
        glTranslatef(self.posicion_lineas_x_6, +self.posicion_lineas_y_6, self.posicion_z)
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
        glTranslatef(self.posicion_lineas_x_7, self.posicion_lineas_y_7, self.posicion_z)
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
        glTranslatef(self.posicion_lineas_x_8, self.posicion_lineas_y_8, self.posicion_z)
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
        glTranslatef(self.posicion_lineas_x_9, self.posicion_lineas_y_9, self.posicion_z)
        glBegin(GL_QUADS)
        glColor3f(0.628,0.121,1.0)

        glVertex3f(-0.01,0.35,0.0)
        glVertex3f(0.01,0.35,0.0)
        glVertex3f(0.01,-0.35,0.0)
        glVertex3f(-0.01,-0.35,0.0)
        glEnd()
        glPopMatrix()

        #Ho
        glPushMatrix()
        glTranslatef(self.posicion_lineas_x_10, self.posicion_lineas_y_10, self.posicion_z)
        glBegin(GL_QUADS)
        glColor3f(0.628,0.121,1.0)

        glVertex3f(-0.1,0.01,0.0)
        glVertex3f(0.3,0.01,0.0)
        glVertex3f(0.3,-0.01,0.0)
        glVertex3f(-0.1,-0.01,0.0)
        glEnd()
        glPopMatrix()

        ##ver
        glPushMatrix()
        glTranslatef(self.posicion_lineas_x_11, self.posicion_lineas_y_11, self.posicion_z)
        glBegin(GL_QUADS)
        glColor3f(0.628,0.121,1.0)

        glVertex3f(-0.01,1.0,0.0)
        glVertex3f(0.01,1.0,0.0)
        glVertex3f(0.01,-0.65,0.0)
        glVertex3f(-0.01,-0.65,0.0)
        glEnd()
        glPopMatrix()

        #Ver
        glPushMatrix()
        glTranslatef(self.posicion_lineas_x_12, self.posicion_lineas_y_12, self.posicion_z)
        glBegin(GL_QUADS)
        glColor3f(0.628,0.121,1.0)

        glVertex3f(-0.1,0.01,0.0)
        glVertex3f(0.3,0.01,0.0)
        glVertex3f(0.3,-0.01,0.0)
        glVertex3f(-0.1,-0.01,0.0)
        glEnd()
        glPopMatrix()

        #Ho
        glPushMatrix()
        glTranslatef(self.posicion_lineas_x_13, self.posicion_lineas_y_13, self.posicion_z)
        glBegin(GL_QUADS)
        glColor3f(0.628,0.121,1.0)

        glVertex3f(-0.1,0.01,0.0)
        glVertex3f(0.3,0.01,0.0)
        glVertex3f(0.3,-0.01,0.0)
        glVertex3f(-0.1,-0.01,0.0)
        glEnd()
        glPopMatrix()

        #Ho
        glPushMatrix()
        glTranslatef(self.posicion_lineas_x_14, self.posicion_lineas_y_14, self.posicion_z)
        glBegin(GL_QUADS)
        glColor3f(0.628,0.121,1.0)

        glVertex3f(-0.6,0.01,0.0)
        glVertex3f(0.6,0.01,0.0)
        glVertex3f(0.6,-0.01,0.0)
        glVertex3f(-0.6,-0.01,0.0)
        glEnd()
        glPopMatrix()
        #############
        #############FIN DE LINEAS

        #cudrados
        glPushMatrix()
        glTranslatef(self.posicion_16, self.posicion_17, self.posicion_z)
        glRotatef(180,1,1,0)
        glScalef(2,3,0)
        glBegin(GL_QUADS)
        glColor3f(0.167,0.003,0.359)

        glVertex3f(-0.08,0.05,0.0)
        glVertex3f(0.08,0.05,0.0)
        glVertex3f(0.08,-0.05,0.0)
        glVertex3f(-0.08,-0.05,0.0)
        glEnd()
        glPopMatrix()
        ##
        #cuadro grande morado
        glPushMatrix()
        glTranslatef(self.posicion_7, self.posicion_8, self.posicion_z)
        glRotatef(180,1,1,0)
        glScalef(1.4,7.0,0)
        glBegin(GL_QUADS)
        glColor3f(0.167,0.003,0.359)

        glVertex3f(-0.08,0.05,0.0)
        glVertex3f(0.08,0.05,0.0)
        glVertex3f(0.08,-0.05,0.0)
        glVertex3f(-0.08,-0.05,0.0)
        glEnd()
        glPopMatrix()

        #Triangulos azules
        #No hubicado
        glPushMatrix()
        glTranslatef(self.obstaculo_x_4, self.posicion_9, self.posicion_z)
        glRotatef(180.0,1,0,0)
        glBegin(GL_TRIANGLES)
        glColor3f(0.5,0.72,0.141)

        glVertex3f(-0.05,-0.05,0)
        glVertex3f(0,0.05,0)
        glVertex3f(0.05,-0.05,0)
        glEnd()
        glPopMatrix()
        ##
        glPushMatrix()
        glTranslatef(self.posicion_y, self.posicion_9, self.posicion_z)
        glRotatef(180.0,1,0,0)
        glBegin(GL_TRIANGLES)
        glColor3f(0.257,0.97,1)

        glVertex3f(-0.05,-0.05,0)
        glVertex3f(0,0.05,0)
        glVertex3f(0.05,-0.05,0)
        glEnd()
        glPopMatrix()
        ##
        glPushMatrix()
        glTranslatef(+self.obstaculo_x_4, self.posicion_9, self.posicion_z)
        glRotatef(180.0,1,0,0)
        glBegin(GL_TRIANGLES)
        glColor3f(0.127,0.072,0.506)

        glVertex3f(-0.05,-0.05,0)
        glVertex3f(0,0.05,0)
        glVertex3f(0.05,-0.05,0)
        glEnd()
        glPopMatrix()
        ##
        glPushMatrix()
        glTranslatef(+self.obstaculo_x_2, self.posicion_10, self.posicion_z)
        glRotatef(180.0,1,0,0)
        glBegin(GL_TRIANGLES)
        glColor3f(0.57,0.4,0.465)

        glVertex3f(-0.05,-0.05,0)
        glVertex3f(0,0.05,0)
        glVertex3f(0.05,-0.05,0)
        glEnd()
        glPopMatrix()
        ##
        glPushMatrix()
        glTranslatef(self.obstaculo_y, self.posicion_10, self.posicion_z)
        glRotatef(180.0,1,0,0)
        glBegin(GL_TRIANGLES)
        glColor3f(0.21,0.42,0.691)

        glVertex3f(-0.05,-0.05,0)
        glVertex3f(0,0.05,0)
        glVertex3f(0.05,-0.05,0)
        glEnd()
        glPopMatrix()
        ##
        glPushMatrix()
        glTranslatef(self.posicion_5, self.posicion_10, self.posicion_z)
        glRotatef(180.0,1,0,0)
        glBegin(GL_TRIANGLES)
        glColor3f(0.27,0.9,0.451)

        glVertex3f(-0.05,-0.05,0)
        glVertex3f(0,0.05,0)
        glVertex3f(0.05,-0.05,0)
        glEnd()
        glPopMatrix()
        ##
        glPushMatrix()
        glTranslatef(+self.obstaculo_x_3, self.posicion_10, self.posicion_z)
        glRotatef(180.0,1,0,0)
        glBegin(GL_TRIANGLES)
        glColor3f(0.2,0.972,0.851)

        glVertex3f(-0.05,-0.05,0)
        glVertex3f(0,0.05,0)
        glVertex3f(0.05,-0.05,0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(self.posicion_cuadritos_x_1, self.posicion_cuadritos_y_1, self.posicion_z)
        glScalef(0.5,0.5,0)
        glBegin(GL_QUADS)
        glColor3f(0.464, 0.393, 0.211)
        glVertex3f(-0.05,0.05,0.0)
        glVertex3f(0.05,0.05,0.0)
        glVertex3f(0.05,-0.05,0.0)
        glVertex3f(-0.05,-0.05,0.0)
        glEnd()

        glPopMatrix()

        glPushMatrix()
        glTranslatef(self.posicion_cuadritos_x_2, +self.posicion_cuadritos_y_2, self.posicion_z)
        glScalef(0.5,0.5,0)
        glBegin(GL_QUADS)
        glColor3f(0.464, 0.393, 0.211)
        glVertex3f(-0.05,0.05,0.0)
        glVertex3f(0.05,0.05,0.0)
        glVertex3f(0.05,-0.05,0.0)
        glVertex3f(-0.05,-0.05,0.0)
        glEnd()

        glPopMatrix()

        ##
        ##
        ##
        ##Rombo
        glPushMatrix()
        glTranslatef(self.obstaculo_x, self.posicion_11, self.posicion_z)
        glRotatef(self.rotacion, 0, 0.0, 1.0)
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
        glTranslatef(self.obstaculo_x, self.posicion_11, self.posicion_z)
        glRotatef(self.rotacion, 0.0,0.0, 1.0)
        glScalef(1.9,1.9,0)
        glBegin(GL_QUADS)
        glColor3f(0.368,0.380,1.0)

        glVertex3f(-0.05,0.05,0.0)
        glVertex3f(0.05,0.05,0.0)
        glVertex3f(0.05,-0.05,0.0)
        glVertex3f(-0.05,-0.05,0.0)
        glEnd()
        glPopMatrix()
        ##
        ##
        ##
        ##
        ##TRIANGULOS ADORNOS
        #Triangulos2
        glPushMatrix()
        glTranslatef(self.obstaculo_x_4, self.posicion_12, self.posicion_z)
        glBegin(GL_TRIANGLES)
        glColor3f(0.0,1.0,0.733)

        glVertex3f(-0.05,-0.05,0)
        glVertex3f(0,0.05,0)
        glVertex3f(0.05,-0.05,0)
        glEnd()
        glPopMatrix()
        ##
        glPushMatrix()
        glTranslatef(self.posicion_y, self.posicion_13, self.posicion_z)
        glScalef(1,1.5,0)
        glBegin(GL_TRIANGLES)
        glColor3f(0.749,1.0,0.933)

        glVertex3f(-0.05,-0.05,0)
        glVertex3f(0,0.05,0)
        glVertex3f(0.05,-0.05,0)
        glEnd()
        glPopMatrix()
        ##
        glPushMatrix()
        glTranslatef(+self.obstaculo_x_4, self.posicion_14, self.posicion_z)
        glScalef(1,1.8,0)
        glBegin(GL_TRIANGLES)
        glColor3f(0.929,1.0,0.980)

        glVertex3f(-0.05,-0.05,0)
        glVertex3f(0,0.05,0)
        glVertex3f(0.05,-0.05,0)
        glEnd()
        glPopMatrix()
        ##
        glPushMatrix()
        glTranslatef(+self.obstaculo_x_2, self.posicion_15, self.posicion_z)
        glScalef(1,0.5,0)
        glBegin(GL_TRIANGLES)
        glColor3f(0.2,0,0.8)

        glVertex3f(-0.05,-0.05,0)
        glVertex3f(0,0.05,0)
        glVertex3f(0.05,-0.05,0)
        glEnd()
        glPopMatrix()
        ##
        glPushMatrix()
        glTranslatef(self.obstaculo_y, self.posicion_15, self.posicion_z)
        glScalef(1,0.5,0)
        glBegin(GL_TRIANGLES)
        glColor3f(0.0,0,0.95)

        glVertex3f(-0.05,-0.05,0)
        glVertex3f(0,0.05,0)
        glVertex3f(0.05,-0.05,0)
        glEnd()
        glPopMatrix()

    def actualizar(self, tiempo_delta):

        cantidad_movimiento = self.velocidad_y * tiempo_delta

        if self.direccion == 0:
            self.obstaculo_x_3 = self.obstaculo_x_3 - cantidad_movimiento
            self.obstaculo_x_3 = self.obstaculo_x_3 + (
                math.cos((self.angulo + self.fase) * pi / 180.0) * cantidad_movimiento
            )
            self.obstaculo_x_3 = self.obstaculo_x_3 + (
                math.sin((self.angulo + self.fase) * pi / 180.0) * cantidad_movimiento
            )
            self.obstaculo_x_3 = self.obstaculo_x_3 + (
                math.cos((self.angulo + self.fase) * pi / 180.0) * cantidad_movimiento
            )
            self.obstaculo_x_3 = self.obstaculo_x_3 + (
                math.sin((self.angulo + self.fase) * pi / 180.0) * cantidad_movimiento
            )

        elif self.direccion == 1:
            self.obstaculo_x_3 = self.obstaculo_x_3 + cantidad_movimiento
        
        if self.obstaculo_x_3 <= -0.8 and self.direccion == 0:
            self.direccion = 1
        
        if self.obstaculo_x_3 >= 1 and self.direccion == 1:
            self.direccion = 0
            
            #posicion_cuadrado[0] = -1
            #posicion_cuadrado[1] = posicion_cuadrado[1] - 0.1

        if self.direccion == 0:
            self.obstaculo_x_3 = self.obstaculo_x_3 - cantidad_movimiento

        elif self.direccion == 1:
            self.obstaculo_x_3 = self.obstaculo_x_3 + cantidad_movimiento
        
        if self.obstaculo_x_3 <= -0.8 and self.direccion == 0:
            self.direccion = 1
        
        if self.obstaculo_x_3 >= 1 and self.direccion == 1:
            self.direccion = 0
            
            #posicion_cuadrado[0] = -1
            #posicion_cuadrado[1] = posicion_cuadrado[1] - 0.1

        tiempo_actual = glfw.get_time()
        #Cuanto tiempo paso entre la ejecucion actual
        #y la inmediata anterior de esta funcion
        tiempo_delta = tiempo_actual - tiempo_anterior

        cantidad_movimiento = self.velocidad_x * tiempo_delta

        cantidad_rotacion = self.velocidad_angular * tiempo_delta
        cantidad_rotacion = -self.velocidad_angular * tiempo_delta
        self.rotacion = self.rotacion + self.rotacion

        self.rotacion = self.rotacion + cantidad_rotacion

        if self.rotacion  > 360.0:
            self.rotacion = self.rotacion - 360.0
        
        if self.rotacion  > 360.0:
            self.rotacion = self.rotacion - 360.0

        tiempo_anterior = tiempo_actual