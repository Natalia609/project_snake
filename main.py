import pygame as pg
from game1 import gameLoop, fast_speed, low_speed, midle_speed, snake, dragon

start_game_box = pg.Rect(100, 125, 400, 70)
screen = pg.display.set_mode((600, 400))
sett_box = pg.Rect(100, 225, 400, 70)
local_menu_box = pg.Rect(100, 315, 400, 70)
speed = pg.Rect(100, 215, 400, 70)
skin = pg.Rect(100, 115, 400, 70)
low = pg.Rect(100, 85, 400, 70)
middle = pg.Rect(100, 185, 400, 70)
fast = pg.Rect(100, 285, 400, 70)
snke = pg.Rect(100, 135, 400, 70)
drgon = pg.Rect(100, 255, 400, 70)

font = pg.font.Font(None, 80)
font2 = pg.font.Font(None, 70)
font3 = pg.font.Font(None, 55)
clock = pg.time.Clock()

snake()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)


def menu():

    fong_logo = pg.font.Font(None, 20)

    screen_serf = pg.image.load("lug.png")
    screen_rect = screen_serf.get_rect(bottomright=(600, 400))
    screen.blit(screen_serf, screen_rect)

    pg.display.set_caption('Игра Змейка')
    name = font.render("Game Snake", True, yellow)
    screen.blit(name, (120, 25))
    logo = fong_logo.render("2021 © Natalya Nurieva and Inna Vakulenko", True, black)
    start_text = font2.render("Начать игру", True, 'lightskyblue3')
    settings_text = font2.render("Настройки", True, "lightskyblue3")
    pg.draw.rect(screen, white, sett_box)
    pg.draw.rect(screen, red, sett_box, 2)
    pg.draw.rect(screen, white, start_game_box)
    pg.draw.rect(screen, red, start_game_box, 2)
    screen.blit(start_text, (155, 135))
    screen.blit(settings_text, (175, 235))
    screen.blit(logo, (170, 350))
    pg.display.update()


def settings():

    screen_serf = pg.image.load("lug.png")
    screen_rect = screen_serf.get_rect(bottomright=(600, 400))
    screen.blit(screen_serf, screen_rect)

    set_text = font2.render("Настройки", True, yellow)
    screen.blit(set_text, (167, 25))

    pg.draw.rect(screen, white, local_menu_box)
    pg.draw.rect(screen, red, local_menu_box, 2)
    menu_text = font3.render("Вернуться в меню", True, 'lightskyblue3')
    screen.blit(menu_text, (130, 335))

    pg.draw.rect(screen, white, speed)
    pg.draw.rect(screen, red, speed, 2)
    speed_text = font3.render("Изменить скорость", True, "lightskyblue3")
    screen.blit(speed_text, (120, 235))

    pg.draw.rect(screen, white, skin)
    pg.draw.rect(screen, red, skin, 2)
    skin_text = font3.render("Сменить скин", True, "lightskyblue3")
    screen.blit(skin_text, (170, 135))

    pg.display.update()


def speed_ch():
    screen_serf = pg.image.load("lug.png")
    screen_rect = screen_serf.get_rect(bottomright=(600, 400))
    screen.blit(screen_serf, screen_rect)

    pg.draw.rect(screen, white, low)
    pg.draw.rect(screen, red, low, 2)

    pg.draw.rect(screen, white, middle)
    pg.draw.rect(screen, red, middle, 2)

    pg.draw.rect(screen, white, fast)
    pg.draw.rect(screen, red, fast, 2)

    low_text = font2.render("Медленная", True, "lightskyblue3")
    middle_text = font2.render("Средняя", True, "lightskyblue3")
    fast_text = font2.render("Быстрая", True, "lightskyblue3")
    screen.blit(low_text, (160, 95))
    screen.blit(middle_text, (190, 195))
    screen.blit(fast_text, (200, 295))
    speed_text = font3.render("Выберите скорость змейки", True, yellow)
    screen.blit(speed_text, (50, 25))

    pg.display.update()


def change_skin():
    screen_serf = pg.image.load("lug.png")
    screen_rect = screen_serf.get_rect(bottomright=(600, 400))
    screen.blit(screen_serf, screen_rect)

    dragon_text = font2.render("Дракон", True, "lightskyblue3")
    snake_text = font2.render("Змейка", True, "lightskyblue3")
    change_text = font2.render("Выберите скин", True, yellow)

    pg.draw.rect(screen, white, snke)
    pg.draw.rect(screen, red, snke, 2)


    pg.draw.rect(screen, white, drgon)
    pg.draw.rect(screen, red, drgon, 2)

    screen.blit(snake_text, (215, 145))
    screen.blit(dragon_text, (205, 265))
    screen.blit(change_text, (115, 50))
    pg.display.update()


def main():
    menu()
    sett = False
    done = False
    sped = False
    skn = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.K_ESCAPE:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                if start_game_box.collidepoint(event.pos) and not sped and not sett and not skn:
                    gameLoop()
                elif sett_box.collidepoint(event.pos) and not sped and not sett and not skn:
                    sett = True
                    settings()
                elif local_menu_box.collidepoint(event.pos) and sett:
                    sett = False
                    menu()
                elif speed.collidepoint(event.pos) and sett and not sped:
                    sett = False
                    sped = True
                    speed_ch()
                elif skin.collidepoint(event.pos) and sett and not skn:
                    sett = False
                    skn = True
                    change_skin()
                elif low.collidepoint(event.pos) and not sett and sped:
                    sped = False
                    sett = False
                    low_speed()
                    menu()
                elif middle.collidepoint(event.pos) and not sett and sped:
                    sped = False
                    sett = False
                    midle_speed()
                    menu()
                elif fast.collidepoint(event.pos) and not sett and sped:
                    sped = False
                    sett = False
                    fast_speed()
                    menu()
                elif snke.collidepoint(event.pos) and not sett and skn and not sped:
                    skn = False
                    menu()
                elif drgon.collidepoint(event.pos) and not sett and skn and not sped:
                    skn = False
                    dragon()
                    menu()
                pass



    pg.display.flip()
    clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
