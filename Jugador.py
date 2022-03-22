from OpenGL.GL import *
from glew_wish import *
from Modelo import *

import glfw

class Jugador(Modelo):

    JUMP = False
    IS_JUMPING = False
    IS_FALLING = False
    herida = False
    posicion_y_cuadrado_anterior = 0.0

    def __init__(self):

        super().__init__(-0.9,-0.55,0.0,1.0,0.0)

        self.posicion_anterior = 0.0

        self.velocidad_x = 0.6
        self.velocidad_y = 0.7

        self.extremo_izquierdo = 0.05
        self.extremo_derecho = 0.05
        self.extremo_inferior = 0.05
        self.extremo_superior = 0.05

    def dibujar(self):
    
        glPushMatrix()
        # if not self.herida:
        #  glTranslatef(self.posicion_x, self.posicion_y, self.posicion_z)
        # else: 
        #     glTranslatef(self.posicion_x, self.posicion_y, self.posicion_z)
        
        glTranslatef(self.posicion_x, self.posicion_y,0.0)

        glBegin(GL_QUADS)

        glColor3f(0.4, 0.9, 0.21)

        glVertex3f(-0.05,0.05,0.0)
        glVertex3f(0.05,0.05,0.0)
        glVertex3f(0.05,-0.05,0.0)
        glVertex3f(-0.05,-0.05,0.0)
        glEnd()

        glPopMatrix()
        
        self.dibujar_bounding_box()

    def actualizar(self, window, tiempo_delta):

        tiempo_actual = glfw.get_time()

        velocidad_cuadrado = 0.9

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
        #print(str(estado_tecla_space))

        if self.JUMP is False and self.IS_JUMPING is False and estado_tecla_space == glfw.PRESS:
            self.JUMP = True
            self.posicion_y_cuadrado_anterior = self.posicion_y

        if self.JUMP is True:
            # Añade a la y la velocidad_y a la velocidad anteiror
            # Añade la velocidad del salto
            self.posicion_y += vel_y
            self.IS_JUMPING = True

        #Ver si ya se paso
        if self.IS_JUMPING:
            if self.posicion_y - self.posicion_y_cuadrado_anterior >= cantidad_de_salto:
                
                self.JUMP = False
                vel_y = gravedad * tiempo_delta
                self.posicion_y += vel_y
                self.IS_FALLING = True

        if self.IS_FALLING: 
            vel_y = gravedad * tiempo_delta
            self.posicion_y += vel_y

            if self.posicion_y <= self.posicion_y_cuadrado_anterior:
                self.IS_JUMPING = False
                self.JUMP = False
                self.IS_FALLING = False
                self.posicion_y = self.posicion_y_cuadrado_anterior
                
        # actualizar_cuadrado(tiempo_delta)
        self.tiempo_anterior = tiempo_actual