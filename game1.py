import sys

import pygame


class Game:
    def event(self, direction):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    direction = "RIGHT"
                elif event.key == pygame.K_LEFT or event.key == ord('a'):
                    direction = "LEFT"
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    direction = "UP"
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    direction = "DOWN"
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        return direction
