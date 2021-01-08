import pygame,sys
import PONGSETTINGS as settings
import PADDLE as paddle
from pygame.locals import *

def startMenu(window):
    menuClock = pygame.time.Clock()

    while True:
        window.fill((0,0,0))
        surfaces_to_print,surfaces_rects = prepareMenuOptions()
        option_choosed = ""
        
        #change collor when cursos collision
        for key in surfaces_rects:
            if surfaces_rects[key].collidepoint(pygame.mouse.get_pos()):
                if key == 'onePlayerOpt':
                    surfaces_to_print,surfaces_rects = prepareMenuOptions(onep_c=(80,80,80))
                if key == 'twoPlayerOpt':
                    surfaces_to_print,surfaces_rects = prepareMenuOptions(twop_c=(80,80,80))
                option_choosed = key

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    return option_choosed
        window.blits(surfaces_to_print)
        pygame.display.update()
        
        menuClock.tick(60)

def prepareMenuOptions(onep_c = (255,255,255), twop_c = (255,255,255)):
    pygame.font.init()

    title_c = (255,255,255)
    window_center = settings.WIDTH//2
    
    #title
    titleFont = pygame.font.SysFont('courier',100,True)
    title = titleFont.render("PONG",True,title_c)
    title_rect = title.get_rect()
    title_rect.center = (window_center,100)

    #options
    optionFont = pygame.font.SysFont('courier',40)

    #1p
    onePlayerOpt = optionFont.render("1-P Mode",True,(0,0,0))
    temp_sur = pygame.Surface(onePlayerOpt.get_size())
    temp_sur.fill(onep_c)
    temp_sur.blit(onePlayerOpt,(0,0))
    onePlayerOpt = temp_sur
    onePlayerOpt_rect = onePlayerOpt.get_rect()
    onePlayerOpt_rect.top = title_rect.bottom + 30
    onePlayerOpt_rect.centerx = window_center 

    #2p
    twoPlayerOpt = optionFont.render("2-P Mode",True,(0,0,0))
    temp_sur = pygame.Surface(twoPlayerOpt.get_size())
    temp_sur.fill(twop_c)
    temp_sur.blit(twoPlayerOpt,(0,0))
    twoPlayerOpt = temp_sur
    twoPlayerOpt_rect = twoPlayerOpt.get_rect()
    twoPlayerOpt_rect.top = onePlayerOpt_rect.bottom + 10
    twoPlayerOpt_rect.centerx = window_center 


    #list of surfaces to print
    surfaces = [(title,title_rect.topleft),
    (onePlayerOpt,onePlayerOpt_rect),
    (twoPlayerOpt,twoPlayerOpt_rect)]

    #dict of rect
    rects = {'title':title_rect,'onePlayerOpt':onePlayerOpt_rect,'twoPlayerOpt':twoPlayerOpt_rect}

    return surfaces,rects

def onePlayerMode(window):
    onePlayerClock = pygame.time.Clock()
    player = paddle.Paddle()
    game_start = False
    while True:
        window.fill((0,0,0))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == K_a:
                    player.left = True
                if event.key == K_RIGHT or event.key == K_d:
                    player.right = True
            if event.type == KEYUP:
                if event.key == K_RETURN:
                    game_start = True
                if event.key == K_LEFT or event.key == K_a:
                    player.left = False
                if event.key == K_RIGHT or event.key == K_d:
                    player.right = False
        
        if game_start == True:
            player.update()
        
        else:
            text_font = pygame.font.SysFont('courier',20)
            text = text_font.render("Press 'ENTER' to start",True,(255,255,255))
            text_rect = text.get_rect()
            window.blit(text,(settings.WIDTH//2 - text_rect.width//2,settings.HEIGHT//2 - text_rect.height//2))
        
        player.draw(window)
        pygame.display.update()
        onePlayerClock.tick(60)

if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((settings.WIDTH,settings.HEIGHT))
    pygame.display.set_caption("Pong")
    while True:
        game_mode = startMenu(window)
        if game_mode == 'onePlayerOpt':
            onePlayerMode(window)