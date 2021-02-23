import os

import pygame
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15
SIZE = (600, 400)
background = pygame.Surface(SIZE)

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
fullname = os.path.join("apple.png")
image = pygame.image.load('apple.png')
image.set_colorkey(white)
sprite.image = image
sprite.rect = sprite.image.get_rect()

im = pygame.image.load('Snake sprite.png')
im.set_colorkey(white)
headlist = pygame.sprite.Group()
sprite1 = pygame.sprite.Sprite()
fullname1 = os.path.join("Head.png")
sprite1.image1 = pygame.image.load(fullname1)
sprite1.rect = sprite1.image1.get_rect()
Rotation = 'Down'

im1 = pygame.image.load('Head.png')
im1.set_colorkey('black')
im2 = pygame.image.load('HeadL.png')
im2.set_colorkey('black')
im3 = pygame.image.load('HeadU.png')
im3.set_colorkey('black')
im4 = pygame.image.load('HeadR.png')
im4.set_colorkey('black')

bodylist = pygame.sprite.Group()
sprite2 = pygame.sprite.Sprite()
fullname2 = os.path.join("Snake sprite.png")
sprite2.image2 = pygame.image.load(fullname2)
sprite2.rect = sprite2.image2.get_rect()


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list, Rotation):
    for x in snake_list:
        if x == snake_list[-1]:
            if Rotation == 'Up':
                dis.blit(im3, [x[0], x[1], snake_block, snake_block])
            elif Rotation == 'Right':
                dis.blit(im2, [x[0], x[1], snake_block, snake_block])
            elif Rotation == 'Left':
                dis.blit(im4, [x[0], x[1], snake_block, snake_block])
            else:
                dis.blit(im1, [x[0], x[1], snake_block, snake_block])
        else:
            dis.blit(im, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    for item in all_sprites:
        item.kill()
        all_sprites.clear(dis, background)
        all_sprites.draw(dis)
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    Rotation = 'Down'
    snake_List = []
    Length_of_snake = 1

    a = Food(all_sprites)

    while not game_over:

        while game_close:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Rotation = 'Left'
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    Rotation = 'Right'
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    Rotation = 'Up'
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    Rotation = 'Down'
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        xf = Food.get_x(a)
        yf = Food.get_y(a)
        all_sprites.draw(dis)
        snake_Head = [x1, y1]
        Head(x1, y1)
        headlist.draw(dis)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List, Rotation)
        Your_score(Length_of_snake - 1)

        pygame.display.update()
        if (x1 + 10 == xf and y1 + 10 == yf) or (x1 + 10 == xf + 1 and y1 + 10 == yf + 1):
            for item in all_sprites:
                item.kill()
                all_sprites.clear(dis, background)
                all_sprites.draw(dis)
            a = Food(all_sprites)
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


class Food(pygame.sprite.Sprite):
    image = pygame.image.load(fullname)
    image.set_colorkey(white)

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Food.image
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.x = round(random.randrange(10, dis_width - snake_block) / 10.0) * 10.0
        self.y = round(random.randrange(10, dis_height - snake_block) / 10.0) * 10.0
        self.rect.center = (self.x, self.y)
        self.x1 = self.x
        self.y1 = self.y

    def get_x(self):
        return self.x1

    def get_y(self):
        return self.y1


class Head:
    image1 = pygame.image.load(fullname1)

    def __init__(self, x, y):
        super().__init__()
        self.image = Head.image1
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (self.x, self.y)


gameLoop()
