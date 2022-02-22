#Importar librerias
from pickle import GLOBAL
from sre_constants import JUMP
from turtle import pos
from OpenGL.GL import *
from glew_wish import *
from cmath import cos, pi, sin

import glfw
import colision as col
import draw_cuadrado as cua
import fondo as drawfond
import fondo_animado as fond
import math

#Variables
velocidad_x = 0.6

velocidad_y = 0.7
JUMP = False
IS_JUMPING = False
IS_FALLING = False

#Formato = x, y, z, width, height
posicion_cuadrado = [-0.9, -0.55, 0.0, 0.05, 0.05]
posicion_y_cuadrado_anterior = 0.0
window = None
posicion_respawn = [-0.9, -0.55, 0.0, 0.05, 0.05]

rotacion_rombo = 0.0
rotacion_rombo1 = 0.0
velocidad_angular = 135.0
velocidad_angular1 = -135.0
tiempo_anterior = 0.0

#Cerrar con ESC
def key_callback(window, key, scancode, action, mods):
    #Que la tecla escape cierre ventana al ser presionado
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
         glfw.set_window_should_close(window, 1)

#Cuadrado
posicion_cuadrado45 = [0.0, 0.0, 0.0]
posicion_cuadrado44 = [0.0, 0.6, 0.0]
#0 - izquierda,  1 - derecha
direccion_cuadrado = 1
velocidad_cuadrado = 0.20

angulo_triangulo = 0.0
fase = 90.0

def actualizar_cuadrado(tiempo_delta):
    global direccion_cuadrado
    global velocidad_cuadrado
    global posicion_cuadrado45, posicion_cuadrado44
    cantidad_movimiento = velocidad_cuadrado * tiempo_delta
    if direccion_cuadrado == 0:
        posicion_cuadrado45[0] = posicion_cuadrado45[0] - cantidad_movimiento
        posicion_cuadrado45[0] = posicion_cuadrado45[0] + (
            math.cos((angulo_triangulo + fase) * pi / 180.0) * cantidad_movimiento
        )
        posicion_cuadrado45[1] = posicion_cuadrado45[1] + (
            math.sin((angulo_triangulo + fase) * pi / 180.0) * cantidad_movimiento
        )
        posicion_cuadrado45[0] = posicion_cuadrado45[0] + (
            math.cos((angulo_triangulo + fase) * pi / 180.0) * cantidad_movimiento
        )
        posicion_cuadrado45[1] = posicion_cuadrado45[1] + (
            math.sin((angulo_triangulo + fase) * pi / 180.0) * cantidad_movimiento
        )

    elif direccion_cuadrado == 1:
        posicion_cuadrado45[0] = posicion_cuadrado45[0] + cantidad_movimiento
       
    if posicion_cuadrado45[0] <= -0.8 and direccion_cuadrado == 0:
        direccion_cuadrado = 1
      
    if posicion_cuadrado45[0] >= 1 and direccion_cuadrado == 1:
        direccion_cuadrado = 0
        
        #posicion_cuadrado[0] = -1
        #posicion_cuadrado[1] = posicion_cuadrado[1] - 0.1

    if direccion_cuadrado == 0:
        posicion_cuadrado44[0] = posicion_cuadrado44[0] - cantidad_movimiento

    elif direccion_cuadrado == 1:
        posicion_cuadrado44[0] = posicion_cuadrado44[0] + cantidad_movimiento
       
    if posicion_cuadrado44[0] <= -0.8 and direccion_cuadrado == 0:
        direccion_cuadrado = 1
      
    if posicion_cuadrado44[0] >= 1 and direccion_cuadrado == 1:
        direccion_cuadrado = 0
        
        #posicion_cuadrado[0] = -1
        #posicion_cuadrado[1] = posicion_cuadrado[1] - 0.1
    

