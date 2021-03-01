import pygame as pg
from game1 import gameLoop

def main():
    screen = pg.display.set_mode((600, 400), pg.RESIZABLE)
    font = pg.font.Font(None, 80)
    font2 = pg.font.Font(None, 70)
    font3 = pg.font.Font(None, 55)
    clock = pg.time.Clock()

    fong_logo = pg.font.Font(None, 20)
    start_game_box = pg.Rect(100, 125, 400, 70)

    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    screen_serf = pg.image.load("lug.png")
    screen_rect = screen_serf.get_rect(bottomright=(600, 400))
    screen.blit(screen_serf, screen_rect)

    change_level_box = pg.Rect(100, 225, 400, 70)
    pg.display.set_caption('Игра Змейка')
    done = False
    name = font.render("Game Snake", True, yellow)
    screen.blit(name, (120, 25))
    logo = fong_logo.render("2021 © Natalya Nurieva and Inna Vakulenko", True, black)
    start_text = font2.render("Начать игру", True, 'lightskyblue3')
    change_text = font3.render("Изменить сложность", True, 'lightskyblue3')
    pg.draw.rect(screen, white, change_level_box)
    pg.draw.rect(screen, red, change_level_box, 2)
    pg.draw.rect(screen, white, start_game_box)
    pg.draw.rect(screen, red, start_game_box, 2)
    screen.blit(start_text, (155, 135))
    screen.blit(change_text, (105, 245))
    screen.blit(logo, (170, 350))
    pg.display.update()
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.K_ESCAPE:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                if start_game_box.collidepoint(event.pos):
                    gameLoop()
                elif change_level_box.collidepoint(event.pos):
                    print("меняется уровень сложности")
                    #изменить уровень сложности
    pg.display.flip()
    clock.tick(30)

if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
