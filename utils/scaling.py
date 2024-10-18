import pygame

class Scaler:
    SCALE = 1
    OFFSET = [0, 0]

    @staticmethod
    def winSze():
        return pygame.display.get_surface().get_size()
    
    @classmethod
    def scalePos(cls, pos):
        return (pos[0] - cls.OFFSET[0]) // cls.SCALE, (pos[1] - cls.OFFSET[1]) // cls.SCALE

    @classmethod
    def scale(cls, surf):
        sze = cls.winSze()
        scale = min(sze) / max(surf.get_size())
        cls.SCALE = scale
        newSze = min(sze)
        leftOverAmnt = max(sze)-newSze
        if sze[0] >= sze[1]:
            leftOver = [leftOverAmnt, 0]
        else:
            leftOver = [0, leftOverAmnt]
        return pygame.transform.scale(surf, (newSze, newSze)), leftOver
