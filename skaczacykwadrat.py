import pygame
from pygame.locals import *
pygame.init()
vec = pygame.math.Vector2
HEIGHT=450
WIDTH=400
ACC=0.5
FRIC=-0.12
GRAV=0.25
FPS=60
FramePerSec = pygame.time.Clock()
displaysurface=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect(center=(10,420))
        self.pos = vec((10,385))
        self.vel = vec((0,0))
        self.acc = vec((0,0))
    def move(self):
        self.acc = vec(0,0)
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
        if pressed_keys[K_UP] and self.pos.y == 385:
            self.vel.y = -8
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.vel.y += GRAV
        self.pos.x += self.vel.x + 0.5 * self.acc.x
        self.pos.y += self.vel.y + 0.5 * GRAV
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.y > 385:
            self.pos.y = 385
        self.rect.midbottom=self.pos
    
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH,20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center=(WIDTH/2, HEIGHT - 10))

PT1 = platform()
P1 = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    displaysurface.fill((0,0,0))
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
    pygame.display.update()
    FramePerSec.tick(FPS)
    P1.move()