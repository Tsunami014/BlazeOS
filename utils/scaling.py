import pygame

class Scaler:
    SCALE = [1, 1]
    OFFSET = [0, 0]

    @staticmethod
    def winSze():
        return pygame.display.get_surface().get_size()
    
    @classmethod
    def scalePos(cls, pos):
        return (pos[0] - cls.OFFSET[0]) // cls.SCALE[0], (pos[1] - cls.OFFSET[1]) // cls.SCALE[1]

    @classmethod
    def scale(cls, surf):
        sze = cls.winSze()
        newSze = min(sze)

        cls.SCALE = newSze / surf.get_width(), newSze / surf.get_height()

        leftOverAmnt = max(sze)-newSze
        if sze[0] >= sze[1]:
            leftOver = [leftOverAmnt, 0]
        else:
            leftOver = [0, leftOverAmnt]
        return pygame.transform.scale(surf, (newSze, newSze)), leftOver
