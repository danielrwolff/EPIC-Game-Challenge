# gui.py
# Daniel Wolff
# 01/02/2016

from tools import Button, Text

class UserInterface :

    def __init__(self, pygame, menuID, bg, buttons, decor) :
        '''
        Initialize UI object.
        :param pygame: PyGame instance.
        :param menuID: (Int) UI ID.
        :param bg: Background colour.
        :param buttons: List of button data (NOT button objects).
        :param decor: List of decoration data.
        :return: None
        '''

        self.id = menuID
        self.bg = bg
        self.buttons = []
        for i in buttons :
            self.buttons.append(Button(pygame, i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]))

        self.decor = []
        for i in decor :
            if i[0] == 'I' :
                self.decor.append((i[1], i[2]))
            elif i[0] == 'T' :
                self.decor.append(Text(pygame, i[1][0],i[1][1],i[1][2],i[1][3],i[1][4],i[1][5]))
            elif i[0] == 'R' or i[0] == 'C' :
                self.decor.append(i)




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
        for i in self.decor :
            if isinstance(i, Text) :
                i.draw(screen, pygame)
            elif isinstance(i[0], pygame.Surface) :
                screen.blit(i[0], i[1])
            else :
                if i[0] == 'R' :
                    pygame.draw.rect(screen, i[1][0], (i[1][1],i[1][2],i[1][3],i[1][4]))
                elif i[0] == 'C' :
                    pygame.draw.circle(screen, i[1][0], i[1][1], i[1][2])

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

    def doMouseUp(self, env, mouse, pos) :
        '''
        Process a mouse button release.
        :param env: logic instance.
        :param mouse: pygame.mouse.get_pressed()
        :param pos: (Tuple) -> mouse (x,y)
        :return: None
        '''

    def getBG(self) :
        return self.bg



class UI_Gameplay (UserInterface) :

    def __init__(self, pygame, menuID, bg, buttons, decor) :
        '''
        Initialize UI object.
        :param pygame: PyGame instance.
        :param menuID: (Int) UI ID.
        :param bg: Background colour.
        :param buttons: List of button data (NOT button objects).
        :param decor: List of decoration data.
        :return: None
        '''
        UserInterface.__init__(self, pygame, menuID, bg, buttons, decor)


class UI_Menu (UserInterface) :

    def __init__(self, pygame, menuID, bg, buttons, decor) :
        '''
        Initialize UI object.
        :param pygame: PyGame instance.
        :param menuID: (Int) UI ID.
        :param bg: Background colour.
        :param buttons: List of button data (NOT button objects).
        :param decor: List of decoration data.
        :return: None
        '''
        UserInterface.__init__(self, pygame, menuID, bg, buttons, decor)

    def doMouseUp(self, env, mouse, pos) :
        '''
        Process a mouse button release.
        :param env: logic instance.
        :param mouse: pygame.mouse.get_pressed()
        :param pos: (Tuple) -> mouse (x,y)
        :return: None
        '''
        for button in self.buttons :
            if button.isClicked(pos[0], pos[1]) :
                env.setMenu(button.getTargetID())
                return



class UI_SplashScreen(UserInterface) :

    def __init__(self, pygame, menuID, targetID, bg, decor) :
        '''
        Initialize UI object.
        :param pygame: PyGame instance.
        :param menuID: (Int) UI ID.
        :param bg: Background colour.
        :param targetID: Target menu ID.
        :param decor: List of decoration data.
        :return: None
        '''
        UserInterface.__init__(self, pygame, menuID, bg, [], decor)
        self.targetID = targetID


    def doMouseUp(self, env, mouse, pos) :
        '''
        Process a mouse button release.
        :param env: logic instance.
        :param mouse: pygame.mouse.get_pressed()
        :param pos: (Tuple) -> mouse (x,y)
        :return: None
        '''
        if mouse[1] == 1 :
            return
        env.setMenu(self.targetID)
