import pygame
pygame.mixer.init()
pygame.mixer.music.load("/home/pi/chain.mp3")
pygame.mixer.music.play()
while True:
    if pygame.mixer.music.get_busy() == False:
        pygame.mixer.music.load("/home/pi/chain.mp3")
        pygame.mixer.music.play()