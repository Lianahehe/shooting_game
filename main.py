import pygame

# initialises the game
pygame.init()

# creates the screen (w x h)
screen = pygame.display.set_mode( (800, 600))

running = True

#changing Title of the game 
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Space Shooter")

# Player details
playerImg = pygame.image.load("player.png")
# sets where the image wants to be set (position)
playerX = 370
playerY = 480
playerX_change = 0

def player(x,y):
    # blit means to draw, parameters is ( image, coordinates)
    screen.blit(playerImg, (x,y) )


# closes the screen when we quit, if dont have this, then the screen is open forever
while running :
    # changing colour of background
    screen.fill( (177, 156, 217))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # checks if key pressed is right or left (only works on arrow keys)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0
    
    playerX += playerX_change

    #take into consideration pizel size of spaceship(64x64)
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    player(playerX, playerY)
    pygame.display.update()
