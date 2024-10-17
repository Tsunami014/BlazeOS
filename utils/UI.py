import pygame
from utils.mouse import Mouse

UI = pygame.image.load("assets/UI.png")

class Button:
    def __init__(self, x, y):
        self.sur = UI.subsurface((x*32, y*16, 32, 16))
        self.selectedSur = UI.subsurface((x*32, y*16+32, 32, 16))
    
    def draw(self, win, x, y):
        selected = pygame.Rect(x, y, 32, 16).collidepoint(Mouse.MousePos())
        if selected:
            if pygame.mouse.get_pressed()[0]:
                Mouse.changeMouseType("Clicking")
                selected = False
            else:
                Mouse.changeMouseType("Click")
        win.blit(self.selectedSur if selected else self.sur, (x, y))
    
    def copy(self):
        return Button(self.sur.get_offset()[0]/32, self.sur.get_offset()[1]/16)

UIBUTTONS = {
    "Yes": Button(0, 0),
    "No": Button(1, 0),
    "OK": Button(2, 0),
    "Cancel": Button(0, 1),
    "Save": Button(1, 1)
}