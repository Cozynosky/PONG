import pygame, sys
import PONGSETTINGS as settings
import PADDLE as pad
import BALL as b
from pygame.locals import *


def startMenu(window):
    menuClock = pygame.time.Clock()

    while True:
        window.fill((0, 0, 0))
        surfaces_to_print, surfaces_rects = prepareMenuOptions()
        option_choosed = ""

        # change collor when cursos collision
        for key in surfaces_rects:
            if surfaces_rects[key].collidepoint(pygame.mouse.get_pos()):
                if key == "onePlayerOpt":
                    surfaces_to_print, surfaces_rects = prepareMenuOptions(
                        onep_c=(80, 80, 80)
                    )
                if key == "twoPlayerOpt":
                    surfaces_to_print, surfaces_rects = prepareMenuOptions(
                        twop_c=(80, 80, 80)
                    )
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


def prepareMenuOptions(onep_c=(255, 255, 255), twop_c=(255, 255, 255)):
    pygame.font.init()

    title_c = (255, 255, 255)
    window_center = settings.WIDTH // 2

    # title
    titleFont = pygame.font.SysFont("courier", 100, True)
    title = titleFont.render("PONG", True, title_c)
    title_rect = title.get_rect()
    title_rect.center = (window_center, 100)

    # options
    optionFont = pygame.font.SysFont("courier", 40)

    # 1p
    onePlayerOpt = optionFont.render("1-P Mode", True, (0, 0, 0))
    temp_sur = pygame.Surface(onePlayerOpt.get_size())
    temp_sur.fill(onep_c)
    temp_sur.blit(onePlayerOpt, (0, 0))
    onePlayerOpt = temp_sur
    onePlayerOpt_rect = onePlayerOpt.get_rect()
    onePlayerOpt_rect.top = title_rect.bottom + 30
    onePlayerOpt_rect.centerx = window_center

    # 2p
    twoPlayerOpt = optionFont.render("2-P Mode", True, (0, 0, 0))
    temp_sur = pygame.Surface(twoPlayerOpt.get_size())
    temp_sur.fill(twop_c)
    temp_sur.blit(twoPlayerOpt, (0, 0))
    twoPlayerOpt = temp_sur
    twoPlayerOpt_rect = twoPlayerOpt.get_rect()
    twoPlayerOpt_rect.top = onePlayerOpt_rect.bottom + 10
    twoPlayerOpt_rect.centerx = window_center

    # list of surfaces to print
    surfaces = [
        (title, title_rect.topleft),
        (onePlayerOpt, onePlayerOpt_rect),
        (twoPlayerOpt, twoPlayerOpt_rect),
    ]

    # dict of rect
    rects = {
        "title": title_rect,
        "onePlayerOpt": onePlayerOpt_rect,
        "twoPlayerOpt": twoPlayerOpt_rect,
    }

    return surfaces, rects


