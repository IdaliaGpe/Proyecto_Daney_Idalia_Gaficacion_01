from OpenGL.GL import *
from glew_wish import *
from Modelo import *

import glfw

class Jugador(Modelo):

    def __init__(self):

        super().__init__()

        self.posicion_x = -0.9
        self.posicion_y = -0.55
        self.posicion_y = 0.0
        self.posicion_anterior = 0.0

        self.velocidad_x = 0.6
        self.velocidad_y = 0.7

        self.extremo_izquierdo = 0.05
        self.extremo_derecho = 0.05
        self.extremo_inferior = 0.05
        self.extremo_superior = 0.05

    def dibujar(self):
    
        glPushMatrix()
        glTranslatef(self.posicion_x, self.posicion_y, self.posicion_z)
        glBegin(GL_QUADS)

        glColor3f(0.4, 0.9, 0.21)

        glVertex3f(-0.05,0.05,0.0)
        glVertex3f(0.05,0.05,0.0)
        glVertex3f(0.05,-0.05,0.0)
        glVertex3f(-0.05,-0.05,0.0)

        glEnd()
        glPopMatrix()

    def actualizar(self, window, tiempo_delta):

        velocidad_cuadrado = 0.20

        cantidad_movimiento = velocidad_cuadrado * tiempo_delta

        #Cuadrado se mueve solo
        avanzar = True

        if avanzar == True:
            self.posicion_x = self.posicion_x + cantidad_movimiento
    
        #Salto
        #Velocidad de salto
        poder_salto = 1.9
        vel_y = self.velocidad_y * tiempo_delta * poder_salto
        gravedad = -0.9
        #Que tan alto salta
        cantidad_de_salto = 0.5

        estado_tecla_space = glfw.get_key(window, glfw.KEY_SPACE)

        JUMP = False
        IS_JUMPING = False
        IS_FALLING = False

        if JUMP is False and IS_JUMPING is False and estado_tecla_space == glfw.PRESS:
            JUMP = True
            posicion_y_cuadrado_anterior = self.velocidad_y

        if JUMP is True:
            # Añade a la y la velocidad_y a la velocidad anteiror
            # Añade la velocidad del salto
            self.velocidad_y += vel_y
            IS_JUMPING = True

        #Ver si ya se paso de burger
        if IS_JUMPING:
            if self.velocidad_y - posicion_y_cuadrado_anterior >= cantidad_de_salto:
                
                JUMP = False
                vel_y = gravedad * tiempo_delta
                self.velocidad_y += vel_y
                IS_FALLING = True

        if IS_FALLING: 
            vel_y = gravedad * tiempo_delta
            self.velocidad_y += vel_y

            if self.velocidad_y <= posicion_y_cuadrado_anterior:
                IS_JUMPING = False
                JUMP = False
                IS_FALLING = False
                self.velocidad_y = posicion_y_cuadrado_anterior

        # actualizar_cuadrado(tiempo_delta)
        # tiempo_anterior = tiempo_actual