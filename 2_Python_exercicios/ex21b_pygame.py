import pygame
pygame.init() #inicar o pygame
pygame.mixer.music.load("ex021.mp3")
pygame.mixer.music.play()
pygame.event.wait() #esperar terminar para encerrar
