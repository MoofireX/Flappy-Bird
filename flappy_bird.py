import pygame
import random
import time

og_tower1_x = 100
og_tower1_y = 720

og_tower2_x = 500
og_tower2_y = 720

og_tower3_x = 1000
og_tower3_y = 720

og_flappy_x = 450
og_flappy_y = 360

score = 0
running = False

def setup():
    global running
    global screen
    global bg
    global clock 

    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Flappy Bird")
    bg = pygame.image.load("./Assets/background-day.png") 
    screen.blit(bg, (0,0))
    clock = pygame.time.Clock()
    running = True

setup()

class Towers(pygame.sprite.Sprite):
    def __init__(self, image, scale, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.tower = pygame.image.load(image).convert_alpha()
        w = int(self.tower.get_width() * scale)
        h = int(self.tower.get_height() * scale)

        self.image = pygame.transform.scale(self.tower, (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.collision = self.rect.copy()
        self.collision.x = self.rect.x
        self.collision.y = self.rect.y

class Flappy(pygame.sprite.Sprite):    
    def __init__(self, image, scale, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.flappy = pygame.image.load(image).convert_alpha()
        w = int(self.flappy.get_width() * scale)
        h = int(self.flappy.get_height() * scale)

        self.image = pygame.transform.scale(self.flappy, (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.collision = self.rect.copy()
        self.collision.x = self.rect.x
        self.collision.y = self.rect.y

    def update(self):
        self.collision.x += 1
        self.rect.x +=1
        self.collision.y += 5
        self.rect.y += 5

    def up(self):
        self.collision.y -= 10
        self.rect.y -= 10
        time.sleep(0.01)

def objects(pillar1x=og_tower1_x, pillar2x=og_tower2_x, pillar3x=og_tower3_x):
    global og_flappy_x, og_flappy_y, og_tower1_x, og_tower1_y, og_tower2_x, og_tower2_y, og_tower3_x, og_tower3_y

    player = pygame.sprite.Group()
    bird = Flappy("./Assets/bluebird-midflap.png", 3, og_flappy_x, og_flappy_y)
    player.add(bird)

    pillars = pygame.sprite.Group()
    pillar1 = Towers("./Assets/pipe-green.png", 1, pillar1x, og_tower1_y)
    pillar2 = Towers("./Assets/pipe-green.png", 1, pillar2x, og_tower2_y)
    pillar3 = Towers("./Assets/pipe-green.png", 1, pillar3x, og_tower3_y)
    pillars.add(pillar1, pillar2, pillar3)

    return bird, player, pillars

def main():
    global score
    global running
    global screen
    global bg
    global clock

    bird, player, pillars = objects()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                bird.up()
                
        bird.update()
        player.draw(screen)
        if bird.collision.x >= 1250:
            pillars.draw(screen)

        if bird.collision.y >= 720:
            break

        pygame.display.flip()
        screen.blit(bg, (0,0))
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()