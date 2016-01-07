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
            self.buttons.append(Button(pygame, i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]))

        self.decor = []
        for i in decor :
            if i[0] == 'I' :
                self.decor.append((i[1], i[2]))
            elif i[0] == 'T' :
                self.decor.append(Text(pygame, i[1][0],i[1][1],i[1][2],i[1][3],i[1][4],i[1][5]))
            elif i[0] == 'R' or i[0] == 'C' :
                self.decor.append(i)




    def update(self, logic) :
        '''
        Update the user interface.
        :param logic : Logic instance.
        :return: None
        '''
        mx, my = logic.getMouse()
        for i in self.buttons :
            if i.isHovering(mx, my) :
                i.setHover(True)
            else :
                i.setHover(False)

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
        for button in self.buttons :
            if button.isHovering(pos[0], pos[1]) :
                env.setMenu(button.getTargetID())
                return

    def getBG(self) :
        return self.bg



class UI_Gameplay (UserInterface) :

    def __init__(self, pygame, menuID, bg, buttons, decor, screenWidth, screenHeight) :
        '''
        Initialize UI object.
        :param pygame: PyGame instance.
        :param menuID: (Int) UI ID.
        :param bg: Background colour.
        :param buttons: List of button data (NOT button objects).
        :param decor: List of decoration data.
        :param screenWidth: Screen width.
        :param screenHeight: Screen height.
        :return: None
        '''
        UserInterface.__init__(self, pygame, menuID, bg, buttons, decor)

        self.WHITE = (255,255,255)
        self.YELLOW = (255,255,0)
        self.ORANGE = (255,155,0)
        self.RED = (255,0,0)

        self.p1Damage = Text(pygame, "", 190, screenHeight - 50, 'impact', 30, self.WHITE)
        self.p2Damage = Text(pygame, "", screenWidth - 230, screenHeight - 50, 'impact', 30, self.WHITE)

        self.countDownCount = 0
        self.countDownTime = 100
        self.countDownText = [  Text(pygame, "GO", screenWidth/2 - 85, screenHeight/2 - 100, 'impact', 150, self.WHITE),
                                Text(pygame, "1", screenWidth/2 - 30, screenHeight/2 - 100, 'impact', 150, self.WHITE),
                                Text(pygame, "2", screenWidth/2 - 40, screenHeight/2 - 100, 'impact', 150, self.WHITE),
                                Text(pygame, "3", screenWidth/2 - 40, screenHeight/2 - 100, 'impact', 150, self.WHITE)
                                ]

    def update(self, logic):
        '''
        Update the user interface.
        :param logic : Logic instance.
        :return: None
        '''

        UserInterface.update(self, logic)

        if self.countDownCount > self.countDownTime :
            logic.startMatch()
        else :
            self.countDownCount += 1

        p1 = logic.getPlayerDamage(1)
        p2 = logic.getPlayerDamage(2)

        if p1 > 250 :
            self.p1Damage.setColour(self.RED)
        elif p1 > 175 :
            self.p1Damage.setColour(self.ORANGE)
        elif p1 > 100 :
            self.p1Damage.setColour(self.YELLOW)
        else :
            self.p1Damage.setColour(self.WHITE)

        if p2 > 250 :
            self.p2Damage.setColour(self.RED)
        elif p2 > 175 :
            self.p2Damage.setColour(self.ORANGE)
        elif p2 > 100 :
            self.p2Damage.setColour(self.YELLOW)
        else :
            self.p2Damage.setColour(self.WHITE)

        self.p1Damage.setText(str(p1) + "%")
        self.p2Damage.setText(str(p2) + "%")

    def draw(self, screen, pygame) :
        '''
        Draw the user interface.
        :param screen: Surface to draw to.
        :param pygame: Pygame instance.
        :return: None
        '''
        UserInterface.draw(self, screen, pygame)

        self.p1Damage.draw(screen, pygame)
        self.p2Damage.draw(screen, pygame)

        if self.countDownCount < self.countDownTime :
            if self.countDownCount >= 75 :
                self.countDownText[0].draw(screen, pygame)
            elif self.countDownCount >= 50 :
                self.countDownText[1].draw(screen, pygame)
            elif self.countDownCount >= 25 :
                self.countDownText[2].draw(screen, pygame)
            else :
                self.countDownText[3].draw(screen, pygame)

    def resetCountDown(self) :
        '''
        Reset the game count down.
        :return: None
        '''
        self.countDownCount = 0




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
