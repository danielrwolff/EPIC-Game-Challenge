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
            print key
        elif key == self.P1LEFT :
            self.player1.goDirection('L')
        elif key == self.P1RIGHT :
            self.player1.goDirection('R')

        elif key == self.P2UP :
            self.player2.jump()
        elif key == self.P2DOWN :
            print key
        elif key == self.P2LEFT :
            self.player2.goDirection('L')
        elif key == self.P2RIGHT :
            self.player2.goDirection('R')

    def doKeyUp(self, key) :
        '''
        Manage a key released.
        :param key: pygame.key event.
        :return: None
        '''
        #if key == self.P1UP :
        #    print key
        #elif key == self.P1DOWN :
        #    print key
        if key == self.P1LEFT :
            self.player1.stop()
        elif key == self.P1RIGHT :
            self.player1.stop()

        #elif key == self.P2UP :
        #    print key
        #elif key == self.P2DOWN :
        #    print key
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

        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Punch_Right1.png")).convert_alpha())
        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Punch_Right2.png")).convert_alpha())
        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Punch_Right3.png")).convert_alpha())

        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Stationary_Left.png")).convert_alpha())
        for i in range(1, 7) :
            leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Walk_Left" + str(i) + ".png")).convert_alpha())

        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Fall_Left.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Fall_Left2.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Fall_Left3.png")).convert_alpha())

        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Punch_Left1.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Punch_Left2.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Punch_Left3.png")).convert_alpha())

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


        self.direction = 'L'
        self.move = False
        self.attack = False
        self.attackType = 'NA'
        self.attackStages = [[10, 12, 14, 16],[]]
        self.grounded = True
        self.allowDoubleJump = True
        self.animStage = 0
        '''
        Stage 0: Stand Stationary
        Stage 1 - 2: Start running
        Stage 3 - 6: Running animation
        Stage 7 - 9: Falling animation
        Stage 10 - 12: Punch animation 1
        '''
        self.frameDelay = 3
        self.frameCount = 0

        self.groundSpeed = 5
        self.dashDistance = 6/3
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

        if 2 <= self.animStage <= 9 :
            self.xPos += self.vel.getMagX()
        elif 10 <= self.animStage <= 12 :
            if self.direction == 'L' :
                self.xPos += self.dashDistance * -1
            else :
                self.xPos += self.dashDistance

        self.yPos += self.vel.getMagY()

        # COLLISIONS
        self.checkCollisions(objs)

        # When the frame count is greater than or equal to the frame delay, update the stage.
        if self.frameCount >= self.frameDelay :
            self.frameCount = 0

            if self.grounded :

                # Attack animations.
                if self.attack :
                    self.animStage += 1
                    for i in range(1,4) :
                        if self.attackType == 'P'*i and self.animStage >= self.attackStages[0][i] :
                            self.attack = False
                            self.attackType = 'NA'
                        #elif self.attackType == 'K'*i and self.animStage >= self.attackStages[1][i] :
                        #    self.attack = False
                        #    self.attackType = 'NA'


                # Moving animations.
                elif self.move :
                    if self.animStage >= 6 :
                        self.animStage = 3
                    else :
                        self.animStage += 1

                # Sprite is stationary.
                else :
                    self.animStage = 0
            else :

                # Air attack animations.
                if self.attack :
                    #######
                    pass ##
                    #######

                # Air animations.
                elif self.vel.getMagY() < -3 :
                    self.animStage = 7
                elif self.vel.getMagY() > 3 :
                    self.animStage = 9
                else :
                    self.animStage = 8

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

        if self.direction == 'L' :
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
        self.direction = direction
        self.move = True

    def jump(self) :
        '''
        Make the player jump.
        :return: None
        '''
        if self.grounded :
            self.vel.setMagY(self.jumpSpeed)
            self.grounded = False
        elif self.allowDoubleJump and not self.grounded :
            self.vel.setMagY(self.jumpSpeed)
            self.allowDoubleJump = False

    def stop(self) :
        '''
        Stops the player from running.
        :return: None
        '''
        self.move = False

    def punch(self) :
        self.attack = True
        self.assignAttack('P', self.attackStages[0])

    def kick(self) :
        self.attack = True
        #self.assignAttack('K')

    def assignAttack(self, a, l) :
        '''
        Assign an attack to the sprite.
        :param a: Attack type.
        :param l: List of corresponding attack stages.
        :return: None
        '''
        if self.animStage < l[0] :
            self.attackType = a
            self.animStage = l[0]
        elif l[0] < self.animStage < l[1] :
            self.attackType = 2*a
        elif l[1] < self.animStage < l[2] :
            self.attackType = 3*a

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

