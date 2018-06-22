import pygame


class Sprite(pygame.sprite.Sprite):
    def __init__(self, images):
        super(Sprite, self).__init__()
        self.images = images
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(5, 5, 64, 64)
        self.factor = 1

    def update(self, *args):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

        self.resize(self.factor)

    def resize(self, factor=1):
        size = self.image.get_size()
        dim = (size[0] * factor, size[1] * factor)
        self.image = pygame.transform.scale(self.image, dim)

