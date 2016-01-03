# game.py
# Daniel Wolff
# 11/11/2015

import os, random
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
        self.environment.append(EnvObject(100, self.HEIGHT/2.0, self.WIDTH/2.0, 15, (200, 200, 200), (180, 180, 180)))

        self.player1 = Sprite(pygame, self.sprites, 100, 200, 50, 100, (0, 0, 0))
        self.player2 = Sprite(pygame, self.sprites, 300, 200, 50, 100, (255, 0, 0))

        self.attacks = [None,None]

    def update(self) :
        '''
        Update the game manager.
        :return: None
        '''
        self.camera.determinePosition(self.player1, self.player2)
        self.attacks[0] = self.player1.update(self.physics, self.environment)
        self.attacks[1] = self.player2.update(self.physics, self.environment)

        self.player1.opposingAttacks(self.attacks[1])
        self.player2.opposingAttacks(self.attacks[0])

    def draw(self, screen, pygame) :
        '''
        Draw the objects within the game manager.
        :param screen: Screen to draw the objects on.
        :param pygame: PyGame instance.
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

        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Roll_Right1.png")).convert_alpha())
        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Roll_Right2.png")).convert_alpha())
        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Roll_Right3.png")).convert_alpha())
        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Roll_Right4.png")).convert_alpha())
        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Roll_Right5.png")).convert_alpha())
        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Roll_Right6.png")).convert_alpha())

        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Punch_Right1.png")).convert_alpha())
        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Punch_Right2.png")).convert_alpha())
        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "CrouchPunch_Right1.png")).convert_alpha())
        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "CrouchPunch_Right2.png")).convert_alpha())

        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Kick_Right1.png")).convert_alpha())
        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Kick_Right2.png")).convert_alpha())
        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Launch_Right.png")).convert_alpha())
        rightAnim.append(pygame.image.load(os.path.join("data", "Right", "Lay_Right.png")).convert_alpha())


        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Stationary_Left.png")).convert_alpha())
        for i in range(1, 7) :
            leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Walk_Left" + str(i) + ".png")).convert_alpha())

        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Fall_Left.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Fall_Left2.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Fall_Left3.png")).convert_alpha())

        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Crouch_Left1.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Crouch_Left2.png")).convert_alpha())

        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Roll_Left1.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Roll_Left2.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Roll_Left3.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Roll_Left4.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Roll_Left5.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Roll_Left6.png")).convert_alpha())

        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Punch_Left1.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Punch_Left2.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "CrouchPunch_Left1.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "CrouchPunch_Left2.png")).convert_alpha())

        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Kick_Left1.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Kick_Left2.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Launch_Left.png")).convert_alpha())
        leftAnim.append(pygame.image.load(os.path.join("data", "Left", "Lay_Left.png")).convert_alpha())


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

    def __init__(self, pygame, anim, xPos, yPos, width, height, col) :
        '''
        Initialize the sprite.
        :param anim: Animation images.
        :param xPos: X position.
        :param yPos: Y position.
        :param col: Sprite colour.
        :return: None
        '''

        GameObject.__init__(self, xPos, yPos, width, height)

        self.colour = col
        self.animContent = anim

        self.hitBoxes = [   [(10,0,30,30), (15,30,20,70)],
                            [(10,50,30,50)]                      ]

        self.currentDir = 0
        self.lastDir = -1
        self.attackStages = ((18,19),(20,21),(22,23))
        self.grounded = True
        self.crouched = False
        self.allowDoubleJump = True
        self.allowStateChange = True
        self.handicap = False
        self.animStage = 0
        self.action = 0

        '''
        Action 0, Anim 0: Stand Stationary
        Action 1, Anim 1: Start running
        Action 2, Anim 2 - 6: Running animation
        Action 3, Anim 7 - 9: Falling animation
        Action 4, Anim 10 - 11: Crouch animation
        Action 5, Anim 12 - 17: Roll animation
        Action 6, Anim 18 - 19: Punch animation
        Action 7, Anim 20 - 21: Crouch Punch animation
        Action 8, Anim 22 - 23: Kick animation
        Action 9, Anim 24: Launch animation
        Action 10, Anim 25: Lay animation
        '''

        self.frameDelay = 3
        self.frameCount = 0

        self.groundSpeed = 5
        self.dashDistance = 2
        self.rollDistance = 6
        self.fallSpeedX = 3
        self.jumpSpeed = -15
        self.defaultLaunchSpeed = 10

        self.damage = 0

        self.lastXPos = self.xPos
        self.lastYPos = self.yPos
        self.vel = Vector(0, 0)

    def update(self, physics, objs) :
        '''
        Update the sprite.
        :param physics: Physics instance.
        :param objs: Environment objects.
        :return: Attack position (x,y), or None.
        '''

        ### POSITIONS
        self.frameCount += 1

        if self.currentDir != 0 :
            self.lastDir = self.currentDir

        if 2 <= self.action <= 3 :
            if self.grounded :
                self.vel.setMagX(self.groundSpeed * self.currentDir)
            else :
                self.vel.setMagX(self.fallSpeedX * self.currentDir)
        else :
            if self.grounded :
                self.vel.setMagX(self.vel.getMagX()/2.0)
                if abs(self.vel.getMagX()) < 1 :
                    self.vel.setMagX(0)

        self.vel = physics.applyGravity(self.vel)

        self.lastXPos = self.xPos
        self.lastYPos = self.yPos

        if self.action <= 3 :
            self.xPos += self.vel.getMagX()
        elif self.action == 4:
            self.xPos += self.vel.getMagX()
            self.currentDir = 0
        elif self.action == 5 :
            self.xPos += self.rollDistance * self.currentDir
        elif self.action in (6,8) :
            self.xPos += self.dashDistance * self.lastDir
        elif self.action == 9 :
            self.xPos += self.vel.getMagX()

        self.yPos += self.vel.getMagY()
        ###

        ### COLLISIONS
        self.checkCollisions(objs, self.hitBoxes[int(self.crouched)][int(not self.crouched)])

        if self.grounded and self.action == 3 :
            if self.currentDir != 0 :
                self.action = 1
            else :
                self.action = 0
        elif self.grounded and self.action == 9 :
            self.action = 0
            self.handicap = False
        elif not self.grounded and self.action <= 4 :
            self.action = 3
        ###

        ### ANIMATIONS
        if self.frameCount >= self.frameDelay :
            self.frameCount = 0

            if self.action == 0 :
                if 10 < self.animStage <= 12 :
                    self.animStage -= 1
                else :
                    self.animStage = 0

            elif self.action == 1:
                self.animStage = 1
                self.action = 2

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
                if self.animStage < 10 :
                    self.animStage = 10
                elif 10 <= self.animStage < 11 :
                    self.animStage += 1
                else :
                    self.animStage = 11

            elif self.action == 5:
                if self.animStage < 11 or self.animStage > 17 :
                    self.animStage = 11
                    self.allowStateChange = False
                elif 11 <= self.animStage < 17 :
                    self.animStage += 1
                    self.allowStateChange = False
                else :
                    self.animStage = 11
                    self.allowStateChange = True
                    self.action = 4

            elif self.action == 6 :
                if self.animStage < self.attackStages[0][0] :
                    self.animStage = self.attackStages[0][0]
                    self.allowStateChange = False
                elif self.attackStages[0][0] <= self.animStage < self.attackStages[0][1]  :
                    self.animStage += 1
                else :
                    self.allowStateChange = True
                    if self.currentDir == 0 :
                        self.action = 0
                    else :
                        self.action = 1

            elif self.action == 7 :
                if self.animStage < self.attackStages[1][0] :
                    self.animStage = self.attackStages[1][0]
                    self.allowStateChange = False
                elif self.attackStages[1][0] <= self.animStage < self.attackStages[1][1]  :
                    self.animStage += 1
                else :
                    self.allowStateChange = True
                    self.action = 4

            elif self.action == 8 :
                if self.animStage < self.attackStages[2][0] :
                    self.animStage = self.attackStages[2][0]
                    self.allowStateChange = False
                elif self.attackStages[2][0] <= self.animStage < self.attackStages[2][1] :
                    self.animStage += 1
                else :
                    self.allowStateChange = True
                    if self.currentDir == 0 :
                        self.action = 0
                    else :
                        self.action = 1

            elif self.action == 9 :
                self.allowStateChange = True
                if self.animStage != 24 :
                    self.animStage = 24

            elif self.action == 10 :
                self.allowStateChange = False
                if self.animStage != 25 :
                    self.animStage = 25
        ###

        ### ATTACKS
        if self.lastDir == 1 :
            if self.animStage == self.attackStages[0][1] :
                return self.xPos + self.width, self.yPos + 40, self.xPos + self.width/2.0, self.lastDir
            elif self.animStage == self.attackStages[1][1] :
                return self.xPos + self.width, self.yPos + 75, self.xPos + self.width/2.0, self.lastDir
            elif self.animStage == self.attackStages[2][1] :
                return self.xPos + self.width, self.yPos + 70, self.xPos + self.width/2.0, self.lastDir
            else :
                return None
        else :
            if self.animStage == self.attackStages[0][1] :
                return self.xPos, self.yPos + 40, self.xPos + self.width/2.0, self.lastDir
            elif self.animStage == self.attackStages[1][1] :
                return self.xPos, self.yPos + 75, self.xPos + self.width/2.0, self.lastDir
            elif self.animStage == self.attackStages[2][1] :
                return self.xPos, self.yPos + 70, self.xPos + self.width/2.0, self.lastDir
            else :
                return None
        ###

    def draw(self, screen, pygame, camera) :
        '''
        Draw the sprite.
        :param screen: Surface to draw to.
        :param pygame: Pygame instance.
        :param camera: Camera instance.
        :return: None
        '''

        ### TEMP

        for i in self.hitBoxes[0] :
            pos = camera.transToGameScreen(self.xPos + i[0], self.yPos + i[1])
            zoom = camera.zoomToGameScreen(int(i[2]), int(i[3]))

            #pygame.draw.rect(screen, (255,(i[1]*2),0), (pos[0], pos[1], zoom[0], zoom[1]))

        ### TEMP

        if self.animStage == 25 :
            w = int(self.width*2)
        else :
            w = int(self.width)

        if self.lastDir == -1 :
            screen.blit(pygame.transform.smoothscale(self.animContent[0][self.animStage],
                                                        camera.zoomToGameScreen(w, int(self.height))),
                                                        camera.transToGameScreen(self.xPos, self.yPos))
        else :
            screen.blit(pygame.transform.smoothscale(self.animContent[1][self.animStage],
                                                        camera.zoomToGameScreen(w, int(self.height))),
                                                        camera.transToGameScreen(self.xPos, self.yPos))

    def goDirection(self, direction) :
        '''
        Move in the direction specified.
        :param direction: (Int) Direction.
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

        if self.action not in (4, 5) :
            self.currentDir = 0

        if not self.allowStateChange :
            return

        if self.action not in (4, 5) :
            self.action = 0

    def punch(self) :
        '''
        Make the sprite punch.
        :return: None
        '''
        if not self.allowStateChange :
            return

        if self.action == 4 :
            self.action = 7
        else :
            self.action = 6
        return

    def kick(self) :
        '''
        Make the sprite kick.
        :return: None
        '''
        if not self.allowStateChange :
            return
        self.action = 8

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
        else :
            self.action = 5

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

    def checkCollisions(self, objs, hitbox) :
        '''
        Check for any collisions with the given objects.
        :param objs: Objects.
        :param hitbox: HItbox to check collisions with.
        :return: None
        '''

        self.grounded = False

        for i in objs :
            boundary = i.getBoundary()
            if boundary == 'L' and self.xPos + hitbox[0] < i.getXPos() + i.getWidth() :
                self.xPos = i.getXPos() + i.getWidth() - hitbox[0]
                if self.action == 9 :
                    self.vel.setMagX(self.vel.getMagX()/-2.0)
                    self.currentDir *= -1
                else :
                    self.vel.setMagX(0)

            elif boundary == 'R' and self.xPos + hitbox[0] + hitbox[2] > i.getXPos() :
                self.xPos = i.getXPos() - hitbox[0] - hitbox[2]
                if self.action == 9 :
                    self.vel.setMagX(self.vel.getMagX()/-2.0)
                    self.currentDir *= -1
                else :
                    self.vel.setMagX(0)

            elif boundary == 'B' and self.yPos + self.height > i.getYPos() :
                self.yPos = i.getYPos() - self.height
                self.vel.setMagY(0)
                self.grounded = True
                self.allowDoubleJump = True

            elif boundary == 'NA' :
                if (i.getXPos() < self.xPos + hitbox[0] + hitbox[2] and
                            self.xPos + hitbox[0] < i.getXPos() + i.getWidth() and
                            self.lastYPos + self.height <= i.getYPos() < self.yPos + self.height and
                            self.vel.getMagY() > 0) :

                    self.yPos = i.getYPos() - self.height
                    self.vel.setMagY(0)
                    self.grounded = True
                    self.allowDoubleJump = True

    def opposingAttacks(self, a) :
        '''
        Check and handle any opposing attacks that were made by the other player.
        :param a: Attack position (x,y).
        :return: None
        '''

        if a is None or self.handicap :
            return

        if self.crouched and self.checkAttackCollisions(a, self.hitBoxes[1][0]) :
            self.applyDamage(random.randint(15,20), a[3])

        elif (not self.crouched) and self.checkAttackCollisions(a, self.hitBoxes[0][0]) :
            self.applyDamage(random.randint(15,20), a[3])

        elif (not self.crouched) and self.checkAttackCollisions(a, self.hitBoxes[0][1]) :
            self.applyDamage(random.randint(7,12), a[3])


    def applyDamage(self, dam, di) :
        '''
        Apply damage and manage launch speed.
        :param dam: Damage
        :param di: Direction
        :return: None
        '''

        self.damage += dam
        self.handicap = True
        self.action = 9
        self.currentDir = di

        print self.damage

        if self.damage <= 50 :
            self.vel = Vector(self.defaultLaunchSpeed*di, random.randint(-30,-20)*di)
        else :
            self.vel = Vector(int(self.defaultLaunchSpeed*(self.damage/50.0))*di, random.randint(-45,-30)*di)

    def checkAttackCollisions(self, a, hitbox) :
        '''
        Checks to see if an attack landed a hit.
        :param a: Position of the attack (x,y).
        :param hitbox: Current hitbox.
        :return: Boolean - True if hit, False if not.
        '''

        if (((a[2] <= self.xPos + hitbox[0] <= a[0] and a[3] == 1) or
                (a[0] <= self.xPos + hitbox[0] + hitbox[2] <= a[2] and a[3] == -1)) and
                self.yPos + hitbox[1] <= a[1] <= self.yPos + hitbox[1] + hitbox[3]) :
            return True
        return False

    def getXCenter(self) :
        return self.getXPos() + self.getWidth()/2.0

    def getYCenter(self) :
        return self.getYPos() + self.getHeight()/2.0

    def getDamage(self) :
        return self.damage



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

