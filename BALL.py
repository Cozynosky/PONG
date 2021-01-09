# file with ball class
import pygame, random
import PONGSETTINGS as settings


class Ball(pygame.sprite.Sprite):
    def __init__(self, gamemode="1P"):
        pygame.sprite.Sprite.__init__(self)
        self.ball_on_board = True
        self.gamemode = gamemode
        self.size = 15
        self.speed = 3
        self.down = random.choice([0, 1])  # vertical 0 - up 1 - down
        self.right = random.choice([0, 1])  # horizontal 0 - left  1 - right
        self.color = (255, 255, 255)
        self.image = pygame.Surface((self.size, self.size))
        self.rect = self.image.get_rect()
        pygame.draw.circle(
            self.image,
            self.color,
            (self.rect.width // 2, self.rect.height // 2),
            self.size // 2,
        )
        self.rect.center = (settings.WIDTH // 2, settings.HEIGHT // 2)

    def update(self):
        self.check_wall_collision()
        if self.down:
            self.rect.bottom += self.speed
        if not self.down:
            self.rect.top -= self.speed
        if self.right:
            self.rect.right += self.speed
        if not self.right:
            self.rect.left -= self.speed

    def draw(self, window):
        # pygame.draw.circle(window, (255,255,255), (100,100), self.size/2)
        window.blit(self.image, self.rect)

    def who_scored(self):
        if self.rect.bottom < 0:
            return "P1"
        if self.rect.top > settings.HEIGHT:
            return "P2"

    def check_wall_collision(self):
        if self.rect.left < 0:
            self.right = 1
        if self.rect.right > settings.WIDTH:
            self.right = 0
        if self.rect.top > settings.HEIGHT:
            self.ball_on_board = False
        if self.gamemode == "1P":
            if self.rect.top < 0:
                self.down = 1
        if self.gamemode == "2P":
            if self.rect.bottom < 0:
                self.ball_on_board = False
