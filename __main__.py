from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Hide the annoying pygame thing
import pygame
pygame.init()

from utils.mouse import Mouse
from utils.scaling import Scaler
from utils.UI import UIBUTTONS

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
win = pygame.Surface((100, 100))
pygame.display.set_caption("BlazeOS")

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

    Mouse.update(win)

    scaled, leftOver = Scaler.scale(win)
    Scaler.OFFSET = [leftOver[0]//2, leftOver[1]//2]
    screen.blit(scaled, Scaler.OFFSET)

    pygame.display.flip()