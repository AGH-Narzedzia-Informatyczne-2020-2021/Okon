import pygame
import os
from pygame.locals import *


def trex_game():
    pygame.init()
    vec = pygame.math.Vector2
    HEIGHT=480
    WIDTH=640
    czas=0
    ACC=0.5
    FRIC=-0.12
    GRAV=0.375
    FPS=60
    FramePerSec = pygame.time.Clock()
    displaysurface=pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game")
    sourceFileDir = os.path.dirname(os.path.abspath(__file__))
    TLO=pygame.image.load(os.path.join(sourceFileDir,'resources','tlo.png'))
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.surf = pygame.Surface((64, 64))
            self.surf.fill((128,230,30))
            self.image = pygame.image.load(os.path.join(sourceFileDir,'resources','trex.png'))
            self.rect = self.image.get_rect(center=(10,420))
            self.pos = vec((70,415))
            self.vel = vec((0,0))
            self.acc = vec((0,0))

        def move(self):
            self.acc = vec(0,0)
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_UP] and self.pos.y == 448:
                pygame.mixer.music.load(os.path.join(sourceFileDir,'resources','jump.wav'))
                pygame.mixer.music.play(0)
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
            if self.pos.y > 448:
                self.pos.y = 448
            self.rect.midbottom=self.pos


    class platform(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.surf = pygame.Surface((WIDTH,32))
            self.image = pygame.image.load(os.path.join(sourceFileDir,'resources','sand.png'))
            self.surf.fill((240,200,0))
            self.rect = self.image.get_rect(center=(WIDTH/2, HEIGHT - 16))

    class cactus(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.surf = pygame.Surface((64,64))
            self.image = pygame.image.load(os.path.join(sourceFileDir,'resources','cactus.png'))
            self.surf.fill((240,200,0))
            self.rect = self.image.get_rect(center=(WIDTH/2, HEIGHT - 32))



    PT1 = platform()
    C1 = cactus()
    C2 = cactus()
    C3 = cactus()
    P1 = Player()
    score_value=0
    score_temp=0
    testX = 10
    testY = 10
    font = pygame.font.Font('freesansbold.ttf', 32)
    def showScore(x, y):
        score = font.render("Score : " + str(score_value), True, (255, 255, 255))
        displaysurface.blit(score, (x, y))

    all_sprites = pygame.sprite.Group()
    all_sprites.add(P1)
    timevec=0
    timevec2=1052
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        timevec-=6
        timevec2-=6
        czas+=6
        if timevec <= -1052:
            timevec = 1052
        if timevec2 <= -1052:
            timevec2 = 1052
        if czas >= 586 and czas <= 618 and P1.pos.y>390:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        if czas >= 704:
            czas = czas-320
        displaysurface.blit(TLO, (timevec,0))
        displaysurface.blit(TLO, (timevec2,0))
        displaysurface.blit(PT1.image, (timevec,448))
        displaysurface.blit(PT1.image, (timevec2,448))
        displaysurface.blit(C1.image, (640-czas,390))
        displaysurface.blit(C2.image, (960-czas,390))
        displaysurface.blit(C2.image, (1280-czas,390))
        score_temp += 1
        if score_temp == 20:
            score_value += 1
            score_temp = 0
        for entity in all_sprites:
            displaysurface.blit(entity.image, entity.rect)
        showScore(testX,testY)
        pygame.display.update()
        FramePerSec.tick(FPS)
        P1.move()