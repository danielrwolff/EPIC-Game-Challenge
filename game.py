# game.py
# Daniel Wolff
# 11/11/2015

import math, os

class GameManager :

    def __init__(self, pygame) :
        '''
        Initialize the game manager.
        :return: None
        '''

        self.P1UP = pygame.K_UP
        self.P1DOWN = pygame.K_DOWN
        self.P1LEFT = pygame.K_LEFT
        self.P1RIGHT = pygame.K_RIGHT

        self.P2UP = pygame.K_w
        self.P2DOWN = pygame.K_s
        self.P2LEFT = pygame.K_a
        self.P2RIGHT = pygame.K_d



        self.sprites = self.getImages(pygame)

        self.player1 = Sprite(self.sprites[0])

    def update(self) :
        '''
        Update the game manager.
        :return: None
        '''
        self.player1.update()

    def draw(self, screen, pygame) :
        '''
        Draw the objects within the game manager.
        :return: None
        '''
        self.player1.draw(screen, pygame)

    def doKeyDown(self, key) :
        '''
        Manage a key pressed.
        :param key: pygame.key event.
        :return: None
        '''
        if key == self.P1UP :
            print key
        elif key == self.P1DOWN :
            print key
        elif key == self.P1LEFT :
            self.player1.goDirection('L')
        elif key == self.P1RIGHT :
            self.player1.goDirection('R')

    def getImages(self, pygame) :
        '''
        Rerieve all of the image files.
        :param pygame: pygame
        :return: None
        '''

        playerAnim = []
        for i in range(1, 7) :
            playerAnim.append(pygame.image.load(os.path.join("data", "RightWalk", "Walk_Right" + str(i) + ".png")).convert_alpha())
        for i in range(1,7) :
            playerAnim.append(pygame.image.load(os.path.join("data", "LeftWalk", "Walk_Left" + str(i) + ".png")).convert_alpha())

        return [playerAnim]

class Sprite :

    def __init__(self, anim) :
        '''
        Initialize the sprite.
        :return: None
        '''
        self.animContent = anim

        self.direction = 'L'
        self.stage = 0
        '''
        Stage 0: Fall
        Stage 1: Stand Stationary
        Stage 2: Start running
        Stage 3 - 7: Running animation
        '''
        self.frameDelay = 5
        self.frameCount = 0

    def update(self) :
        '''
        Update the sprite.
        :return: None
        '''
        self.frameCount += 1
        if self.frameCount >= self.frameDelay :
            self.stage += 1
            if self.stage >= 6 :
                self.stage = 2
            self.frameCount = 0

    def draw(self, screen, pygame) :
        '''
        Draw the sprite.
        :return: None
        '''
        screen.blit(self.animContent[self.stage], (0,0))

    def goDirection(self, direction) :
        '''
        Move in the direction specified.
        :param direction: (Char) Direction.
        :return: None
        '''
        self.direction = direction



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
        self.magX += other.magX
        self.magY += other.mag

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
