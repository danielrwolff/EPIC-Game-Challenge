# game.py
# Daniel Wolff
# 11/11/2015

import math
from tools import *

class GameManager :

    def __init__(self, pygame, SIZE) :
        '''
        Initialize the game manager.
        :param pygame: PyGame instance.
        :param SIZE: Size of screen.
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

        self.WIDTH = SIZE[0]
        self.HEIGHT = SIZE[1]

        self.sprites = self.getImages(pygame)

        self.physics = Physics()

        self.ground = GameObject(0, self.HEIGHT - 50, self.WIDTH, self.HEIGHT, (200, 200, 200), (180, 180, 180))
        self.player1 = Sprite(self.sprites, 100, 100, 50*0.75, 100*0.75)
        self.player2 = Sprite(self.sprites, 100, 200, 50, 100)

    def update(self) :
        '''
        Update the game manager.
        :return: None
        '''
        self.player1.update(self.physics)
        self.player2.update(self.physics)

    def draw(self, screen, pygame) :
        '''
        Draw the objects within the game manager.
        :return: None
        '''
        self.player1.draw(screen, pygame)
        self.player2.draw(screen, pygame)
        self.ground.draw(screen, pygame)

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

        if key == self.P2UP :
            self.player2.jump()
        elif key == self.P2DOWN :
            print key
        elif key == self.P2LEFT :
            self.player2.goDirection('L')
        elif key == self.P2RIGHT :
            self.player2.goDirection('R')

    def doKeyUp(self, key) :

        if key == self.P1UP :
            print key
        elif key == self.P1DOWN :
            print key
        elif key == self.P1LEFT :
            self.player1.stop()
        elif key == self.P1RIGHT :
            self.player1.stop()

        if key == self.P2UP :
            print key
        elif key == self.P2DOWN :
            print key
        elif key == self.P2LEFT :
            self.player2.stop()
        elif key == self.P2RIGHT :
            self.player2.stop()

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

    def __init__(self, anim, xPos, yPos, width, height) :
        '''
        Initialize the sprite.
        :param anim: Animation images.
        :param xPos: X position.
        :param yPos: Y position.
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
        self.width = width
        self.height = height

        self.groundSpeed = 5
        self.fallSpeedX = 3
        self.jumpSpeed = -10
        self.xPos = xPos
        self.yPos = yPos
        self.vel = Vector(0, 0)

    def update(self, physics) :
        '''
        Update the sprite.
        :param physics: Physics instance.
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
        :param screen: Surface to draw to.
        :param pygame: Pygame instance.
        :return: None
        '''
        if self.direction == 'L' :
            screen.blit(pygame.transform.smoothscale(self.animContent[0][self.stage], (int(self.width), int(self.height))), (self.xPos, self.yPos))
        else :
            screen.blit(pygame.transform.smoothscale(self.animContent[1][self.stage], (int(self.width), int(self.height))), (self.xPos, self.yPos))

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



class GameObject :

    def __init__(self, xPos, yPos, width, height, col1, col2) :
        '''
        Initialize the game object.
        :param xPos: X position.
        :param yPos: Y position.
        :param width: Width of object.
        :param height: Height of object.
        :param col1: Fill colour.
        :param col2: Outline colour.
        :return: None
        '''

        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height
        self.fill = col1
        self.outline = col2

    def draw(self, screen, pygame) :
        pygame.draw.rect(screen, self.fill, (self.xPos, self.yPos, self.width, self.height))
        pygame.draw.rect(screen, self.outline, (self.xPos, self.yPos, self.width, self.height), 1)



