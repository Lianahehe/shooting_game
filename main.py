import pygame
import random

# initialises the game
pygame.init()

# creates the screen (w x h)
screen = pygame.display.set_mode( (800, 600))

# background
background = pygame.image.load("space_background.png")

running = True

#changing Title of the game 
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Space Shooter")

# Player details
playerImg = pygame.image.load("player.png")
# sets where the image wants to be set (position)
playerX = 370
playerY = 500
playerX_change = 0

# Enemy details
enemyImg = pygame.image.load("monster.png")
# sets where the image wants to be set (position)
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 3
enemyY_change = 40

# Bullet details
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletY_change = 10
bullet_state = "ready"

def player(x,y):
    # blit means to draw, parameters is ( image, coordinates)
    screen.blit(playerImg, (x,y) )

def enemy(x,y):
    # blit means to draw, parameters is ( image, coordinates)
    screen.blit(enemyImg, (x,y) )

def bullet_fire(x,y):
    # global so it can be accessed within the function 
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16,y + 10))


# closes the screen when we quit, if dont have this, then the screen is open forever
while running :
    # changing colour of background
    #screen.fill( (177, 156, 217))

    # background image
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # checks if key pressed is right or left (only works on arrow keys)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
            if event.key == pygame.K_LEFT:
                playerX_change = -3

            # button for the bullet 
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    bullet_fire(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0
    
    playerX += playerX_change

    #take into consideration pizel size of spaceship(64x64)
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # enemy movement
    # hits boundary it will move downwards
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = +3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -3
        enemyY += enemyY_change

    # bullet movement
    if bullet_state is "fire":
        bullet_fire(bulletX, bulletY)
        bulletY -= bulletY_change
    #resets the bullet to its ready position (at the spaceship)
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
        
        

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
