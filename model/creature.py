import pygame


class Oak(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('image/oak.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.rect = self.image.get_rect()
        self.rect.center = (800, 300)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Pig(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('image/pig.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        self.speed = 1

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self):
        self.rect.move_ip(0, self.speed)


class Wolf(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('image/wolf.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (500, 400)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
