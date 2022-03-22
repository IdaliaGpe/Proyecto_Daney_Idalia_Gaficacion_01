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

import glfw

#Formato = x, y, z, width, height
window = None

tiempo_anterior = 0.0

estado_anterior_espacio = glfw.RELEASE

closed = False
close = glfw.set_window_should_close(window, 1)

meta = Meta()
fondo = Fondo_Ani()
obstaculo = Obstaculos()
obsr = []
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
    for obstaculo in obsr:
        obstaculo.actualizar(tiempo_delta)
        if obstaculo.colisionando(jugador):
            obstaculo.herida = True

    if jugador.colisionando(meta):
        glfw.set_window_should_close(window, 1)

    tiempo_anterior = tiempo_actual
    
def colisionando():
    colisionando = False
    return colisionando   
    
 
def draw():

    fondo.dibujar()
    meta.dibujar()
    obstaculo.dibujar()
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