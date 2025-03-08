import pygame
pygame.init() #inicar o pygame
pygame.mixer.music.load('/Users/thaismoreira/GITHUB/Python3-Mundo01-Gustavo-Guanabara/2_Python_exercicios/ex021.mp3')
pygame.mixer.music.play()

#pygame.event.wait() 
#> NAO ESTÁ FUNCIONANDO. AI TEM A SOLUÇAO ABAIXO, MAS ENVOLVE CODIGO QUE NAO FOI ESTUDADO AINDA

# Enquanto o áudio estiver tocando, espera
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)  # Aguarda um pouco para não sobrecarregar o processador