import pygame


def load(spritesheet, dim):
    sheet = pygame.image.load(spritesheet).convert()
    sheet_size = sheet.get_size()

    images = []

    for y in range(0, sheet_size[1], dim[1]):
        for x in range(0, sheet_size[0], dim[0]):
            surf = pygame.Surface(dim)
            surf.blit(sheet, (0, 0), pygame.Rect(x, y, dim[0], dim[1]))
            images.append(surf)

    return images




