import pygame


class Sprite(pygame.sprite.Sprite):
    def __init__(self, images):
        super(Sprite, self).__init__()
        self.images = images
        self.index = 0
        self.ref_image = self.images[self.index]
        self.ref_rect = self.ref_image.get_rect()
        self.image = self.ref_image
        self.rect = self.ref_rect
        self.factor = 1

    def update(self, *args):
        self.resize()

    def next_frame(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def resize(self):
        dim = (self.ref_rect.w * self.factor, self.ref_rect.h * self.factor)
        self.image = pygame.transform.scale(self.image, dim)
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, self.rect)