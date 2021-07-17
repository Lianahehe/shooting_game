import pygame

# initialises the game
pygame.init()

# creates the screen (w x h)
screen = pygame.display.set_mode( (800, 600))

running = True

#changing Title of the game 
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Space Invaders")

# Player details
playerImg = pygame.image.load("player.png")
# sets where the image wants to be set (position)
playerX = 370
playerY = 480

def player():
    # blit means to draw, parameters is ( image, coordinates)
    screen.blit(playerImg, (playerX,playerY))


# closes the screen when we quit, if dont have this, then the screen is open forever
while running :
    # changing colour of background
    screen.fill( (177, 156, 217))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player()
    pygame.display.update()
