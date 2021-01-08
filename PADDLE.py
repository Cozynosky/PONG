#file with paddle class
import pygame
import PONGSETTINGS as settings

class Paddle(pygame.sprite.Sprite):

    def __init__(self,player='P1'):
        pygame.sprite.Sprite.__init__(self)
        self.height = 15
        self.width = 70
        self.speed = 5
        self.left = False
        self.right = False
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.centerx = settings.WIDTH//2
        if player == 'P1':
            self.rect.bottom = settings.HEIGHT - 10
    
    def update(self):
        if self.left  and self.rect.left > 0:
            self.rect.left -= self.speed
        if self.right and self.rect.right < settings.WIDTH:
            self.rect.right += self.speed
    
    def draw(self,window):
        window.blit(self.image,self.rect)