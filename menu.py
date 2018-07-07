import pygame


class BackDrop:
    def __init__(self):
        self.rect = pygame.Rect(200, 0, 200, 200)
        self.surface = pygame.Surface(self.rect.size)
        self.surface.fill((128, 128, 128))

    def draw(self, surface, sprite):
        sprite.rect.center = self.rect.w/2, self.rect.h/2
        self.surface.blit(sprite.image, sprite.rect)
        surface.blit(self.surface, self.rect)


class Button:
    def __init__(self):
        self.pressed = False
        self.color = (0, 255, 0)
        self.rect = pygame.Rect(5, 405, 100, 20)

    def render(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

