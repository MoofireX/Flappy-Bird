import pygame
import random
import time

og_tower1_x = 30
og_tower1_y = -300

og_tower2_x = 100
og_tower2_y = 450

og_tower3_x = 200
og_tower3_y = 300

og_flappy_x = 10
og_flappy_y = 250

running = False

def setup():
    global running
    global screen
    global bg
    global gameover
    global clock
    global score 
    global font

    pygame.init()
    font = pygame.font.Font(None, 30)
    screen = pygame.display.set_mode((285, 500))
    pygame.display.set_caption("Flappy Bird")
    bg = pygame.image.load("./Assets/background-day.png") 
    gameover = pygame.image.load("./Assets/gameover.png")
    screen.blit(bg, (0,0))
    clock = pygame.time.Clock()
    score = 0
    running = True

setup()

class Towers(pygame.sprite.Sprite):
    def __init__(self, image, scale, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.tower = pygame.image.load(image).convert_alpha()
        w = int(self.tower.get_width() * scale)
        h = int(self.tower.get_height() * scale * 3)

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
        self.collision.y += 1
        self.rect.y += 1

    def up(self):
        self.collision.y -= 10
        self.rect.y -= 10
        time.sleep(0.01)

def objects(pillar1x=og_tower1_x, pillar2x=og_tower2_x, pillar3x=og_tower3_x):
    global og_flappy_x, og_flappy_y, og_tower1_x, og_tower1_y, og_tower2_x, og_tower2_y, og_tower3_x, og_tower3_y

    player = pygame.sprite.Group()
    bird = Flappy("./Assets/bluebird-midflap.png", 1, og_flappy_x, og_flappy_y)
    player.add(bird)

    pillars = pygame.sprite.Group()
    pillar1 = Towers("./Assets/pipe-green.png", .5, pillar1x, og_tower1_y)
    pillar2 = Towers("./Assets/pipe-green.png", 1, pillar2x, og_tower2_y)
    pillar3 = Towers("./Assets/pipe-green.png", .5, pillar3x, og_tower3_y)
    pillars.add(pillar1, pillar2, pillar3)

    return bird, player, pillars

def main():
    global score
    global running
    global screen
    global bg
    global clock
    global font

    bird, player, pillars = objects()

    while running:
        front = pygame.Rect(bird.collision.right, bird.collision.top, 1, bird.collision.height)
        bottom = pygame.Rect(bird.collision.left, bird.collision.bottom, 1, bird.collision.width)
        top = pygame.Rect(bird.collision.left, bird.collision.top, 1, bird.collision.width)

        x1, x2, x3 = random.randint(0, 480), random.randint(0, 480), random.randint(0, 480)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                score += 2
                bird.up()
                
        bird.update()
        player.draw(screen)
        pillars.draw(screen)

        if bird.collision.x >= 285:
            screen.blit(bg, (0,0))
            bird, player, pillars = objects(x1, x2, x3)
            pillars.draw(screen)

        if bird.collision.y >= 500:
            screen.blit(gameover, (40,250))
            time.sleep(2)
            running = False

        for pillar in pillars:
            if front.colliderect(pillar.rect) or bottom.colliderect(pillar.rect) or top.colliderect(pillar.rect):
                screen.blit(gameover, (40,250))
                time.sleep(2)
                running = False

        score_display = font.render(f"Score: {score}", True, (0,0,0))
        pygame.display.flip()
        screen.blit(bg, (0,0))
        screen.blit(score_display, (110, 30))
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()