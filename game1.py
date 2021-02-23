import pygame


class Game:
    def __init__(self):
        self.screen_width = 720
        self.screen_height = 460
        self.red = pygame.Color('red')
        self.green = pygame.Color('green')
        self.black = pygame.Color('black')
        self.white = pygame.Color('white')
        self.brown = pygame.Color('brown')

        self.fps_controller = pygame.time.Clock()

        self.score = 0

        self.play_surface = pygame.display.set_mode((
            self.screen_width, self.screen_height))
        pygame.display.set_caption('Snake')