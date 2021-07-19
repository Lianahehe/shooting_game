import pygame
import random
import math

# initialises the game
pygame.init()

# creates the screen (w x h)
screen = pygame.display.set_mode( (800, 600))

# background
background = pygame.image.load("space_background.png")

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
# initialising enemy list, to set apart the details of each enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

# appends new enemy into the list
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("monster.png"))
    # sets where the image wants to be set (position)
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(2)
    enemyY_change.append(40)

# Bullet details
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletY_change = 10
bullet_state = "ready"

# Score
score_value = 0
# parameters is (font,size)
font = pygame.font.Font('Minecraft.ttf', 32)
textX = 10
textY = 10

def show_score(x,y):
    score = font.render("Score : " + str(score_value), True, (255,255,255) )
    screen.blit(score, (textX, textY) )

def player(x,y):
    # blit means to draw, parameters is ( image, coordinates)
    screen.blit(playerImg, (x,y) )

def enemy(x,y,i):
    # blit means to draw, parameters is ( image, coordinates)
    screen.blit(enemyImg[i], (x,y) )

def bullet_fire(x,y):
    # global so it can be accessed within the function 
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16,y + 10))

# collision of bullet and enemy
# equation of distance between 2 points and the midpoint
def is_collision(enemyX, enemyY, bulletX, bulletY) : 
    distance = math.sqrt(math.pow(enemyX-bulletX, 2) + math.pow(enemyY - bulletY, 2) )
    if distance < 27 :
        return True
    return False

running = True
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
                playerX_change = 4
            if event.key == pygame.K_LEFT:
                playerX_change = -4

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
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = +2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]

        # collision (what happens when bullet collides with enemy)
        collision = is_collision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision :
            bulletY = 480
            bullet_state = "ready"
            score_value += 1

            # enemy respawn
            enemyX[i] = random.randint(0,735 )
            enemyY[i] = random.randint(50,150)
        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bullet_state is "fire":
        bullet_fire(bulletX, bulletY)
        bulletY -= bulletY_change
    #resets the bullet to its ready position (at the spaceship)
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"


    player(playerX, playerY)
    show_score(textX,textY)
    pygame.display.update()
