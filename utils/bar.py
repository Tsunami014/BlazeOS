import pygame

from utils.fonts import Font

IconImg = pygame.image.load('assets/Bar.png')
ICONS = {
    "NoVolume": IconImg.subsurface((0, 0, 8, 8)),
    "YesVolume": IconImg.subsurface((8, 0, 8, 8)),
    "Settings": IconImg.subsurface((16, 0, 8, 8)),
    "Page": IconImg.subsurface((16+8, 0, 8, 8)),
    "Menu": IconImg.subsurface((0, 8, 16, 8)),
}

MenuFont = Font('Small')

class Bar:
    @classmethod
    def draw(cls, win):
        toDraw = [
            ICONS['Menu'],
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
