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

    def getImages(self, pygame) :

        playerAnim = []
        for i in range(1, 7) :
            playerAnim.append(pygame.image.load(os.path.join("data", "Walk_Right" + str(i) + ".png")).convert_alpha())

        return [playerAnim]

class Sprite :

    def __init__(self, anim) :
        '''
        Initialize the sprite.
        :return: None
        '''
        self.animContent = anim

        self.stage = 0
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
