#file with ball class
import pygame,random
import PONGSETTINGS as settings

class Ball(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = 15
        self.speed = 3
        self.vertical = random.choice([0,1])   #vertical 0 - up 1 - down
        self.horizontal = random.choice([0,1]) #horizontal 0 - left  1 - right
        self.color = (255,255,255)
        self.image = pygame.Surface((self.size,self.size))
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, self.color, (self.rect.width//2,self.rect.height//2), self.size//2)
        self.rect.center = (settings.WIDTH//2,settings.HEIGHT//2)
    
    def update(self):
        self.check_wall_collision()
        if self.vertical:
            self.rect.bottom += self.speed
        if not self.vertical:
            self.rect.top -= self.speed
        if self.horizontal:
            self.rect.right += self.speed
        if not self.horizontal:
            self.rect.left -= self.speed
    
    def draw(self,window):
        #pygame.draw.circle(window, (255,255,255), (100,100), self.size/2)
        window.blit(self.image,self.rect)

    def check_wall_collision(self):
        if self.rect.left < 0:
            self.horizontal = 1
        if self.rect.right > settings.WIDTH:
            self.horizontal = 0