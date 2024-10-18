import pygame
from utils.mouse import Mouse

UISur = pygame.image.load("assets/UI.png")
WSSur = pygame.image.load("assets/Workspace.png")

class Button:
    def __init__(self, x, y):
        self.sur = UISur.subsurface((x*32, y*16, 32, 16))
        self.selectedSur = UISur.subsurface((x*32, y*16+32, 32, 16))
    
    def draw(self, win, x, y):
        selected = pygame.Rect(x, y, 32, 16).collidepoint(Mouse.ScrnMousePos())
        if selected:
            if Mouse.PRESSTYP > 0:
                Mouse.changeMouseType("Clicking")
                selected = False
            else:
                Mouse.changeMouseType("Click")
            if Mouse.PRESSTYP == -1:
                print("You clicked on the button!")
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

WSBtnNames = [
    "UpFolder",
    "Folder",
    "Bin",
    "BinFull",
    "Workspace",
    "Floppy",
    # Files
    "Ini",
    "Text",
    "Json",
    "PNG",
    "GIF",
    "Colour",
    "Sprite",
    "Settings",
    "Sound",
    "Music",
    "Fx",
    "Font",
    "Blocks"
]

class WorkspaceBtn:
    def __init__(self, name):
        self.name = name
        idx = WSBtnNames.index(name)
        self.sur = WSSur.subsurface((idx*32, 0, 32, 32))
        self.selectedSur = WSSur.subsurface((idx*32, 32, 32, 32))
        self.mask = pygame.mask.from_surface(self.selectedSur)
    
    def draw(self, win, x, y):
        mp = Mouse.ScrnMousePos()
        selected = pygame.Rect(x, y, 32, 32).collidepoint(mp)
        if selected:
            selected = bool(self.mask.get_at((mp[0]-x, mp[1]-y)))
        if selected:
            if Mouse.PRESSTYP > 0:
                Mouse.changeMouseType("Clicking")
                selected = False
            else:
                Mouse.changeMouseType("Click")
            if Mouse.PRESSTYP == -1:
                print("You clicked on the workspace button!")
        win.blit(self.selectedSur if selected else self.sur, (x, y))
    
    def copy(self):
        return Button(self.name)
