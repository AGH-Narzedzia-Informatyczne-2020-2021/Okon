import pygame
import random
import math
from pygame import mixer
import os

bullet_state = "ready"

def space_invaders_game(main_game):
    # Initialize the pygame
    pygame.init()

    # creating screen
    screen = pygame.display.set_mode((800, 600))  # weight, height

    # Path
    sourceFileDir = os.path.dirname(os.path.abspath(__file__))

    # Background
    background = pygame.image.load(os.path.join(sourceFileDir, 'images', 'background.png'))

    # Background sound
    mixer.music.load(os.path.join(sourceFileDir, 'sounds', 'background.wav'))
    mixer.music.play(-1)

    # Caption and Icon
    pygame.display.set_caption("Space Invaders")
    icon = pygame.image.load(os.path.join(sourceFileDir, 'images', 'ufo.png'))
    pygame.display.set_icon(icon)

    # Player
    player_img = pygame.image.load(os.path.join(sourceFileDir, 'images', 'player.png'))
    playerX = 370
    playerY = 480  # make the player start in the centre
    playerX_change = 0

    # Enemy
    enemy_img = []
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_change = []
    num_of_enemies = 6

    for i in range(num_of_enemies):
        enemy_img.append(pygame.image.load(os.path.join(sourceFileDir, 'images', 'enemy.png')))
        enemyX.append(random.randint(0, 735))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(2)  # beginning value required
        enemyY_change.append(40)

    # Bullet
    # Ready - You can't see the bullet on the screen
    # Fire - The bullet is currently moving
    bullet_img = pygame.image.load(os.path.join(sourceFileDir, 'images', 'bullet.png'))
    bulletX = 0
    bulletY = 480
    # bulletX_change = 0
    bulletY_change = 4
    global bullet_state

    # Score

    score_value = 0
    font = pygame.font.Font(os.path.join(sourceFileDir, 'Font_space_invaders', 'game_over.ttf'), 64)

    textX = 10
    textY = 10

    # Game over

    over_font = pygame.font.Font(os.path.join(sourceFileDir, 'Font_space_invaders', 'game_over.ttf'), 128)

    def show_score(x, y):
        score = font.render("Score: " + str(score_value), True, (255, 255, 255))
        screen.blit(score, (x, y))

    def game_over_text():
        over_text = over_font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(over_text, (250, 250))

    def player(x, y):  # x,y is were currently is our space ship
        screen.blit(player_img, (x, y))  # blit=draw, it draws our player on the screen

    def enemy(x, y, i):
        screen.blit(enemy_img[i], (x, y))

    def fire_bullet(x, y):
        global bullet_state
        bullet_state = "fire"
        screen.blit(bullet_img, (x + 16, y + 10))  # +16 is required to shoot from the centre

    def is_collision(enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
        if distance < 27:
            return True
        else:
            return False

    # Game Loop
    running = True
    while running:

        # RGB - Red, Green, Blue max=255
        screen.fill((0, 0, 0))
        # background image
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            # we are checking whether any key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_game.playing = 0
                    break
                if event.key == pygame.K_LEFT:
                    playerX_change = -3
                if event.key == pygame.K_RIGHT:
                    playerX_change = 3
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":  # checks whether bullet is currently on the screen
                        bullet_Sound = mixer.Sound(os.path.join(sourceFileDir, 'sounds', 'laser.wav'))
                        bullet_Sound.play()
                        bulletX = playerX  # Get the current x coordinate of the spaceship
                        fire_bullet(bulletX, bulletY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        if main_game.playing == 0:
            mixer.music.stop()
            pygame.display.set_mode((800, 600))
            break

        # Player movement and boundaries
        playerX += playerX_change

        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        # Enemy movement
        for i in range(num_of_enemies):

            # Game over
            if enemyY[i] > 440:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 2
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -2
                enemyY[i] += enemyY_change[i]

            # Collision
            collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                explosion_Sound = mixer.Sound(os.path.join(sourceFileDir, 'sounds', 'explosion.wav'))
                explosion_Sound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 735)
                enemyY[i] = random.randint(50, 150)

            enemy(enemyX[i], enemyY[i], i)

        # Bullet movement
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        player(playerX, playerY)
        show_score(textX, textY)
        pygame.display.update()  # it is constantly updating our screen
