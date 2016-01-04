# gui.py
# Daniel Wolff
# 01/02/2016

from tools import Button, Text

class UserInterface :

    def __init__(self, pygame, menuID, buttons) :
        '''
        Initialize UI object.
        :param pygame: PyGame instance.
        :param menuID: (Int) UI ID.
        :param buttons: List of button data (NOT button objects).
        :return: None
        '''

        self.id = menuID
        self.buttons = []
        for i in buttons :
            self.buttons.append(Button(pygame, i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]))


    def update(self) :
        '''
        Update the user interface.
        :return: None
        '''

    def draw(self, screen, pygame) :
        '''
        Draw the user interface.
        :param screen: Surface to draw to.
        :param pygame: Pygame instance.
        :return: None
        '''
        for i in self.buttons :
            i.draw(screen, pygame)

    def doKeyDown(self, env, key) :
        '''
        Process a key being pressed.
        :param env: logic instance.
        :param key: event.key
        :return: None
        '''

    def doKeyUp(self, env, key) :
        '''
        Process a key being released.
        :param env: logic instance.
        :param key: event.key
        :return: None
        '''

    def doMouseDown(self, env, mouse, pos) :
        '''
        Process a mouse button press.
        :param env: logic instance.
        :param mouse: pygame.mouse.get_pressed()
        :param pos: (Tuple) -> mouse (x,y)
        :return: None
        '''


    def doMouseUp(self, env) :
        '''
        Process a mouse button release.
        :param env: logic instance.
        :return: None
        '''


class UI_Gameplay (UserInterface) :

    def __init__(self, pygame, menuID, buttons) :
        '''
        Initialize UI object.
        :param pygame: PyGame instance.
        :param menuID: (Int) UI menu ID.
        :param buttons: List of button objects.
        :return: None
        '''
        UserInterface.__init__(self, pygame, menuID, buttons)


class UI_Menu (UserInterface) :

    def __init__(self, pygame, menuID, buttons) :
        '''
        Initialize UI object.
        :param pygame: PyGame instance.
        :param menuID: (Int) UI menu ID.
        :param buttons: List of button objects.
        :return: None
        '''
        UserInterface.__init__(self, pygame, menuID, buttons)


class UI_SplashScreen(UserInterface) :

    def __init__(self, pygame, menuID, targetID, splash) :
        '''
        Initialize UI object.
        :param pygame: PyGame instance.
        :param menuID: (Int) UI menu ID.
        :param targetID: Target menu ID.
        :param splash: Splash screen image.
        :return: None
        '''
        UserInterface.__init__(self, pygame, menuID, [])
        self.splashScreen = splash
        self.targetID = targetID

    def draw(self, screen, pygame) :
        '''
        Draw splash screen to a surface.
        :param screen: Surface to draw to.
        :param pygame: Pygame instance.
        :return: None
        '''
        screen.blit(self.splashScreen, (0,0))

    def doMouseDown(self, env, mouse, pos) :
        '''
        Process a mouse button press.
        :param env: logic instance.
        :param mouse: pygame.mouse.get_pressed()
        :param pos: (Tuple) -> mouse (x,y)
        :return: None
        '''
        env.setMenu(self.targetID)
