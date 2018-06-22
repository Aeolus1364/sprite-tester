import pygame
import sprite
import spritesheet


pygame.init()


class Main:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.fps = 5
        self.surface = pygame.display.set_mode((400, 400))
        self.running = True

        self.test = spritesheet.load("spritesheetrect.png", (16, 16))

        self.sprite = sprite.Sprite(self.test)
        self.sprite_group = pygame.sprite.Group(self.sprite)
        self.sprite.resize()

    def main_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONUP:
                    self.sprite.factor *= 2

            self.surface.fill((255, 255, 255))

            self.sprite_group.update()
            self.sprite_group.draw(self.surface)

            pygame.display.update()
            self.clock.tick(self.fps)

        pygame.quit()

    #
    # def menu_loop(self):

    def change_surface(self, dimensions):
        self.surface = pygame.display.set_mode(dimensions)


main = Main()
main.main_loop()