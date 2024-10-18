from utils.scaling import Scaler
import pygame
pygame.mouse.set_visible(False)

CURSORIMGS = pygame.image.load("assets/Cursors.png")

CURSORS = {
    "Normal": (CURSORIMGS.subsurface((0, 0, 16, 16)), (1, 2)),
    "Click": (CURSORIMGS.subsurface((16, 0, 16, 16)), (6, 2)),
    "Text": (CURSORIMGS.subsurface((0, 16, 16, 16)), (8, 8)),
    "Clicking": (CURSORIMGS.subsurface((16, 16, 16, 16)), (6, 2)),
}

class Mouse:
    MOUSETYPE = "Normal"

    @classmethod
    def WinMousePos(cls):
        return Scaler.scalePos(pygame.mouse.get_pos())

    @classmethod
    def ScrnMousePos(cls):
        p = Scaler.scalePos(pygame.mouse.get_pos())
        return (p[0]-1, p[1]-9)

    @classmethod
    def changeMouseType(cls, new_type):
        cls.MOUSETYPE = new_type
    
    @classmethod
    def update(cls, win):
        if pygame.mouse.get_focused():
            mp = cls.WinMousePos()
            win.blit(CURSORS[cls.MOUSETYPE][0], (mp[0]-CURSORS[cls.MOUSETYPE][1][0], mp[1]-CURSORS[cls.MOUSETYPE][1][1]))
