# logic.py
# Daniel Wolff
# 10/21/2015

import pygame, random
from game import GameManager

class Logic :

    def __init__(self, _SIZE, _CAPTION) :
        '''
        Initialize the game environment.
        :param _SIZE: Size of window.
        :param _CAPTION: Caption of window.
        :return: None
        '''

        pygame.init()

        self.window = Screen(_SIZE, _CAPTION)
        self.events = EventHandler()

        self.gameManager = GameManager(pygame, _SIZE)
        self.audioManager = AudioManager()

        #self.audioManager.playRandomSong()

        self.mouse = (0, 0)

    def run(self) :
        '''
        Run the game environment loop.
        :return: None
        '''

        while True:
            if self.events.handleEvents(self) :

                # Update objects
                self.mouse = self.events.getMouse()
                self.gameManager.update()

                # Refresh window
                self.window.refresh()

                # Draw objects
                self.window.draw(self.gameManager)

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
        self.gameManager.doKeyDown(key)

    def doKeyUp(self, key) :
        '''
        Process a key being released.
        :param key: event.key
        :return: None
        '''
        self.gameManager.doKeyUp(key)

    def doMouseDown(self, mouse) :
        '''
        Process a mouse button being pressed.
        :param mouse: pygame.mouse.get_pressed()
        :return: None
        '''

    def doMouseUp(self) :
        '''
        Process a mouse button being released.
        :return: None
        '''



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

    def refresh(self) :
        '''
        Clear the pygame screen and all surfaces.
        :return: None
        '''
        self.screen.fill((230, 230, 230))

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
                env.doMouseUp()

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

    def playRandomSong(self) :
        '''
        Play a random song in the song list.
        :return: None
        '''
        self.resChannels["mus"].play(random.choice(self.songs))

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






