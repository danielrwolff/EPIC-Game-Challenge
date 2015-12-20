# tools.py
# Daniel Wolff
# 11/11/2015

import math


class Camera :

    def __init__(self, xPos, yPos, zoom, width, height, buff) :
        '''
        Initialize the camera object.
        :param xPos: x position of camera.
        :param yPos: y position of camera.
        :param zoom: initial zoom of camera.
        :param width: screen width.
        :param height: screen height.
        :param buff: edge of screen buffer.
        :return: None
        '''

        self.WIDTH = width
        self.HEIGHT = height

        self.xPos = xPos
        self.yPos = yPos
        self.zoom = zoom
        self.buffer = buff

    def getZoom(self) :
        return self.zoom

    def getXPos(self) :
        return self.xPos

    def getYPos(self) :
        return self.yPos

    def transToGameScreen(self, x, y) :
        '''
        Translates coordinates to the game screen coordinates.
        :param x: x position to translate.
        :param y: y position to translate.
        :return: Tuple - (x,y)
        '''
        return (x + self.xPos)*self.zoom, (y + self.yPos)*self.zoom

    def zoomToGameScreen(self, w, h) :
        '''
        Zooms objects to the game screen.
        :param w: width to zoom.
        :param h: height to zoom.
        :return: Tuple - (w,h)
        '''
        return w*self.zoom, h*self.zoom



class Physics :

    def __init__(self) :
        '''
        Initialize the physics instance.
        :return: None
        '''
        self.gravity = Vector(0, 90)

    def applyGravity(self, v) :
        '''
        Apply the gravity vector to a velocity vector.
        :param v: Velocity vector.
        :return: Resultant velocity vector.
        '''
        v + self.gravity
        return v



class Vector :

    def __init__(self, mag, ang) :
        '''
        Initialize the vector object.
        :param mag: Magnitude of vector.
        :param ang: Angle of vector.
        :return: None
        '''
        self.angle = math.radians(ang)
        self.magX = float(mag)*math.cos(self.angle)
        self.magY = float(mag)*math.sin(self.angle)

    def __add__(self, other) :
        '''
        Adds other vector to the initial vector.
        :param other: Other vector.
        :return: None
        '''
        self.magX += other.getMagX()
        self.magY += other.getMagY()

    def getOpposite(self) :
        '''
        Create a vector opposite in direction but equal in magnitude.
        :return: Vector -> opposite vector.
        '''
        return Vector(self.getMag(), self.getAngD() + 180)

    def getMag(self) :
        '''
        Get the total magnitude of the vector.
        :return: Float -> magnitude.
        '''
        return math.hypot(self.magX, self.magY)

    def getMagX(self) :
        '''
        Get the x-component of the magnitude.
        :return: Float -> magnitude of x-component.
        '''
        return self.magX

    def getMagY(self) :
        '''
        Get the y-component of the magnitude.
        :return: Float -> magnitude of y-component.
        '''
        return self.magY

    def getAngR(self) :
        '''
        Get the vector angle in radians.
        :return: Float -> angle (radians).
        '''
        return self.angle

    def getAngD(self) :
        '''
        Get the vector angle in degrees.
        :return: Float -> angle (degrees).
        '''
        return math.degrees(self.angle)

    def setMagX(self, x) :
        '''
        Set the x-component of the magnitude.
        :param x: x-component
        :return: None
        '''
        self.magX = x

    def setMagY(self, y) :
        '''
        Set the y-component of the magnitude.
        :param y: y-component
        :return: None
        '''
        self.magY = y