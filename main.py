import pygame
from random import randint
from math import sqrt

pygame.init()

WHITE = (255, 255, 255)
DA = (123, 0, 73)
BLACK = (0, 0, 0)
SIZE = (1280, 1024)
FPS = 240
PURPLE = (90, 0, 157)
sc = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

cursor = pygame.image.load('cursor.png')
osua = pygame.image.load('osua.png')
osub = pygame.image.load('osub.png')
osuc = pygame.image.load('osuc.png')
map = pygame.image.load('map.png')
menu = pygame.image.load('menuosu.png')



circledira = 200
points = 0
circles = []
speed = 1
lives = 3
points50=0
points100=0
points300=0
colvo = 0
r = 50
miss=0
maxcolvo=0
maxcolvo1=0
gamemode=0
gameover = 3
higthscore=0

#ШРИФТЫ
font = pygame.font.SysFont('comic sans ms', 50)
fontda = pygame.font.SysFont('comic sans ms', 50)
game_over_font = pygame.font.SysFont('comic sans ms', 100)
#segoe print


circlex = randint(0 + 200, 1280 - 200)
circley = randint(0 + 200, 1024 - 200)

isGameRunning = True
while isGameRunning:
    if gamemode == 1:
        gameover = 1
    sc.blit(map, (0, 0))
    x, y = pygame.mouse.get_pos()
    x -= 80
    y -= 80
    sc.blit(cursor, (x, y))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            isGameRunning = False
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                if (i.pos[0]-circlex)<r and (i.pos[1]-circley)<r\
                and 85>=circledira>=71:
                    colvo+=1
                    points += 1
                    points50 += 1
                    maxcolvo += 1
                elif (i.pos[0]-circlex)<r and (i.pos[1]-circley)<r\
                and 70>=circledira>=61:
                    colvo += 1
                    points += 1
                    points100 += 1
                    maxcolvo += 1
                elif (i.pos[0]-circlex)<r and (i.pos[1]-circley)<r\
                and 60>=circledira>=50:
                    maxcolvo += 1
                    points += 1
                    points300 += 1
                    colvo += 1
                elif (i.pos[0]-circlex)>r or (i.pos[1]-circley)>r or circledira<50:
                    lives-=1
                else:
                    lives -= 1
                    colvo=0
                    miss+=1


    #ЖИЗНИ И КОМБО
    if colvo>=3:
        lives=3
    if lives <= 0:
        gameover = 0
    if maxcolvo1<=colvo:
        maxcolvo1=colvo

#СОЗДАНИЕ КРУГОВ
    sc.blit(map, (0, 0))
    sc.fill(BLACK)
    sc.blit(map, (0, 0))
    # КРУГИ
    сircle1 = pygame.draw.circle(sc, WHITE, (circlex, circley), r)
    circle2 = pygame.draw.circle(sc, PURPLE, (circlex, circley), circledira, 5)
    circledira -= speed
#КУРСОР
    x, y = pygame.mouse.get_pos()
    x -= 80
    y -= 80
    sc.blit(cursor, (x, y))

    if (circledira < 50):
        circlex = randint(0 + 200, 1280 - 200)
        circley = randint(0 + 200, 1024 - 200)
        circledira = 200
        speed += 0.01

    live = fontda.render(str(lives), True, WHITE)
    sc.blit(live, (47, 3))
    score = fontda.render(str(points), True, WHITE)
    sc.blit(score, (1220, 0))
    colvox = fontda.render('x' + str(colvo), True, WHITE)
    sc.blit(colvox, (8, 962))
    game_over = game_over_font.render('GAME OVER', True, WHITE)

    #GAME OVER
    if gameover==0:
        if points50 <= points300 >= points100:
            sc.blit(osua, (0, 0))
        elif points300 <= points50 >= points100:
            sc.blit(osuc, (0, 0))
        elif points50 <= points100 >= points300:
            sc.blit(osub, (0, 0))

        #РЕЗУЛЬТАТЫ
        scorer = font.render(str(points), True, WHITE)
        sc.blit(scorer, (200, 170))
        score300 = font.render(str(points300), True, WHITE)
        sc.blit(score300, (150, 305))
        score100 = font.render(str(points100), True, WHITE)
        sc.blit(score100, (150, 435))
        score50 = font.render(str(points50), True, WHITE)
        sc.blit(score50, (150, 560))
        misses = font.render(str(miss), True, WHITE)
        sc.blit(misses, (600, 560))
        combo = font.render('x'+str(maxcolvo1), True, WHITE)
        sc.blit(combo, (70, 700))
        # МЫШКА
        x, y = pygame.mouse.get_pos()
        x -= 80
        y -= 80
        sc.blit(cursor, (x, y))
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                if 995 < i.pos[0] < 1058 and 737 < i.pos[1] < 799:
                    gamemode=1
                    lives=3
                    maxcolvo = 0
                    points = 0
                    points300 = 0
                    points100 = 0
                    points50 = 0
                    colvo = 0
                    speed=1

    if gameover==3:
        sc.fill(BLACK)
        sc.blit(menu, (0, 0))
        x, y = pygame.mouse.get_pos()
        x -= 80
        y -= 80
        sc.blit(cursor, (x, y))
        for i in pygame.event.get():
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    if 291 <= i.pos[0] <= 986 and 156 <= i.pos[1] <= 855:
                        gamemode=1
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()