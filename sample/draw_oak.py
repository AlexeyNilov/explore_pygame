import pygame
from pygame.locals import Color
import sys
import time

from model.creature import Oak, Pig
from model.wall import Wall


pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

text_color = Color('black')
font = pygame.font.SysFont("Verdana", 40)
message = font.render("Wall!", True, text_color)

background_color = Color('grey')
oak = Oak()
pig = Pig()

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
    pig.move()

    if pygame.sprite.spritecollideany(pig, walls):
        pig.speed *= -1
        screen.blit(message, (400, 300))
        pygame.display.update()
        time.sleep(0.5)

    screen.fill(background_color)  # Fill the display with a solid color

    # Render the graphics here.
    # ...
    oak.draw(screen)
    pig.draw(screen)

    for wall in walls:
        wall.draw(screen)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
