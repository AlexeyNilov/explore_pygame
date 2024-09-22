import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, x: int = 0, y: int = 0):
        super().__init__()
        self.image = pygame.image.load('image/wall.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
