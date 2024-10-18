from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Hide the annoying pygame thing
import pygame
pygame.init()

from utils.mouse import Mouse
from utils.scaling import Scaler
from utils.fonts import Font
from utils.UI import UIBUTTONS
from utils import COLOURS

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
win = pygame.Surface((100, 100))
pygame.display.set_caption("BlazeOS")

f1 = Font('Large')
f2 = Font('Medium')
f3 = Font('Small')
btn = UIBUTTONS['OK'].copy()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False

    screen.fill(0)
    win.fill((255, 255, 255))

    Mouse.changeMouseType('Normal')

    btn.draw(win, 50, 50)

    y = 0
    for f in (f1, f2, f3):
        o = f.render('Hello!I am cool*:D', 6)
        win.blit(o, (0, y))
        y += o.get_height()

    Mouse.update(win)

    fullWin = pygame.Surface((win.get_width()+2, win.get_height()+2))
    pygame.draw.rect(fullWin, COLOURS['Outer'], (0, 0, 1, fullWin.get_height()), 1)
    pygame.draw.rect(fullWin, COLOURS['Outer'], (fullWin.get_width()-1, 0, 1, fullWin.get_height()), 1)
    pygame.draw.rect(fullWin, COLOURS['Outer'], (0, 0, fullWin.get_width(), 1), 1)
    pygame.draw.rect(fullWin, COLOURS['Outer'], (0, fullWin.get_height()-1, fullWin.get_width(), 1), 1)
    fullWin.blit(win, (1, 1))
    fullWin.set_at((1, 1), COLOURS['Outer'])
    fullWin.set_at((fullWin.get_width()-2, 1), COLOURS['Outer'])
    fullWin.set_at((fullWin.get_width()-2, fullWin.get_height()-2), COLOURS['Outer'])
    fullWin.set_at((1, fullWin.get_height()-2), COLOURS['Outer'])

    scaled, leftOver = Scaler.scale(fullWin)
    Scaler.OFFSET = [leftOver[0]//2, leftOver[1]//2]
    screen.blit(scaled, Scaler.OFFSET)

    pygame.display.flip()