# game.py
# Daniel Wolff
# 11/11/2015

import os
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
        self.P1PUNCH = pygame.K_COMMA
        self.P1KICK = pygame.K_PERIOD

        self.P2UP = pygame.K_w
        self.P2DOWN = pygame.K_s
        self.P2LEFT = pygame.K_a
        self.P2RIGHT = pygame.K_d
        self.P2PUNCH = pygame.K_LSHIFT
        self.P2KICK = pygame.K_CAPSLOCK

        self.WIDTH = SIZE[0]
        self.HEIGHT = SIZE[1]

        self.sprites = self.getImages(pygame)

        self.physics = Physics()
        self.camera = Camera(0, 0, 1, self.WIDTH, self.HEIGHT, 200, 1, 0.5)

        self.environment = []
        self.environment.append(EnvObject(0, 0, 50, self.HEIGHT, (200, 200, 200), (180, 180, 180), 'L'))
        self.environment.append(EnvObject(self.WIDTH - 50, 0, 50, self.HEIGHT, (200, 200, 200), (180, 180, 180), 'R'))
        self.environment.append(EnvObject(0, self.HEIGHT - 50, self.WIDTH, self.HEIGHT, (200, 200, 200), (180, 180, 180), 'B'))
        self.environment.append(EnvObject(100, self.HEIGHT/2.0, self.WIDTH/2.0, 10, (200, 200, 200), (180, 180, 180)))

        self.player1 = Sprite(self.sprites, 100, 200, 50, 100, (0, 0, 0))
        self.player2 = Sprite(self.sprites, 300, 200, 50, 100, (0, 0, 0))

    def update(self) :
        '''
        Update the game manager.
        :return: None
        '''
        self.camera.determinePosition(self.player1, self.player2)
        self.player1.update(self.physics, self.environment)
        self.player2.update(self.physics, self.environment)

    def draw(self, screen, pygame) :
        '''
        Draw the objects within the game manager.
        :return: None
        '''

        for i in self.environment :
            i.draw(screen, pygame, self.camera)

        self.player1.draw(screen, pygame, self.camera)
        self.player2.draw(screen, pygame, self.camera)




    def doKeyDown(self, key) :
        '''
        Manage a key pressed.
        :param key: pygame.key event.
        :return: None
        '''

        if key == self.P1KICK :
            self.player1.kick()
        elif key == self.P1PUNCH :
            self.player1.punch()

        elif key == self.P2KICK :
            self.player2.kick()
        elif key == self.P2PUNCH :
            self.player2.punch()

        elif key == self.P1UP :
            self.player1.jump()
        elif key == self.P1DOWN :
            self.player1.crouch()
        elif key == self.P1LEFT :
            self.player1.goDirection(-1)
        elif key == self.P1RIGHT :
            self.player1.goDirection(1)

        elif key == self.P2UP :
            self.player2.jump()
        elif key == self.P2DOWN :
            self.player2.crouch()
        elif key == self.P2LEFT :
            self.player2.goDirection(-1)
        elif key == self.P2RIGHT :
            self.player2.goDirection(1)

    def doKeyUp(self, key) :
        '''
        Manage a key released.
        :param key: pygame.key event.
        :return: None
        '''
        #if key == self.P1UP :
        #    print key
        if key == self.P1DOWN :
            self.player1.stand()
        elif key == self.P1LEFT :
            self.player1.stop()
        elif key == self.P1RIGHT :
            self.player1.stop()

        #elif key == self.P2UP :
        #    print key
        elif key == self.P2DOWN :
            self.player2.stand()
        elif key == self.P2LEFT :
            self.player2.stop()
        elif key == self.P2RIGHT :
            self.player2.stop()

    def getImages(self, pygame) :
        '''
        Rerieve all of the image files.
        :param pygame: Pygame instance.
        :return: None
        '''

        leftAnim = []
        rightAnim = []

        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Stationary_Right.png")).convert_alpha())
        for i in range(1, 7) :
            rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Walk_Right" + str(i) + ".png")).convert_alpha())

        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Fall_Right.png")).convert_alpha())
        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Fall_Right2.png")).convert_alpha())
        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Fall_Right3.png")).convert_alpha())

        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Crouch_Right1.png")).convert_alpha())
        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Crouch_Right2.png")).convert_alpha())
        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Crouch_Right3.png")).convert_alpha())

        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Roll_Right1.png")).convert_alpha())
        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Roll_Right2.png")).convert_alpha())
        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Roll_Right3.png")).convert_alpha())
        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Roll_Right4.png")).convert_alpha())
        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Roll_Right5.png")).convert_alpha())
        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Roll_Right6.png")).convert_alpha())

        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Punch_Right1.png")).convert_alpha())
        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Punch_Right2.png")).convert_alpha())
        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Punch_Right3.png")).convert_alpha())
        rightAnim.append(rightAnim[-1])

        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Stationary_Left.png")).convert_alpha())
        for i in range(1, 7) :
            leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Walk_Left" + str(i) + ".png")).convert_alpha())

        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Fall_Left.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Fall_Left2.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Fall_Left3.png")).convert_alpha())

        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Crouch_Left1.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Crouch_Left2.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Crouch_Left3.png")).convert_alpha())

        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Roll_Left1.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Roll_Left2.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Roll_Left3.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Roll_Left4.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Roll_Left5.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Roll_Left6.png")).convert_alpha())

        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Punch_Left1.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Punch_Left2.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Punch_Left3.png")).convert_alpha())
        leftAnim.append(leftAnim[-1])

        return [leftAnim, rightAnim]



