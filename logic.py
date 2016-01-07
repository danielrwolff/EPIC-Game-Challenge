# logic.py
# Daniel Wolff
# 10/21/2015

import pygame
from os import path
from game import GameManager
from gui import UI_Gameplay, UI_Menu, UI_SplashScreen

class Logic :

    def __init__(self, _SIZE, _CAPTION) :
        '''
        Initialize the game environment.
        :param _SIZE: Size of window.
        :param _CAPTION: Caption of window.
        :return: None
        '''

        self.BLACK = (0,0,0)
        self.GREY75 = (75, 75, 75)
        self.GREY100 = (100, 100, 100)
        self.GREY150 = (150, 150, 150)
        self.GREY175 = (175, 175, 175)
        self.GREY200 = (200, 200, 200)
        self.WHITE = (255,255,255)
        self.BLUE = (0,0,255)
        self.RED = (255,0,0)

        pygame.init()

        self.window = Screen(_SIZE, _CAPTION)
        self.events = EventHandler()

        self.gameManager = GameManager(pygame, _SIZE, self.GREY150, self.GREY100, self.RED, self.BLUE)
        self.audioManager = AudioManager()

        self.menus = [  UI_SplashScreen(pygame, 0, 1, self.BLACK,
                                [
                                    ['T', ("Thanks for trying out my game!", 210, _SIZE[1]/2 - 50, 'impact', 30, self.WHITE)],
                                    ['T', ("If you find any bugs, please let me know!", 150, _SIZE[1]/2 - 20, 'impact', 30, self.WHITE)],
                                    ['T', ("(Click anywhere to begin)", 290, _SIZE[1]/2 + 50, 'impact', 20, self.WHITE)],
                                ]),
                        UI_Menu(pygame, 1, self.GREY200,
                                [
                                    ((_SIZE[0]/4) * 3 - 100, 50, 220, 50, 4, self.GREY150, self.GREY100, "PLAY", "impact", 30, self.WHITE),
                                    ((_SIZE[0]/4) * 3 - 100, 110, 220, 50, 2, self.GREY150, self.GREY100, "CONTROLS", "impact", 30, self.WHITE),
                                    ((_SIZE[0]/4) * 3 - 100, 170, 220, 50, 3, self.GREY150, self.GREY100, "OPTIONS", "impact", 30, self.WHITE)
                                ],
                                [
                                    ['I', pygame.image.load(path.join("data", "Splash1.png")).convert(), (0,0)],
                                    ['I', pygame.image.load(path.join("data", "lolguy.png")).convert_alpha(), (_SIZE[0] - 300,_SIZE[1] - 350)],
                                    ['T', ("SUPER", 20, -20, 'impact', 150, self.WHITE)],
                                    ['T', ("SMASH", 20, 120, 'impact', 150, self.WHITE)],
                                    ['T', ("STICKS", 20, 260, 'impact', 150, self.WHITE)],
                                    ['T', ("BRAWL", 20, 400, 'impact', 150, self.WHITE)],
                                ]),
                        UI_Menu(pygame, 2, self.GREY200,
                                [
                                    (_SIZE[0] / 2 - 100, _SIZE[1] / 1.25, 220, 50, 1, self.GREY150, self.GREY100, "BACK", "impact", 30, self.WHITE),
                                ],
                                [
                                    ['R', (self.GREY100, 0, 0, _SIZE[0], 105)],
                                    ['R', (self.GREY150, 0, 0, _SIZE[0], 100)],
                                    ['T', ("CONTROLS", 20, -10, 'impact', 100, self.WHITE)],
                                ]),
                        UI_Menu(pygame, 3, self.GREY200,
                                [
                                    (_SIZE[0] / 2 - 100, _SIZE[1] / 1.25, 220, 50, 1, self.GREY150, self.GREY100, "BACK", "impact", 30, self.WHITE),
                                ],
                                [
                                    ['R', (self.GREY100, 0, 0, _SIZE[0], 105)],
                                    ['R', (self.GREY150, 0, 0, _SIZE[0], 100)],
                                    ['T', ("OPTIONS", 20, -10, 'impact', 100, self.WHITE)],
                                    ['T', ("This page is under construction.", 210, _SIZE[1]/2 - 50, 'impact', 30, self.GREY150)]
                                ]),
                        UI_Gameplay(pygame, 4, self.GREY175,
                                    [
                                        (5, 5, 50, 20, 1, self.GREY150, self.GREY100, "EXIT", "impact", 15, self.WHITE)
                                    ],
                                    [
                                        ['R', (self.GREY75, 0, _SIZE[1] - 55, _SIZE[0], 55)],
                                        ['R', (self.GREY100, 0, _SIZE[1] - 50, _SIZE[0], 50)],

                                        ['R', (self.GREY75, 75, _SIZE[1] - 75, 225, 75)],
                                        ['R', (self.GREY150, 75, _SIZE[1] - 70, 220, 70)],
                                        ['C', (self.GREY75, (75, _SIZE[1] - 75), 75)],
                                        ['C', (self.GREY150, (75, _SIZE[1] - 75), 72)],
                                        ['C', (self.RED, (75, _SIZE[1] - 75), 60)],
                                        ['C', (self.GREY150, (75, _SIZE[1] - 75), 55)],

                                        ['R', (self.GREY75, _SIZE[0] - 75, _SIZE[1] - 75, -225, 75)],
                                        ['R', (self.GREY150, _SIZE[0] - 75, _SIZE[1] - 70, -220, 70)],
                                        ['C', (self.GREY75, (_SIZE[0] - 75, _SIZE[1] - 75), 75)],
                                        ['C', (self.GREY150, (_SIZE[0] - 75, _SIZE[1] - 75), 72)],
                                        ['C', (self.BLUE, (_SIZE[0] - 75, _SIZE[1] - 75), 60)],
                                        ['C', (self.GREY150, (_SIZE[0] - 75, _SIZE[1] - 75), 55)]
                                    ],
                                    _SIZE[0], _SIZE[1]),
                        UI_SplashScreen(pygame, 5, 1, self.GREY150,
                                        [
                                    ['T', ("Player 1 wins!", 225, _SIZE[1]/2 - 100, 'impact', 70, self.WHITE)],
                                    ['T', ("(Click anywhere to continue)", 285, _SIZE[1]/2 + 50, 'impact', 20, self.WHITE)],
                                ]),
                        UI_SplashScreen(pygame, 6, 1, self.GREY150,
                                        [
                                    ['T', ("Player 2 wins!", 225, _SIZE[1]/2 - 100, 'impact', 70, self.WHITE)],
                                    ['T', ("(Click anywhere to continue)", 285, _SIZE[1]/2 + 50, 'impact', 20, self.WHITE)],
                                ])
                    ]

        self.currentMenu = 0
        self.gameplayUI = 4
        self.mouse = (0, 0)

        self.matchStarted = False
        self.gameOver = False, -1
        self.endGameCount = 0

    def run(self) :
        '''
        Run the game environment loop.
        :return: None
        '''

        while True:
            if self.events.handleEvents(self) :

                # Update objects
                self.mouse = self.events.getMouse()

                if self.gameOver[0] :
                    self.endGameCount += 1
                    if self.endGameCount > 100 :
                        self.setGameOver(self.gameOver[1])
                        self.gameOver = False, -1


                if self.currentMenu == self.gameplayUI :
                    self.menus[self.currentMenu].update(self)
                    self.gameManager.update(self)

                # Refresh window
                self.window.refresh(self.menus[self.currentMenu].getBG())

                # Draw objects
                if self.currentMenu == self.gameplayUI :
                    self.window.draw(self.gameManager)

                self.window.draw(self.menus[self.currentMenu])

                # Flip window
                self.window.flip()
            else :
                break

        self.window.quit()
        return

    def doKeyDown(self, key) :
        '''
        Process a key being pressed.
        :param key: event.key
        :return: None
        '''
        self.menus[self.currentMenu].doKeyDown(self, key)
        if self.currentMenu == self.gameplayUI :
            self.gameManager.doKeyDown(key)

    def doKeyUp(self, key) :
        '''
        Process a key being released.
        :param key: event.key
        :return: None
        '''
        self.menus[self.currentMenu].doKeyUp(self, key)
        if self.currentMenu == self.gameplayUI :
            self.gameManager.doKeyUp(key)

    def doMouseDown(self, mouse) :
        '''
        Process a mouse button being pressed.
        :param mouse: pygame.mouse.get_pressed()
        :return: None
        '''
        self.menus[self.currentMenu].doMouseDown(self, mouse, self.mouse)

    def doMouseUp(self, mouse) :
        '''
        Process a mouse button being released.
        :param mouse: pygame.mouse.get_pressed()
        :return: None
        '''
        self.menus[self.currentMenu].doMouseUp(self, mouse, self.mouse)

    def setMenu(self, menuID) :
        '''
        Set the current menu.
        :param menuID: Menu ID.
        :return: None
        '''
        if menuID == self.gameplayUI :
            self.gameManager = GameManager(pygame, self.window.getSize(), self.GREY150, self.GREY100, self.RED, self.BLUE)
            self.menus[self.gameplayUI].resetCountDown()
            self.matchStarted = False
            self.gameOver = False, -1
            self.endGameCount = 0
        self.currentMenu = menuID

    def getPlayerDamage(self, p) :
        '''
        Get a player's damage.
        :param p: Player number (1/2)
        :return: (Int) player damage.
        '''
        return self.gameManager.getPlayerDamage(p)

    def declareGameOver(self, winner) :
        '''
        Declare the end of the game.
        :param winner: The winner of the game.
        :return: None
        '''
        self.gameOver = True, winner

    def setGameOver(self, winner) :
        '''
        End the game.
        :param winner: The winner of the game.
        :return: None
        '''
        if winner == 1 :
            self.currentMenu = 5
        elif winner == 2:
            self.currentMenu = 6

    def startMatch(self) :
        '''
        Tell the game manager to start the match.
        :return: None
        '''
        if not self.matchStarted :
            self.matchStarted = True
            self.gameManager.startMatch()

