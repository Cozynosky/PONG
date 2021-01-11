import pygame

pygame.init()

WIDTH = 400
HEIGHT = 600
ball_hit_sound = pygame.mixer.Sound('DATA\\SOUNDS\\ball_hit.wav')
ball_dead_sound = pygame.mixer.Sound('DATA\\SOUNDS\\ball_dead.wav')
wall_hit_sound = pygame.mixer.Sound('DATA\\SOUNDS\\wall_hitted.wav')
gameover_sound = pygame.mixer.Sound('DATA\\SOUNDS\\game_over.wav')