#Actualizar Movimientos
def actualizar():
    global velocidad_x, velocidad_y
    global tiempo_anterior
    global window, JUMP, IS_JUMPING, IS_FALLING 
    global posicion_cuadrado
    global posicion_y_cuadrado_anterior 
    global velocidad_angular, rotacion_rombo, rotacion_rombo1


    tiempo_actual = glfw.get_time()
    #Cuanto tiempo paso entre la ejecucion actual
    #y la inmediata anterior de esta funcion
    tiempo_delta = tiempo_actual - tiempo_anterior

    cantidad_movimiento = velocidad_x * tiempo_delta

    cantidad_rotacion = velocidad_angular * tiempo_delta
    cantidad_rotacion1 = velocidad_angular1 * tiempo_delta
    rotacion_rombo = rotacion_rombo + cantidad_rotacion

    rotacion_rombo1 = rotacion_rombo1 + cantidad_rotacion1

    if rotacion_rombo  > 360.0:
        rotacion_rombo = rotacion_rombo - 360.0
    
    if rotacion_rombo1  > 360.0:
        rotacion_rombo1 = rotacion_rombo - 360.0

    #Cuadrado se mueve solo
    avanzar = True

    if avanzar == True:
        posicion_cuadrado[0] = posicion_cuadrado[0] + cantidad_movimiento
 
    #Salto
    #Velocidad de salto
    poder_salto = 1.9
    vel_y = velocidad_y * tiempo_delta * poder_salto
    gravedad = -0.9
    #Que tan alto salta
    cantidad_de_salto = 0.5

    estado_tecla_space = glfw.get_key(window, glfw.KEY_SPACE)
    if JUMP is False and IS_JUMPING is False and estado_tecla_space == glfw.PRESS:
        JUMP = True
        posicion_y_cuadrado_anterior = posicion_cuadrado[1]

    if JUMP is True:
        # Añade a la y la velocidad_y a la velocidad anteiror
        # Añade la velocidad del salto
        posicion_cuadrado[1] += vel_y
        IS_JUMPING = True

    #Ver si ya se paso de burger
    if IS_JUMPING:
        if posicion_cuadrado[1] - posicion_y_cuadrado_anterior >= cantidad_de_salto:
            
            JUMP = False
            vel_y = gravedad * tiempo_delta
            posicion_cuadrado[1] += vel_y
            IS_FALLING = True

    if IS_FALLING: 
        vel_y = gravedad * tiempo_delta
        posicion_cuadrado[1] += vel_y

        if posicion_cuadrado[1] <= posicion_y_cuadrado_anterior:
            IS_JUMPING = False
            JUMP = False
            IS_FALLING = False
            posicion_cuadrado[1] = posicion_y_cuadrado_anterior

    actualizar_cuadrado(tiempo_delta)
    tiempo_anterior = tiempo_actual

#Dibujar Escenarios y Jugador
def draw():
    global posicion_cuadrado

    fond.draw_fondo_animado(rotacion_rombo, rotacion_rombo1, posicion_cuadrado45, posicion_cuadrado44)
    
    posicion_cuadrado = drawfond.draw_fondo(posicion_cuadrado, window, get_posicion_incial())
    cua.draw_cuadrado(posicion_cuadrado)

#Main
def main():
    global window

    width = 800
    height = 800
    #Inicializar GLFW
    if not glfw.init():
        return

    #Declarar ventana
    window = glfw.create_window(width, height, "Geometry Dash Pirata", None, None)

    #Configuraciones de OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Verificamos la creacion de la ventana
    if not window:
        glfw.terminate()
        return

    #Establecer el contexto
    glfw.make_context_current(window)

    #Le dice a GLEW que si usaremos el GPU
    glewExperimental = True

    #Inicializar glew
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #imprimir version
    version = glGetString(GL_VERSION)
    print(version)

    #Cerrar con ESC
    glfw.set_key_callback(window, key_callback)
    
    #Draw loop
    while not glfw.window_should_close(window):
        #Establecer el viewport
        #glViewport(0,0,width,height)
        #Establecer color de borrado
        glClearColor(41/255, 44/255, 76/255, 1)
        #Borrar el contenido del viewport
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        actualizar()

        #Dibujar
        draw()

        #Polling de inputs
        glfw.poll_events()

        #Cambia los buffers
        glfw.swap_buffers(window)

    glfw.destroy_window(window)
    glfw.terminate()

def get_cuadrado():
    return posicion_cuadrado

def set_posicion_inicial():
    posicion_cuadrado = get_posicion_incial()
    return posicion_cuadrado

def get_posicion_incial():
    return [-0.9, -0.55, 0.0, 0.05, 0.05] 

if __name__ == "__main__":
    main()