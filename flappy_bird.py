import pygame
import random

def setup():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Flappy Bird")
    bg = pygame.image.load() #Add bg here
    clock = pygame.time.Clock()
    running = True


class towers(pygame.sprite.Sprite):
    super().__init__()

    self.tower = pygame.image.load() #Add here

def main():
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()