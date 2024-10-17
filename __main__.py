from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Hide the annoying pygame thing
import pygame
pygame.init()

from utils.mouse import Mouse

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("BlazeOS")

mouse = Mouse()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 255), (400, 300), 75)

    mouse.update(screen)

    pygame.display.flip()