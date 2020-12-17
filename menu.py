import pygame
import trex_game
import space_invaders_game
import os

# Initialize the menu
pygame.init()

# Creating screen
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Path
sourceFileDir = os.path.dirname(os.path.abspath(__file__))

# Draw text in the menu
menu_text = pygame.font.Font(os.path.join(sourceFileDir, 'Font', '8-BIT WONDER.TTF'), 32)


def draw_play(x, y):
    play_text = menu_text.render("PLAY", True, (255, 255, 255))
    screen.blit(play_text, (int(x), int(y)))


def draw_text(x, y):
    over_text = menu_text.render("MAIN MENU", True, (255, 255, 255))
    screen.blit(over_text, (int(x), int(y)))


# Main loop

menu_on = True

while menu_on:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_on = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                space_invaders_game.space_invaders_game()
            if event.key == pygame.K_LEFT:
                trex_game.trex_game()
            # Just press 'Esc' to quit the game
            if event.key == pygame.K_ESCAPE:
                exit()

    draw_text(250, 100)
    draw_play(320, 150)

    pygame.display.update()
