import pygame
pygame.mouse.set_visible(False)

CURSORIMGS = pygame.image.load("assets/Cursors.png")

CURSORS = {
    "Normal": (CURSORIMGS.subsurface((0, 0, 16, 16)), (0, 0))
}

class Mouse:
    MOUSETYPE = "Normal"

    @classmethod
    def changeMouseType(cls, new_type):
        cls.MOUSETYPE = new_type
    
    @classmethod
    def update(cls, win):
        if pygame.mouse.get_focused():
            mp = pygame.mouse.get_pos()
            win.blit(CURSORS[cls.MOUSETYPE][0], (mp[0]-CURSORS[cls.MOUSETYPE][1][0], mp[1]-CURSORS[cls.MOUSETYPE][1][1]))
