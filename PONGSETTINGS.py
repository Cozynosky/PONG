import pygame

pygame.init()

WIDTH = 400
HEIGHT = 600
sounds = "on"
music = "on"
# all playing background music
background_music = pygame.mixer.music.load("DATA\\SOUNDS\\theme.mp3")
pygame.mixer.music.play()

# sounds as events
ball_hit_sound = pygame.mixer.Sound("DATA\\SOUNDS\\ball_hit.wav")
ball_dead_sound = pygame.mixer.Sound("DATA\\SOUNDS\\ball_dead.wav")
wall_hit_sound = pygame.mixer.Sound("DATA\\SOUNDS\\wall_hitted.wav")
gameover_sound = pygame.mixer.Sound("DATA\\SOUNDS\\game_over.wav")


def play_sound(event):
    # play sound depends on input [paddle_hit,wall_hit,ball_dead,gameover]
    if sounds == "on":
        if event == "paddle_hit":
            ball_hit_sound.play()
        if event == "wall_hit":
            wall_hit_sound.play()
        if event == "ball_dead":
            ball_dead_sound.play()
        if event == "gameover":
            gameover_sound.play()
