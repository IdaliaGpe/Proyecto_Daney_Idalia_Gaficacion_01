#Importar librerias
from calendar import c
from pickle import GLOBAL
from sre_constants import JUMP
from turtle import pos
from OpenGL.GL import *
from glew_wish import *

from Meta import *
from Jugador import *
from Fondo_Ani import *
from Obstaculos import *
from Rombo import *

from Obs_1 import *
from Obs_2 import *
from Obs_3 import *

import glfw

#Formato = x, y, z, width, height
window = None

posicion_respawn = [-0.9, -0.55, 0.0, 0.05, 0.05]

tiempo_anterior = 0.0

estado_anterior_espacio = glfw.RELEASE

closed = False
close = glfw.set_window_should_close(window, 1)

rombo = Rombo()
meta = Meta()
fondo = Fondo_Ani()
obstaculo = Obstaculos()
obs_1 = Obs_1()
obs_2 = Obs_2()
obs_3 = Obs_3()
jugador = Jugador()

#Cerrar con ESC
def key_callback(window, key, scancode, action, mods):
    #Que la tecla escape cierre ventana al ser presionado
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
         glfw.set_window_should_close(window, 1)

def actualizar():
    global tiempo_anterior
    global window

    tiempo_actual = glfw.get_time()
    # Cuanto tiempo paso entre la ejecucion actual
    # y la inmediata anterior de esta funcion
    tiempo_delta = tiempo_actual - tiempo_anterior

    jugador.actualizar(window, tiempo_delta)

    if jugador.colisionando(meta):
        glfw.set_window_should_close(window, 1)

    if jugador.colisionando(obs_1):
        jugador.posicion_x = -0.9

    if jugador.colisionando(obs_2):
        jugador.posicion_x = -0.9

    if jugador.colisionando(obs_3):
        jugador.posicion_x = -0.9

    rombo.actualizar(tiempo_delta)

    tiempo_anterior = tiempo_actual
    
def colisionando():
    colisionando = False
    return colisionando   
    
 
def draw():
    fondo.dibujar()
    meta.dibujar()
    rombo.dibujar()
    obstaculo.dibujar()
    obs_1.dibujar()
    obs_2.dibujar()
    obs_3.dibujar()
    jugador.dibujar()

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

if __name__ == "__main__":
    main()