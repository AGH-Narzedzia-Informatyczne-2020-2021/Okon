import pygame


class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 160, 40)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Flappy Bird"
        self.flappyx, self.flappyy = self.mid_w, self.mid_h + 25
        self.trexx, self.trexy = self.mid_w, self.mid_h + 55
        self.spacex, self.spacey = self.mid_w, self.mid_h + 85
        self.snakex, self.snakey = self.mid_w, self.mid_h + 115
        self.quitx, self.quity = self.mid_w, self.mid_h + 145
        self.gamex, self.gamey = self.mid_w, self.mid_h + 230
        self.cursor_rect.midtop = (self.flappyx + self.offset, self.flappyy)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Main Menu', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 - 40)
            self.game.draw_text("Flappy Bird", 25, self.flappyx, self.flappyy)
            self.game.draw_text("Trex", 25, self.trexx, self.trexy)
            self.game.draw_text("Space Invaders", 25, self.spacex, self.spacey)
            self.game.draw_text("Snake", 25, self.snakex, self.snakey)
            self.game.draw_text("QUIT", 25, self.quitx, self.quity)
            self.game.draw_text("ENJOY THE GAME", 40, self.gamex, self.gamey)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Flappy Bird':
                self.cursor_rect.midtop = (self.trexx + self.offset, self.trexy)
                self.state = 'Trex'
            elif self.state == 'Trex':
                self.cursor_rect.midtop = (self.spacex + self.offset, self.spacey)
                self.state = 'Space Invadors'
            elif self.state == 'Space Invadors':
                self.cursor_rect.midtop = (self.snakex + self.offset, self.snakey)
                self.state = 'Snake'
            elif self.state == 'Snake':
                self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
                self.state = 'Quit'
            elif self.state == 'Quit':
                self.cursor_rect.midtop = (self.flappyx + self.offset, self.flappyy)
                self.state = 'Flappy Bird'
        elif self.game.UP_KEY:
            if self.state == 'Flappy Bird':
                self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
                self.state = 'Quit'
            elif self.state == 'Trex':
                self.cursor_rect.midtop = (self.flappyx + self.offset, self.flappyy)
                self.state = 'Flappy Bird'
            elif self.state == 'Space Invaders':
                self.cursor_rect.midtop = (self.trexx + self.offset, self.trexy)
                self.state = 'Trex'
            elif self.state == 'Snake':
                self.cursor_rect.midtop = (self.spacex + self.offset, self.spacey)
                self.state = 'Space Invaders'
            elif self.state == 'Quit':
                self.cursor_rect.midtop = (self.snakex + self.offset, self.snakey)
                self.state = 'Snake'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Flappy Bird':
                self.game.playing = 1
            elif self.state == 'Trex':
                self.game.playing = 2
            elif self.state == 'Space Invaders':
                self.game.playing = 3
            elif self.state == 'Snake':
                self.game.playing = 4
            elif self.state == 'Quit':
                self.game.playing = 5
            self.run_display = False
