import pygame

from utils.fonts import Font
from utils.mouse import Mouse
from utils import COLOURS

IconImg = pygame.image.load('assets/Bar.png')
ICONS = {
    "NoVolume": IconImg.subsurface((0, 0, 8, 8)),
    "YesVolume": IconImg.subsurface((8, 0, 8, 8)),
    "Settings": IconImg.subsurface((16, 0, 8, 8)),
    "Page": IconImg.subsurface((16+8, 0, 8, 8)),
    "Menu": IconImg.subsurface((0, 8, 16, 8)),
    "MenuPress": IconImg.subsurface((16, 8, 16, 8)),
}

MenuFont = Font('Small')

class Bar:
    MenuOpen = False

    @classmethod
    def draw(cls, win):
        selected = pygame.Rect(0, 0, 16, 8).collidepoint(Mouse.WinMousePos())
        if selected:
            if Mouse.PRESSTYP > 0:
                Mouse.changeMouseType("Clicking")
                selected = False
            else:
                Mouse.changeMouseType("Click")
        
        if cls.MenuOpen:
            menuW = 40
            Xpadding = 3
            Ypadding = 2
            def Hrule():
                s = pygame.Surface((menuW-Xpadding*2, 3), pygame.SRCALPHA)
                s.fill(COLOURS['Inner'], (0, 2, menuW-Xpadding*2, 1))
                return s
            
            defaultSelectAction = lambda: print("You selected an option!")
            menuElms = {
                MenuFont.render('Enabled', COLOURS['Outer']): defaultSelectAction,
                Hrule(): None,
                MenuFont.render('Disabled1', COLOURS['Disabled']): None,
                MenuFont.render('Disabled2', COLOURS['Disabled']): None,
                Hrule(): None,
                MenuFont.render('Enabled', COLOURS['Outer']): defaultSelectAction,
                MenuFont.render(':D :D :D', COLOURS['Outer']): defaultSelectAction,
            }
            menuSze = (menuW, sum([i.get_height()+Ypadding for i in menuElms]))
            pygame.draw.rect(win, COLOURS['Menu'], (0, 7, menuSze[0]+4, menuSze[1]+4), border_radius=2)
            pygame.draw.rect(win, COLOURS['Outer'], (0, 7, menuSze[0]+4, menuSze[1]+4), 2, 2)
            win.set_at((2, 9), COLOURS['Outer'])
            win.set_at((2, 8+menuSze[1]), COLOURS['Outer'])
            win.set_at((1+menuSze[0], 8+menuSze[1]), COLOURS['Outer'])
            win.set_at((1+menuSze[0], 9), COLOURS['Outer'])

            y = 9
            for e, func in menuElms.items():
                h = e.get_height()
                if func is not None:
                    r = pygame.Rect(2, y, menuW, h + Ypadding)
                    if r.collidepoint(Mouse.WinMousePos()):
                        pygame.draw.rect(win, COLOURS['Selected'], r, border_radius=2)
                        if Mouse.PRESSTYP > 0:
                            Mouse.changeMouseType("Clicking")
                        elif Mouse.PRESSTYP == -1:
                            func()
                        else:
                            Mouse.changeMouseType("Click")
                win.blit(e, (2+Xpadding, y))
                y += h + Ypadding
        
        if Mouse.PRESSTYP == -1:
            if selected:
                cls.MenuOpen = not cls.MenuOpen
            elif cls.MenuOpen:
                cls.MenuOpen = False

        toDraw = [
            ICONS[['Menu', 'MenuPress'][cls.MenuOpen]],
            ICONS['Page'],
            MenuFont.render('Hello', (255, 255, 255))
        ]
        x = 0
        for d in toDraw:
            win.blit(d, (x, 0))
            x += d.get_width()
        

        toDraw = [
            ICONS['YesVolume'],
            MenuFont.render(' Time', (255, 255, 255)),
            # MenuFont.render(' Fri 16:03PM 2024', (255, 255, 255)),
        ]
        toDraw.reverse()
        x = 0
        for d in toDraw:
            x += d.get_width()
            win.blit(d, (win.get_width()-x, 0))
