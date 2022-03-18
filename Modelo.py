from OpenGL.GL import *
from glew_wish import *
import glfw

class Modelo:

    #POSICIONES
    @property
    def obstaculo_x_4(self):
        return self._obstaculo_x_4
    @obstaculo_x_4.setter
    def obstaculo_x_4(self, obstaculo_x_4):
        self._obstaculo_x_4 = obstaculo_x_4

    @property
    def obstaculo_x_3(self):
        return self._obstaculo_x_3
    @obstaculo_x_3.setter
    def obstaculo_x_3(self, obstaculo_x_3):
        self._obstaculo_x_3 = obstaculo_x_3

    @property
    def obstaculo_x_2(self):
        return self._obstaculo_x_2
    @obstaculo_x_2.setter
    def obstaculo_x_2(self, obstaculo_x_2):
        self._obstaculo_x_2 = obstaculo_x_2

    @property
    def obstaculo_x_1(self):
        return self._obstaculo_x_1
    @obstaculo_x_1.setter
    def obstaculo_x_1(self, obstaculo_x_1):
        self._obstaculo_x_1 = obstaculo_x_1

    @property
    def obstaculo_x(self):
        return self._obstaculo_x
    @obstaculo_x.setter
    def obstaculo_x(self, obstaculo_x):
        self._obstaculo_x = obstaculo_x

    @property
    def obstaculo_y_1(self):
        return self._obstaculo_y_1
    @obstaculo_y_1.setter
    def obstaculo_y_1(self, obstaculo_y_1):
        self._obstaculo_y_1 = obstaculo_y_1

    @property
    def obstaculo_y(self):
        return self._obstaculo_y
    @obstaculo_y.setter
    def obstaculo_y(self, obstaculo_y):
        self._obstaculo_y = obstaculo_y

    @property
    def tamaño_3(self):
        return self._tamaño_3
    @tamaño_3.setter
    def tamaño_3(self, tamaño_3):
        self._tamaño_3 = tamaño_3

    @property
    def tamaño_1(self):
        return self._tamaño_1
    @tamaño_1.setter
    def tamaño_1(self, tamaño_1):
        self._tamaño_1 = tamaño_1

    @property
    def tamaño_6(self):
        return self._tamaño_6
    @tamaño_6.setter
    def tamaño_6(self, tamaño_6):
        self._tamaño_6 = tamaño_6
    
    @property
    def tamaño_7(self):
        return self._tamaño_7
    @tamaño_7.setter
    def tamaño_7(self, tamaño_7):
        self._tamaño_7 = tamaño_7

    @property
    def tamaño_8(self):
        return self._tamaño_8
    @tamaño_8.setter
    def tamaño_8(self, tamaño_8):
        self._tamaño_8 = tamaño_8

    @property
    def tamaño_9(self):
        return self._tamaño_9
    @tamaño_9.setter
    def tamaño_9(self, tamaño_9):
        self._tamaño_9 = tamaño_9

    @property
    def tamaño_10(self):
        return self._tamaño_10
    @tamaño_10.setter
    def tamaño_10(self, tamaño_10):
        self._tamaño_10 = tamaño_10

    @property
    def tamaño_11(self):
        return self._tamaño_11
    @tamaño_11.setter
    def tamaño_11(self, tamaño_11):
        self._tamaño_11 = tamaño_11

    @property
    def tamaño_12(self):
        return self._tamaño_12
    @tamaño_12.setter
    def tamaño_12(self, tamaño_12):
        self._tamaño_12 = tamaño_12

    @property
    def tamaño_13(self):
        return self._tamaño_13
    @tamaño_13.setter
    def tamaño_13(self, tamaño_13):
        self._tamaño_13 = tamaño_13

    @property
    def tamaño_14(self):
        return self._tamaño_14
    @tamaño_14.setter
    def tamaño_14(self, tamaño_14):
        self._tamaño_14 = tamaño_14

    @property
    def tamaño_15(self):
        return self._tamaño_15
    @tamaño_15.setter
    def tamaño_15(self, tamaño_15):
        self._tamaño_15 = tamaño_15


    @property
    def tamaño_4(self):
        return self._tamaño_4
    @tamaño_4.setter
    def tamaño_4(self, tamaño_4):
        self._tamaño_4 = tamaño_4
    
    @property
    def tamaño_5(self):
        return self._tamaño_5
    @tamaño_5.setter
    def tamaño_5(self, tamaño_5):
        self._tamaño_5 = tamaño_5

    @property
    def tamaño_2(self):
        return self._tamaño_2
    @tamaño_2.setter
    def tamaño_2(self, tamaño_2):
        self._tamaño_2 = tamaño_2

    @property
    def posicion_meta(self):
        return self._posicion_meta
    @posicion_meta.setter
    def posicion_meta(self, posicion_meta):
        self._posicion_meta = posicion_meta

    @property
    def posicion_x(self):
        return self._posicion_x
    @posicion_x.setter
    def posicion_x(self, posicion_x):
        self._posicion_x = posicion_x
    
    @property
    def posicion_y(self):
        return self._posicion_y
    @posicion_y.setter
    def posicion_y(self, posicion_y):
        self._posicion_y = posicion_y

    @property
    def posicion_z(self):
        return self._posicion_z
    @posicion_z.setter
    def posicion_z(self, posicion_z):
        self._posicion_z = posicion_z

    @property
    def posicion_anterior(self):
        return self._posicion_anterior
    @posicion_anterior.setter
    def posicion_anterior(self, posicion_anterior):
        self._posicion_anterior = posicion_anterior

    #VELOCIDADES
    @property
    def velocidad_angular(self):
        return self._velocidad_angular
    @velocidad_angular.setter
    def velocidad_angular(self, velocidad_angular):
        self._velocidad_angular = velocidad_angular

    @property
    def velocidad_x(self):
        return self._velocidad_x
    @velocidad_x.setter
    def velocidad_x(self, velocidad_x):
        self._velocidad_x = velocidad_x

    @property
    def velocidad_y(self):
        return self._velocidad_y
    @velocidad_y.setter
    def velocidad_y(self, velocidad_y):
        self._velocidad_y = velocidad_y
    
    #DIRRECIONES
    @property
    def direccion(self):
        return self._direccion
    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion
    
    #EXTREMOS
    @property
    def extremo_izquierdo(self):
        return self._extremo_izquierdo
    @extremo_izquierdo.setter
    def extremo_izquierdo(self, extremo_izquierdo):
        self._extremo_izquierdo = extremo_izquierdo

    @property
    def extremo_derecho(self):
        return self._extremo_derecho
    @extremo_derecho.setter
    def extremo_derecho(self, extremo_derecho):
        self._extremo_derecho = extremo_derecho

    @property
    def extremo_superior(self):
        return self._extremo_superior
    @extremo_superior.setter
    def extremo_superior(self, extremo_superior):
        self._extremo_superior = extremo_superior   

    @property
    def extremo_inferior(self):
        return self._extremo_inferior
    @extremo_inferior.setter
    def extremo_inferior(self, extremo_inferior):
        self._extremo_inferior = extremo_inferior

    #ANGULOS
    @property
    def angulo(self):
        return self._angulo
    @angulo.setter
    def angulo(self, angulo):
        self._angulo = angulo

    #ROTACION
    @property
    def rotacion(self):
        return self._rotacion
    @angulo.setter
    def rotacion(self, rotacion):
        self._rotacion = rotacion

    # Inicializar
    def __init__(self, posicion_x = 0.0, posicion_y = 0.0, posicion_z = 0.0,
        velocidad = 0.0, direccion = 0.0, velocidad_angular = 135.0, angulo = 0.0, rotacion = 0.0):
        self._posicion_x = posicion_x
        self._posicion_y = posicion_y
        self._posicion_z = posicion_z
        self._velocidad = velocidad
        self._velocidad_angular = velocidad_angular
        self._direccion = direccion
        self._angulo = angulo
        self._rotacion = rotacion

    def colisionando(self, modelo):
       
        assert isinstance(modelo, Modelo)
        colisionando = False

        if (self.posicion_x + self.extremo_derecho >= modelo.posicion_x - modelo.extremo_izquierdo
            and self.posicion_x - self.extremo_izquierdo <= modelo.posicion_x + modelo.extremo_derecho
            and self.posicion_y + self.extremo_superior >= modelo.posicion_y - modelo.extremo_inferior
            and self.posicion_y - self.extremo_inferior <= modelo.posicion_y + modelo.extremo_superior):

            colisionando = True

        return colisionando