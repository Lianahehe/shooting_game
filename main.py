import pygame

# initialises the game
pygame.init()

# creates the screen
screen = pygame.display.set_mode( (800, 600))

running = True

# closes the screen when we quit, if dont have this, then the screen is open forever
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