class GameObject :

    def __init__(self, xPos, yPos, width, height, fill=(0,0,0), outline=(0,0,0)) :
        '''
        Initialize the game object.
        :param xPos: X position.
        :param yPos: Y position.
        :param width: Width of object.
        :param height: Height of object.
        :param fill: Fill colour.
        :param outline: Outline colour.
        :return: None
        '''

        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height
        self.fill = fill
        self.outline = outline

    def getXPos(self) :
        return self.xPos

    def getYPos(self) :
        return self.yPos

    def getWidth(self) :
        return self.width

    def getHeight(self) :
        return self.height



class Sprite (GameObject) :

    def __init__(self, anim, xPos, yPos, width, height, col) :
        '''
        Initialize the sprite.
        :param anim: Animation images.
        :param xPos: X position.
        :param yPos: Y position.
        :return: None
        '''

        GameObject.__init__(self, xPos, yPos, width, height)

        self.animContent = anim

        self.hitBoxes = [   (10,0,30,30), (15,30,20,70)   ]

        self.currentDir = 0
        self.lastDir = 'L'
        self.attackStages = ((17,20),())
        self.grounded = True
        self.crouched = False
        self.allowDoubleJump = True
        self.allowStateChange = True
        self.animStage = 0
        self.action = 0

        '''
        Action 0, Anim 0: Stand Stationary
        Action 1, Anim 1: Start running
        Action 2, Anim 2 - 6: Running animation
        Action 3, Anim 7 - 9: Falling animation
        Action 4, Anim 10 - 12: Crouch animation
        Action 5, Anim 13 - 18: Roll animation
        Action 6, Anim 19 - 22: Punch animation 1
        '''

        self.frameDelay = 3
        self.frameCount = 0

        self.groundSpeed = 5
        self.dashDistance = 6/3
        self.rollDistance = 6
        self.fallSpeedX = 3
        self.jumpSpeed = -15

        self.vel = Vector(0, 0)

    def update(self, physics, objs) :
        '''
        Update the sprite.
        :param physics: Physics instance.
        :return: None
        '''
        self.frameCount += 1

        if self.currentDir == -1 :
            self.lastDir = 'L'
        elif self.currentDir == 1 :
            self.lastDir = 'R'

        if 2 <= self.action <= 3 :
            if self.grounded :
                self.vel.setMagX(self.groundSpeed * self.currentDir)
            else :
                self.vel.setMagX(self.fallSpeedX * self.currentDir)
        else :
            self.vel.setMagX(0)

        self.vel = physics.applyGravity(self.vel)

        if 2 <= self.action <= 3 :
            self.xPos += self.vel.getMagX()
        elif self.action == 4:
            self.vel.setMagX(0)
            self.currentDir = 0
        elif self.action == 5 :
            self.xPos += self.rollDistance * self.currentDir

        self.yPos += self.vel.getMagY()

        # COLLISIONS
        self.checkCollisions(objs)

        if self.grounded and self.action == 3 :
            if self.currentDir != 0 :
                self.action = 1
            else :
                self.action = 0
        elif not self.grounded and self.action <= 4 :
            self.action = 3

        # When the frame count is greater than or equal to the frame delay, update the stage.
        if self.frameCount >= self.frameDelay :
            self.frameCount = 0

            if self.action == 0 :
                if 10 < self.animStage <= 12 :
                    self.animStage -= 1
                else :
                    self.animStage = 0

            elif self.action == 1:
                self.animStage += 1
                self.action += 1

            elif self.action == 2:
                if self.animStage < 6 :
                    self.animStage += 1
                else :
                    self.animStage = 3

            elif self.action == 3:
                if self.vel.getMagY() < -3 :
                    self.animStage = 7
                elif self.vel.getMagY() > 3 :
                    self.animStage = 9
                else :
                    self.animStage = 8

            elif self.action == 4 :
                if not self.crouched :
                    if self.currentDir == 0 :
                        self.action = 0
                    else :
                        self.action = 1
                if 10 <= self.animStage < 12 :
                    self.animStage += 1
                else :
                    self.animStage = 12

            elif self.action == 5:
                if self.animStage < 12 :
                    self.animStage = 12
                elif 12 <= self.animStage < 18 :
                    self.animStage += 1
                    self.allowStateChange = False
                else :
                    self.animStage = 12
                    self.allowStateChange = True
                    self.action = 4


    def draw(self, screen, pygame, camera) :
        '''
        Draw the sprite.
        :param screen: Surface to draw to.
        :param pygame: Pygame instance.
        :param camera: Camera instance.
        :return: None
        '''

        ### TEMP

        for i in self.hitBoxes :
            pos = camera.transToGameScreen(self.xPos + i[0], self.yPos + i[1])
            zoom = camera.zoomToGameScreen(int(i[2]), int(i[3]))

            #pygame.draw.rect(screen, (255,(i[1]*2),0), (pos[0], pos[1], zoom[0], zoom[1]))

        ### TEMP

        if self.lastDir == 'L' :
            screen.blit(pygame.transform.smoothscale(self.animContent[0][self.animStage],
                                                        camera.zoomToGameScreen(int(self.width), int(self.height))),
                                                        camera.transToGameScreen(self.xPos, self.yPos))
        else :
            screen.blit(pygame.transform.smoothscale(self.animContent[1][self.animStage],
                                                        camera.zoomToGameScreen(int(self.width), int(self.height))),
                                                        camera.transToGameScreen(self.xPos, self.yPos))

    def goDirection(self, direction) :
        '''
        Move in the direction specified.
        :param direction: (Char) Direction.
        :return: None
        '''
        if not self.allowStateChange :
            return

        self.currentDir = direction
        if self.grounded :
            if self.action == 4:
                self.action = 5
            else :
                self.action = 1
        else :
            self.action = 3

    def jump(self) :
        '''
        Make the player jump.
        :return: None
        '''
        if not self.allowStateChange :
            return

        self.action = 3
        if self.grounded :
            self.vel.setMagY(self.jumpSpeed)
            self.grounded = False
        elif self.allowDoubleJump :
            self.vel.setMagY(self.jumpSpeed)
            self.allowDoubleJump = False

    def stop(self) :
        '''
        Stops the player from running.
        :return: None
        '''
        if not self.allowStateChange :
            return

        self.currentDir = 0
        if self.action not in (4, 5) :
            self.action = 0

    def punch(self) :
        '''
        Make the sprite punch.
        :return: None
        '''
        #self.action = 6
        if not self.allowStateChange :
            return
        return

    def kick(self) :
        '''
        Make the sprite kick.
        :return: None
        '''
        #self.action = 7
        if not self.allowStateChange :
            return
        return

    def crouch(self) :
        '''
        Make the sprite crouch.
        :return: None
        '''
        self.crouched = True

        if not self.allowStateChange :
            return

        if self.currentDir == 0 :
            self.action = 4
            self.animStage = 10
        else :
            self.action = 5
            self.animStage = 12


    def stand(self) :
        '''
        Make the sprite stand.
        :return: None
        '''
        self.crouched = False

        if not self.allowStateChange :
            return

        if self.currentDir == 0 :
            self.action = 0
        else :
            self.action = 1

    def checkCollisions(self, objs) :
        '''
        Check for any collisions with the given objects.
        :param objs: Objects.
        :return: None
        '''

        self.grounded = False

        for i in objs :
            boundary = i.getBoundary()
            if boundary == 'L' and self.xPos + self.hitBoxes[1][0] < i.getXPos() + i.getWidth() :
                self.xPos = i.getXPos() + i.getWidth() - self.hitBoxes[1][0]
                self.vel.setMagX(0)

            elif boundary == 'R' and self.xPos + self.hitBoxes[1][0] + self.hitBoxes[1][2] > i.getXPos() :
                self.xPos = i.getXPos() - self.hitBoxes[1][0] - self.hitBoxes[1][2]
                self.vel.setMagX(0)

            elif boundary == 'B' and self.yPos + self.height > i.getYPos() :
                self.yPos = i.getYPos() - self.height
                self.vel.setMagY(0)
                self.grounded = True
                self.allowDoubleJump = True

            else :
                # Probably need some better collision here, but this should do for now:
                if (i.getXPos() < self.xPos + self.hitBoxes[1][0] + self.hitBoxes[1][2] and
                            self.xPos + self.hitBoxes[1][0] < i.getXPos() + i.getWidth() and
                            i.getYPos() < self.yPos + self.height < i.getYPos() + i.getHeight() and
                            self.vel.getMagY() > 0) :

                    self.yPos = i.getYPos() - self.height
                    self.vel.setMagY(0)
                    self.grounded = True
                    self.allowDoubleJump = True

    def getXCenter(self) :
        return self.getXPos() + self.getWidth()/2.0

    def getYCenter(self) :
        return self.getYPos() + self.getHeight()/2.0



class EnvObject (GameObject) :

    def __init__(self, xPos, yPos, width, height, fill, outline, boundary = 'NA'):
        '''
        Initializes an environment object.
        :param xPos: x position.
        :param yPos: y position.
        :param width: width of object.
        :param height: height of object.
        :param fill: fill colour.
        :param outline: outline colour.
        :return: None
        '''
        GameObject.__init__(self, xPos, yPos, width, height, fill, outline)
        self.boundary = boundary

    def draw(self, screen, pygame, camera) :

        pos = camera.transToGameScreen(self.xPos, self.yPos)
        size = camera.zoomToGameScreen(self.width, self.height)

        pygame.draw.rect(screen, self.fill, (pos[0], pos[1], size[0], size[1]))
        pygame.draw.rect(screen, self.outline, (pos[0], pos[1], size[0], size[1]), 1)

    def getBoundary(self) :
        return self.boundary

