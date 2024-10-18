from utils.scaling import Scaler
import pygame
pygame.mouse.set_visible(False)

CURSORIMGS = pygame.image.load("assets/Cursors.png")

CURSORS = {
    "Normal": (CURSORIMGS.subsurface((0, 0, 16, 16)), (1, 2)),
    "Click": (CURSORIMGS.subsurface((16, 0, 16, 16)), (6, 2)),
    "Text": (CURSORIMGS.subsurface((0, 16, 16, 16)), (8, 8)),
    "Clicking": (CURSORIMGS.subsurface((16, 16, 16, 16)), (6, 2)),
    "Loading": (pygame.image.load("assets/LoadingMouse.png"), (6, 7))
}

class Mouse:
    MOUSETYPE = "Normal"
    LoadingFrame = 0
    _LastLoaded = None
    LoadingSpeed = 50
    PRESSTYP = 0
    """The type of press

    - `-1` = just released
    - `0` = not pressed
    - `1` = pressed
    - `2` = just started pressing"""

    @classmethod
    def changePressType(cls, newPT):
        cls.PRESSTYP = newPT

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
            if cls._LastLoaded != cls.MOUSETYPE:
                cls._LastLoaded = cls.MOUSETYPE
                cls.LoadingFrame = 0
            mp = cls.WinMousePos()
            cur = CURSORS[cls.MOUSETYPE][0]
            if cls.MOUSETYPE == "Loading":
                cls.LoadingFrame += 1
                if cls.LoadingFrame >= cur.get_width()//16*cls.LoadingSpeed:
                    cls.LoadingFrame = 0
                cur = cur.subsurface((cls.LoadingFrame//cls.LoadingSpeed*16, 0, 16, 16))
            win.blit(cur, (mp[0]-CURSORS[cls.MOUSETYPE][1][0], mp[1]-CURSORS[cls.MOUSETYPE][1][1]))
