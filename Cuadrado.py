from pickle import GLOBAL
from sre_constants import JUMP
from turtle import pos
from OpenGL.GL import *
from glew_wish import *
from cmath import cos, pi, sin
from Modelo import *
import math

class Cuadrado(Modelo):

    def __init__(self):

        super().__init__()

        self.posicion_cuadritos_x_1 = 0.0
        self.posicion_cuadritos_y_1 = 0.0
        self.posicion_cuadritos_x_2 = 0.3
        self.posicion_cuadritos_y_2 = -0.2
        self.direccion_cuadrado = 1
        self.posicion_anterior = 0.0

    fase = 90.0
    velocidad_cuadrado = 0.20
    angulo_triangulo = 0.0

    def dibujar(self):

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

    def actualizar(self, tiempo_delta):

        tiempo_actual = glfw.get_time()

        cantidad_movimiento = self.velocidad_cuadrado * tiempo_delta
        if self.direccion_cuadrado == 0:
            self.posicion_cuadritos_x_1 = self.posicion_cuadritos_x_1 - cantidad_movimiento
            self.posicion_cuadritos_x_1 = self.posicion_cuadritos_x_1 + (
                math.cos((self.angulo_triangulo + self.fase) * pi / 180.0) * cantidad_movimiento
            )
            self.posicion_cuadritos_y_1 = self.posicion_cuadritos_y_1 + (
                math.sin((self.angulo_triangulo + self.fase) * pi / 180.0) * cantidad_movimiento
            )
            self.posicion_cuadritos_x_1 = self.posicion_cuadritos_x_1 + (
                math.cos((self.angulo_triangulo + self.fase) * pi / 180.0) * cantidad_movimiento
            )
            self.posicion_cuadritos_y_1 = self.posicion_cuadritos_y_1 + (
                math.sin((self.angulo_triangulo + self.fase) * pi / 180.0) * cantidad_movimiento
            )

        elif self.direccion_cuadrado == 1:
            self.posicion_cuadritos_x_1 = self.posicion_cuadritos_x_1 + cantidad_movimiento
        
        if self.posicion_cuadritos_x_1 <= -0.8 and self.direccion_cuadrado == 0:
            self.direccion_cuadrado = 1
        
        if self.posicion_cuadritos_x_1 >= 1 and self.direccion_cuadrado == 1:
            self.direccion_cuadrado = 0
            
            #posicion_cuadrado[0] = -1
            #posicion_cuadrado[1] = posicion_cuadrado[1] - 0.1

        if self.direccion_cuadrado == 0:
            self.posicion_cuadritos_x_2 = self.posicion_cuadritos_x_2 - cantidad_movimiento

        elif self.direccion_cuadrado == 1:
            self.posicion_cuadritos_x_2 = self.posicion_cuadritos_x_2 + cantidad_movimiento
        
        if self.posicion_cuadritos_x_2 <= -0.8 and self.direccion_cuadrado == 0:
            self.direccion_cuadrado = 1
        
        if self.posicion_cuadritos_x_2 >= 1 and self.direccion_cuadrado == 1:
            self.direccion_cuadrado = 0
            
            #posicion_cuadrado[0] = -1
            #posicion_cuadrado[1] = posicion_cuadrado[1] - 0.1
                
        # actualizar_cuadrado(tiempo_delta)
        self.tiempo_anterior = tiempo_actual
