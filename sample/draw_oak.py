import pygame
from pygame.locals import Color
import sys

from model.creature import Oak


pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

background_color = Color('grey')
oak = Oak()

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Do logical updates here.
    # ...

    screen.fill(background_color)  # Fill the display with a solid color

    # Render the graphics here.
    # ...
    oak.draw(screen)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
