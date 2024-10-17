from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Hide the annoying pygame thing
import pygame
pygame.init()

from utils.mouse import Mouse
from utils.UI import UIBUTTONS

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("BlazeOS")

mouse = Mouse()

btn = UIBUTTONS['OK'].copy()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False

    screen.fill((255, 255, 255))

    mouse.changeMouseType('Normal')

    btn.draw(screen, 400, 300)

    mouse.update(screen)

    pygame.display.flip()