import pygame
from pygame.locals import Color
import sys

from model.creature import Oak
from model.wall import Wall


pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

background_color = Color('grey')
oak = Oak()

walls = pygame.sprite.Group()
for x in range(0, 1400, 100):
    walls.add(Wall(x=x, y=0))

for x in range(0, 1400, 100):
    walls.add(Wall(x=x, y=720))

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Do logical updates here.
    # ...
    oak.move()

    if pygame.sprite.spritecollideany(oak, walls):
        oak.speed *= -1

    screen.fill(background_color)  # Fill the display with a solid color

    # Render the graphics here.
    # ...
    oak.draw(screen)
    for wall in walls:
        wall.draw(screen)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
