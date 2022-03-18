#Importar librerias
from pickle import GLOBAL
from sre_constants import JUMP
from turtle import pos
from OpenGL.GL import *
from glew_wish import *

from Jugador import *
from Fondo_Ani import *
from Obstaculos import *

import glfw

#Formato = x, y, z, width, height
window = None
posicion_respawn = [-0.9, -0.55, 0.0, 0.05, 0.05]

tiempo_anterior = 0.0

estado_anterior_espacio = glfw.RELEASE

fondo = Fondo_Ani()
obs = Obstaculos()
obsr = []
jugador = Jugador()

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
            glfw.set_window_should_close(window, 1)

    # jugador.actualizar(window, tiempo_delta)
    # for obstaculo in obs:
    #     obstaculo.actualizar(tiempo_delta)
    #     if obstaculo.colisionando(jugador):
    #         jugador.self.posicion_x = get_posicion_incial()

    tiempo_anterior = tiempo_actual
    
def colisionando():
   
    colisionando = False
    
 
def draw():

    fondo.dibujar()
    obs.dibujar()
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

# def get_cuadrado():
#     return posicion_cuadrado

# def set_posicion_inicial():
#     posicion_cuadrado = get_posicion_incial()
#     return posicion_cuadrado

    # get_posicion_incial():
    #     return [-0.9, -0.55, 0.0, 0.05, 0.05] 

if __name__ == "__main__":
    main()