def onePlayerMode(window):
    onePlayerClock = pygame.time.Clock()
    player = pad.Paddle()

    # setup fonts
    score_font = pygame.font.SysFont("courier", 20, True)
    text_font = pygame.font.SysFont("courier", 20)

    ball = b.Ball()
    game_start = False
    while ball.ball_on_board:
        window.fill((0, 0, 0))

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

        # draw elements
        player.draw(window)
        ball.draw(window)
        score = score_font.render("SCORE:" + str(player.score), True, (0, 255, 255))
        score_rect = score.get_rect()
        window.blit(score, (settings.WIDTH // 2 - score_rect.width // 2, 40))

        # update elements if true
        if game_start == True:
            player.update()
            player.ball_hitted(ball)
            ball.update()

        else:
            text = text_font.render("Press 'ENTER' to start", True, (255, 255, 255))
            text_rect = text.get_rect()
            window.blit(
                text,
                (
                    settings.WIDTH // 2 - text_rect.width // 2,
                    settings.HEIGHT // 2 - text_rect.height // 2 - 40,
                ),
            )

        pygame.display.update()
        onePlayerClock.tick(60)

    game_ended = True

    while game_ended:

        player.draw(window)
        ball.draw(window)

        ending = text_font.render("Press any key to go to menu", True, (255, 255, 255))
        ending_rect = ending.get_rect()
        window.blit(
            ending,
            (
                settings.WIDTH // 2 - ending_rect.width // 2,
                settings.HEIGHT // 2 - ending_rect.height // 2 - 40,
            ),
        )

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                game_ended = False

        pygame.display.update()
        onePlayerClock.tick(60)


def twoPlayerMode(window):
    twoPlayerClock = pygame.time.Clock()
    p1 = pad.Paddle()
    p2 = pad.Paddle("P2")

    ball = b.Ball("2P")

    text_font = pygame.font.SysFont("courier", 20)
    score_font = pygame.font.SysFont("courier", 30, True)
    scored_font = pygame.font.SysFont("courier", 40, True)

    game_start = False

    while p1.lifes > 0 and p2.lifes > 0:
        window.fill((0, 0, 0))
        new_round = False

        if not ball.ball_on_board:
            who_scored = ball.who_scored()
            if who_scored == "P1":
                p2.lifes -= 1
            if who_scored == "P2":
                p1.lifes -= 1

            scored = scored_font.render(who_scored + " SCORED!", True, (0, 255, 255))
            scored_rect = scored.get_rect()
            window.blit(
                scored,
                (
                    settings.WIDTH // 2 - scored_rect.width // 2,
                    settings.HEIGHT // 2 - 40,
                ),
            )

            ball = b.Ball("2P")
            new_round = True

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                # p1
                if event.key == K_LEFT:
                    p1.left = True
                if event.key == K_RIGHT:
                    p1.right = True
                # p2
                if event.key == K_a:
                    p2.left = True
                if event.key == K_d:
                    p2.right = True
            if event.type == KEYUP:
                if event.key == K_RETURN:
                    game_start = True
                # p1
                if event.key == K_LEFT:
                    p1.left = False
                if event.key == K_RIGHT:
                    p1.right = False
                # p2
                if event.key == K_a:
                    p2.left = False
                if event.key == K_d:
                    p2.right = False

        # draw elements
        score_p1 = score_font.render("P1: " + "♡" * p1.lifes, True, (0, 255, 255))
        score_p2 = score_font.render("P2: " + "♡" * p2.lifes, True, (0, 255, 255))
        score_p1_rect = score_p1.get_rect()
        score_p2_rect = score_p2.get_rect()
        window.blit(
            score_p1,
            (
                settings.WIDTH // 2 - (score_p1_rect.width + (14 * (3 - p1.lifes))) * 2,
                settings.HEIGHT // 2 - score_p1_rect.height // 2,
            ),
        )
        window.blit(
            score_p2,
            (
                settings.WIDTH // 2 + (score_p2_rect.width + (14 * (3 - p2.lifes))),
                settings.HEIGHT // 2 - score_p2_rect.height // 2,
            ),
        )
        p1.draw(window)
        p2.draw(window)
        ball.draw(window)

        # update elements if true
        if game_start == True:
            p1.update()
            p2.update()
            p1.ball_hitted(ball)
            p2.ball_hitted(ball)
            ball.update()

        else:
            text = text_font.render("Press 'ENTER' to start", True, (255, 255, 255))
            text_rect = text.get_rect()
            window.blit(
                text,
                (
                    settings.WIDTH // 2 - text_rect.width // 2,
                    settings.HEIGHT // 2 - text_rect.height // 2 - 40,
                ),
            )

        pygame.display.update()
        if new_round:
            pygame.time.wait(500)
        twoPlayerClock.tick(60)

    game_ended = True

    while game_ended:
        p1.draw(window)
        p2.draw(window)

        ending = text_font.render("Press any key to go to menu", True, (255, 255, 255))
        ending_rect = ending.get_rect()
        window.blit(
            ending,
            (
                settings.WIDTH // 2 - ending_rect.width // 2,
                settings.HEIGHT // 2 - ending_rect.height // 2 - 55,
            ),
        )

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                game_ended = False

        pygame.display.update()
        twoPlayerClock.tick(60)


if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    pygame.display.set_caption("Pong")
    while True:
        game_mode = startMenu(window)
        if game_mode == "onePlayerOpt":
            onePlayerMode(window)
        if game_mode == "twoPlayerOpt":
            twoPlayerMode(window)
