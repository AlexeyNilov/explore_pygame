import pygame


class Oak(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('image/oak.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 400)
        self.speed = 1

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self):
        self.rect.move_ip(0, self.speed)
