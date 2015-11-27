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

        self.physics = Physics()

        self.player1 = Sprite(self.sprites, 100, 100)

    def update(self) :
        '''
        Update the game manager.
        :return: None
        '''
        self.player1.update(self.physics)

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
            self.player1.jump()
        elif key == self.P1DOWN :
            print key
        elif key == self.P1LEFT :
            self.player1.goDirection('L')
        elif key == self.P1RIGHT :
            self.player1.goDirection('R')

    def doKeyUp(self, key) :

        if key == self.P1UP :
            print key
        elif key == self.P1DOWN :
            print key
        elif key == self.P1LEFT :
            self.player1.stop()
        elif key == self.P1RIGHT :
            self.player1.stop()

    def getImages(self, pygame) :
        '''
        Rerieve all of the image files.
        :param pygame: pygame
        :return: None
        '''

        leftAnim = []
        rightAnim = []

        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Fall_Right.png")).convert_alpha())
        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Stationary_Right.png")).convert_alpha())
        for i in range(1, 7) :
            rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Walk_Right" + str(i) + ".png")).convert_alpha())

        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Fall_Left.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Stationary_Left.png")).convert_alpha())
        for i in range(1, 7) :
            leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Walk_Left" + str(i) + ".png")).convert_alpha())

        return [leftAnim, rightAnim]

class Sprite :

    def __init__(self, anim, xPos, yPos) :
        '''
        Initialize the sprite.
        :return: None
        '''
        self.animContent = anim

        self.direction = 'L'
        self.move = False
        self.grounded = True
        self.stage = 1
        '''
        Stage 0: Fall
        Stage 1: Stand Stationary
        Stage 2 - 3: Start running
        Stage 4 - 7: Running animation
        '''
        self.frameDelay = 3
        self.frameCount = 0

        self.groundSpeed = 5
        self.fallSpeedX = 3
        self.jumpSpeed = -10
        self.xPos = xPos
        self.yPos = yPos
        self.vel = Vector(0, 0)

    def update(self, physics) :
        '''
        Update the sprite.
        :return: None
        '''
        self.frameCount += 1

        if self.move :
            if self.grounded :
                if self.direction == 'L' :
                    self.vel.setMagX(self.groundSpeed*-1)
                else :
                    self.vel.setMagX(self.groundSpeed)
            else :
                if self.direction == 'L' :
                    self.vel.setMagX(self.fallSpeedX*-1)
                else :
                    self.vel.setMagX(self.fallSpeedX)
        else :
            self.vel.setMagX(0)

        self.vel = physics.applyGravity(self.vel)

        if self.stage >= 3 or self.stage == 0 :
            self.xPos += self.vel.getMagX()

        self.yPos += self.vel.getMagY()

        # When the frame count is greater than or equal to the frame delay, update the stage.
        if self.frameCount >= self.frameDelay :
            self.frameCount = 0

            if self.grounded :
                # ...
                if self.move :
                    if self.stage >= 7 :
                        self.stage = 4
                    else :
                        self.stage += 1
                else :
                    self.stage = 1
            else :
                self.stage = 0

    def draw(self, screen, pygame) :
        '''
        Draw the sprite.
        :return: None
        '''
        if self.direction == 'L' :
            screen.blit(self.animContent[0][self.stage], (self.xPos, self.yPos))
        else :
            screen.blit(self.animContent[1][self.stage], (self.xPos, self.yPos))

    def goDirection(self, direction) :
        '''
        Move in the direction specified.
        :param direction: (Char) Direction.
        :return: None
        '''
        self.direction = direction
        self.move = True

    def jump(self) :
        '''
        Make the player jump.
        :return: None
        '''
        self.grounded = False
        self.vel.setMagY(self.jumpSpeed)

    def stop(self) :
        '''
        Stops the player from running.
        :return: None
        '''
        self.move = False

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