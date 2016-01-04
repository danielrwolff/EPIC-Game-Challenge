# tools.py
# Daniel Wolff
# 11/11/2015

import math


class Camera :

    def __init__(self, xPos, yPos, zoom, width, height, buff, maxZoom, minZoom) :
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
        self.maxZoom = maxZoom
        self.minZoom = minZoom

    def getZoom(self) :
        return self.zoom

    def getXPos(self) :
        return self.xPos

    def getYPos(self) :
        return self.yPos

    def determinePosition(self, p1, p2) :
        '''
        Determine the position and zoom of the camera based on player positions.
        :param p1: Player 1.
        :param p2: Player 2.
        :return: None
        '''

        dx = abs(p1.getXCenter() - p2.getXCenter())
        dy = abs(p1.getYCenter() - p2.getYCenter())

        if dx > dy :
            self.zoom = self.WIDTH/(dx + self.buffer)
        else:
            self.zoom = self.HEIGHT/(dy + self.buffer)

        if self.zoom < self.minZoom :
            self.zoom = self.minZoom
        elif self.zoom > self.maxZoom :
            self.zoom = self.maxZoom

        self.xPos = (p1.getXCenter() + p2.getXCenter())/2.0
        self.yPos = (p1.getYCenter() + p2.getYCenter())/2.0

    def transToGameScreen(self, x, y) :
        '''
        Translates coordinates to the game screen coordinates.
        :param x: x position to translate.
        :param y: y position to translate.
        :return: Tuple - (x,y)
        '''
        return (x - self.xPos)*self.zoom + self.WIDTH/2.0, (y-self.yPos)*self.zoom + self.HEIGHT/2.0

    def zoomToGameScreen(self, w, h) :
        '''
        Zooms objects to the game screen.
        :param w: width to zoom.
        :param h: height to zoom.
        :return: Tuple - (w,h)
        '''
        return int(w*self.zoom), int(h*self.zoom)



class Physics :

    def __init__(self) :
        '''
        Initialize the physics instance.
        :return: None
        '''
        self.gravity = Vector(0.98, 90)

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



class Button :

    def __init__(self, pygame, x, y, w, h, t, fill, outline, text = None, textFont = None, textSize = None, textColour = None) :
        '''
        Initialize button.
        :param pygame: PyGame instance.
        :param x: x position.
        :param y: y position.
        :param w: Width.
        :param h: Height.
        :param t: Target menu ID.
        :param fill: Fill colour.
        :param outline: Outline colour.
        :param text: Text object.
        :param textFont: Text font.
        :param textSize: Text size.
        :param textColour: Text colour.
        :return: None
        '''

        self.xPos = x
        self.yPos = y
        self.width = w
        self.height = h
        self.targetID = t
        self.fill = fill
        self.outline = outline
        if text is not None :
            self.text = Text(pygame, text, x + 10, y + h/2.0 - (textSize+5)/2.0, textFont, textSize, textColour)

    def draw(self, screen, pygame) :
        '''
        Draw the button.
        :param screen: Screen to draw the objects on.
        :param pygame: PyGame instance.
        :return: None
        '''
        pygame.draw.rect(screen, self.fill, (self.xPos, self.yPos, self.width, self.height))
        pygame.draw.rect(screen, self.outline, (self.xPos, self.yPos, self.width, self.height), 1)
        self.text.draw(screen, pygame)

    def isClicked(self, mx, my) :
        '''
        Check to see if the button has been clicked.
        :param mx: Mouse x position.
        :param my: Mouse y position.
        :return: Boolean
        '''
        if self.xPos <= mx <= self.xPos + self.width and self.yPos <= my <= self.yPos + self.height :
            return True
        return False

    def getTargetID(self) :
        return self.targetID

class Text :

    def __init__(self, pygame, text, x, y, font, size, col) :
        '''
        Initialize text.
        :param text: Text string.
        :param x: x position.
        :param y: y position.
        :param font: Text font name (string).
        :param size: Text font size.
        :param col: Text colour.
        :return: None
        '''
        self.text = text
        self.xPos = x
        self.yPos = y
        self.fontLoc = (pygame.font.match_font(font))
        self.font = pygame.font.Font(self.fontLoc,size)
        self.colour = col

    def draw(self, screen, pygame) :
        '''
        Draw the text to a surface.
        :param screen: Surface to draw to.
        :param pygame: Pygame instance.
        :return: None
        '''
        rend = self.font.render(self.text, True, self.colour)
        screen.blit(rend,[self.xPos,self.yPos])

    def setText(self, text) :
        '''
        Set the text.
        :param text: Text string.
        :return: None
        '''
        self.text = text