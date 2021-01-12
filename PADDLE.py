# file with paddle class
import pygame
import PONGSETTINGS as settings


class Paddle(pygame.sprite.Sprite):
    def __init__(self, player="P1"):
        pygame.sprite.Sprite.__init__(self)
        self.lifes = 3
        self.player = player
        self.height = 15
        self.width = 70
        self.speed = 5
        self.score = 0
        self.play_sound = False
        self.left = False
        self.right = False
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.centerx = settings.WIDTH // 2
        if player == "P1":
            self.rect.bottom = settings.HEIGHT - 10
        if player == "P2":
            self.rect.top = 10

    def update(self):
        if self.left and self.rect.left > 0:
            self.rect.left -= self.speed
        if self.right and self.rect.right < settings.WIDTH:
            self.rect.right += self.speed
        if self.play_sound:
            settings.play_sound("paddle_hit")
            self.play_sound = False

    def draw(self, window):
        window.blit(self.image, self.rect)

    def reset_position(self):
        self.rect.centerx = settings.WIDTH // 2
        if self.player == "P1":
            self.rect.bottom = settings.HEIGHT - 10
        if self.player == "P2":
            self.rect.top = 10

    def ball_hitted(self, ball):
        # check if ball was hitted recently
        if ball.just_hitted == 0:
            # check collision
            if ball.rect.colliderect(self.rect):
                # check if it was directly in the paddle corner
                if (
                    (
                        ball.rect.right > self.rect.left
                        and ball.rect.left < self.rect.left
                    )
                    or (
                        ball.rect.left < self.rect.right
                        and ball.rect.right > self.rect.right
                    )
                ) and (
                    (self.player == "P1" and ball.rect.bottom < self.rect.top + 4)
                    or (self.player == "P2" and ball.rect.top > self.rect.bottom - 4)
                ):
                    # if opposite directions change ball direction
                    if (self.left and ball.right) or (self.right and not ball.right):
                        ball.right = not ball.right
                    ball.down = not ball.down
                    self.score += 1
                    ball.speed += 1
                # check if it hitted centre of the paddle
                elif (
                    ball.rect.centerx > self.rect.left
                    and ball.rect.centerx < self.rect.right
                ):
                    # speedup when same directions
                    if (self.right and ball.right) or (self.left and not ball.right):
                        ball.speed += 1
                    # other way slow down
                    elif (
                        (self.left and ball.right) or (self.right and not ball.right)
                    ) and ball.speed > 2:
                        ball.speed -= 1
                    ball.down = not ball.down
                    self.score += 1
                # if it was on the side
                elif (
                    ball.rect.right > self.rect.left and ball.rect.left < self.rect.left
                ) or (
                    ball.rect.left < self.rect.right
                    and ball.rect.right > self.rect.right
                ):
                    ball.right = not ball.right
                    ball.speed += 2
                    pass

                self.play_sound = True
                ball.just_hitted = 60
        # substrac 1 if it was hitted
        else:
            ball.just_hitted -= 1
