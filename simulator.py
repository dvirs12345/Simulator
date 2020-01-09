import pygame

pygame.init()  # init a game
screen = pygame.display.set_mode((1000, 600))  # Set the screen to be x,y


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()