class Screen :

    def __init__(self, _SIZE, _CAPTION) :
        '''
        :param _SIZE: Size of screen.
        :param _CAPTION: Caption of the window.
        :return: None
        '''

        self.screen = pygame.display.set_mode(_SIZE)
        pygame.display.set_caption(_CAPTION)
        self.SIZE = _SIZE
        self.CAPTION = _CAPTION

    def refresh(self, col) :
        '''
        Clear the pygame screen and all surfaces.
        :param col: Background colour.
        :return: None
        '''
        self.screen.fill(col)

    def flip(self) :
        '''
        Blit surfaces, and flip the pygame screen.
        :return: None
        '''
        pygame.display.flip()
        pygame.time.delay(20)

    def draw(self, _obj) :
        '''
        Draw an object to the opaque screen.
        :param _obj: Any object.
        :return: None
        '''
        _obj.draw(self.screen, pygame)

    def quit(self) :
        '''
        Quit pygame window.
        :return: None
        '''
        pygame.quit()

    def getWidth(self) :
        return self.SIZE[0]

    def getHeight(self) :
        return self.SIZE[1]

    def getSize(self) :
        return self.SIZE



class EventHandler :

    def __init__(self) :
        '''
        Initialize the event handler.
        :return: None
        '''

    def handleEvents(self, env) :
        '''
        Handle the events received by pygame.
        :param env: Logic class instance.
        :return: Boolean -> True: continue application; False: exit application.
        '''

        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                return False
            elif event.type == pygame.KEYDOWN :
                env.doKeyDown(event.key)
            elif event.type == pygame.KEYUP :
                env.doKeyUp(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN :
                env.doMouseDown(pygame.mouse.get_pressed())
            elif event.type == pygame.MOUSEBUTTONUP :
                env.doMouseUp(pygame.mouse.get_pressed())

        return True

    def getMouse(self) :
        '''
        Get the mouse position on the screen.
        :return: (TUPLE) = (mouseX,mouseY)
        '''
        return pygame.mouse.get_pos()



class AudioManager :

    def __init__(self) :
        '''
        Manages pygame audio channels and sounds.
        :return: None
        '''
        pygame.mixer.init()
        self.numChannels = 8
        pygame.mixer.set_num_channels(self.numChannels)

        self.resChannels = {    "mus" : pygame.mixer.Channel(0)    }

        self.musicVolume = [100, 100]
        self.sfxVolume = [100, 100]
        self.fadeRate = 1

        self.songs = [  pygame.mixer.Sound("data/hotpursuit.wav"),
                        pygame.mixer.Sound("data/adventuretime.wav")    ]

    def update(self) :
        '''
        Update the audio object.
        :return: None
        '''
        self.adjustVolume(self.musicVolume)
        self.adjustVolume(self.sfxVolume)

    def setFadeRate(self, r) :
        '''
        Set the fade rate.
        :param r: New fade rate.
        :return: None
        '''
        self.fadeRate = r

    def setMusicVolume(self, v) :
        '''
        Set the volume of music (0-100).
        :param v: New volume.
        :return: None
        '''
        self.musicVolume[0] = v

    def setSFXVolume(self, v) :
        '''
        Set the volume of SFX (0-100).
        :param v: New volume.
        :return: None
        '''
        self.sfxVolume[0] = v

    def adjustVolume(self, v) :
        '''
        Adjusts the inputted volume level.
        :param v: Inputted volume variable.
        :return: None
        '''
        if v[0] < v[1] :
            v += self.fadeRate
        elif v[0] > v[1] :
            v -= self.fadeRate






