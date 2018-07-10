import pygame
import sprite
import spritesheet
import menu


pygame.init()


class Main:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.sprite_fps = 1
        self.set_framerate(1)

        self.surface = pygame.display.set_mode((400, 430), pygame.RESIZABLE)
        self.running = True

        self.test = spritesheet.load("spritesheetflat.png", (16, 16))
        self.sprite = sprite.Sprite(self.test)

        self.backdrop = menu.BackDrop()

        self.main_loop()

    def main_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.USEREVENT:
                    self.sprite.next_frame()
                    self.sprite.factor += 1

                if event.type == pygame.VIDEORESIZE:
                    print(event.size)
                    self.surface = pygame.display.set_mode(event.size, pygame.RESIZABLE)

            self.sprite.update()
            self.surface.fill((255, 255, 255))

            self.backdrop.draw(self.surface, self.sprite)

            pygame.display.update()
            self.clock.tick(self.fps)

        pygame.quit()

    def set_framerate(self, fps):
        self.sprite_fps = fps
        pygame.time.set_timer(pygame.USEREVENT, int(1000/self.sprite_fps))

    def change_surface(self, dimensions):
        self.surface = pygame.display.set_mode(dimensions)


main = Main()
