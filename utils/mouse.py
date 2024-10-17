from utils.scaling import Scaler
import pygame
pygame.mouse.set_visible(False)

CURSORIMGS = pygame.image.load("assets/Cursors.png")

CURSORS = {
    "Normal": (CURSORIMGS.subsurface((0, 0, 16, 16)), (1, 1)),
    "Click": (CURSORIMGS.subsurface((16, 0, 16, 16)), (6, 1)),
    "Text": (CURSORIMGS.subsurface((0, 16, 16, 16)), (8, 8)),
    "Clicking": (CURSORIMGS.subsurface((16, 16, 16, 16)), (6, 1)),
}

class Mouse:
    MOUSETYPE = "Normal"

    @classmethod
    def MousePos(cls):
        return Scaler.scalePos(pygame.mouse.get_pos())

    @classmethod
    def changeMouseType(cls, new_type):
        cls.MOUSETYPE = new_type
    
    @classmethod
    def update(cls, win):
        if pygame.mouse.get_focused():
            mp = cls.MousePos()
            win.blit(CURSORS[cls.MOUSETYPE][0], (mp[0]-CURSORS[cls.MOUSETYPE][1][0], mp[1]-CURSORS[cls.MOUSETYPE][1][1]))
