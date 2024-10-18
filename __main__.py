from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Hide the annoying pygame thing
import pygame
pygame.init()

from utils.bar import Bar
from utils.mouse import Mouse
from utils.scaling import Scaler
from utils.fonts import Font
from utils.UI import UIBUTTONS, WorkspaceBtn
from utils import COLOURS

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
win = pygame.Surface((100, 100))
pygame.display.set_caption("BlazeOS")

f1 = Font('Large')
f2 = Font('Medium')
f3 = Font('Small')
btn = UIBUTTONS['OK'].copy()
btn2 = WorkspaceBtn('Workspace')

run = True
while run:
    Mouse.changePressType(1 if pygame.mouse.get_pressed()[0] else 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            Mouse.changePressType(-1)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            Mouse.changePressType(2)

    screen.fill(0)
    win.fill(COLOURS['Inner'])

    Mouse.changeMouseType('Normal')

    btn.draw(win, 50, 50)
    btn2.draw(win, 50, 70)

    y = 0
    for f in (f1, f2, f3):
        o = f.render('Hello!I am cool*:D', COLOURS['Outer'], 6)
        win.blit(o, (0, y))
        y += o.get_height()

    fullWin = pygame.Surface((win.get_width()+2, win.get_height()+10))
    pygame.draw.rect(fullWin, COLOURS['Outer'], (0, 0, fullWin.get_width(), 9))
    pygame.draw.rect(fullWin, COLOURS['Outer'], (0, 0, fullWin.get_width(), fullWin.get_height()), 1)
    fullWin.blit(win, (1, 9))
    # fullWin.set_at((1, 9), COLOURS['Outer'])
    # fullWin.set_at((fullWin.get_width()-2, 9), COLOURS['Outer'])
    fullWin.set_at((fullWin.get_width()-2, fullWin.get_height()-2), COLOURS['Outer'])
    fullWin.set_at((1, fullWin.get_height()-2), COLOURS['Outer'])
    Bar.draw(fullWin)
    Mouse.update(fullWin)

    scaled, leftOver = Scaler.scale(fullWin)
    Scaler.OFFSET = [leftOver[0]//2, leftOver[1]//2]
    screen.blit(scaled, Scaler.OFFSET)

    pygame.display.flip()