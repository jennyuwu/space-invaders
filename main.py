import pygame
import random

# Initializes PyGame
pygame.init()

# Create screen pop-up
screen = pygame.display.set_mode((1000, 800))

# Background
background = pygame.image.load('1876.jpg')


# Changing title and logo
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#  Player (loading the player image)
playerImg = pygame.image.load("player_64.png")
playerX = 468
playerY = 700
playerX_change = 0

# Enemy (loading pic for alien)
enemyImg = pygame.image.load("alien.png")
enemyX = random.randint(0, 1000)
enemyY = random.randint(50, 150)
enemyX_change = 5
enemyY_change = 40

# Bullet
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 650
bulletX_change = 0
bulletY_change = 20
bullet_state = "ready"


def player(x, y):
    # Render player sprite
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# Game Loop (making an infinite loop)
# The for loop keeps looping through events to monitor a change of events, such
# as clicking the 'x' button for quit. When this is detected it changes the
# variable to false to close the window/ stop running
running = True
while running:

    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # If keystroke is pressed, check whether left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -15
            if event.key == pygame.K_RIGHT:
                playerX_change = 15
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # playerX = playerX + playerX_change
    playerX += playerX_change

    # Boundaries for screen - Player
    if playerX <= 0:
        playerX = 0
    elif playerX >= 936:
        playerX = 936

    enemyX += enemyX_change
    # Boundaries for screen - Enemy
    if enemyX <= 0:
        enemyX_change = 5
        enemyY += enemyY_change
    elif enemyX >= 936:
        enemyX_change = -5
        enemyY += enemyY_change

    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
