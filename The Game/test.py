import pygame
import random
from Sprites.Player import Player
from Sprites.CactusSingle import CactusSingle
from Sprites.CactusDouble import CactusDouble

obstacleProbability = 0.5
global obstaclesOnScreen
obstaclesOnScreen = []
speed = 1.5

def drawGameBackground():
    screen.fill(background_colour)


def drawCharacter():
    tRex.drawCharacter(screen)
    for obstacles in obstaclesOnScreen:
        obstacles.drawCharacter(screen)
    pygame.display.update()

def generateGameObstacles():
    if len(obstaclesOnScreen) == 0 or obstaclesOnScreen[len(obstaclesOnScreen) - 1].x < 1000:
        if random.uniform(0,1) < obstacleProbability:
            obstacleNumber = random.randint(0,6)
            if obstacleNumber <= 2:
                obstaclesOnScreen.append(CactusSingle(1370, 620))
            elif obstacleNumber <= 4:
                obstaclesOnScreen.append(CactusDouble(1370, 620))

def cleanDeadObstaclesAndPropagate(obstacles):
    index = 0;
    for obstacle in obstacles:
        if obstacle.x >= 0:
            break
        index+=1
    obstacles = obstacles[index : ]
    for obstacle in obstacles:
        obstacle.propagate(speed)
    return obstacles




pygame.init()
clock = pygame.time.Clock()
background_colour = (255,255,255)
(width, height) = (1370, 750)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('T-Rex')
drawGameBackground()
pygame.display.flip()

x = 30
y = 600

direction = -1
tRex = Player(x, y)
cactusSingle = CactusSingle(1370, 620)


running = True
jump = False
while running:
    clock.tick(175)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    keys = pygame.key.get_pressed()

    if not jump:
        if keys[pygame.K_SPACE]:
            jump = True
    else:
        tRex.y += 2 * direction
        if tRex.y < 520 :
            direction = 1
        elif tRex.y == y:
            direction = -1
            jump = False

    drawGameBackground()
    generateGameObstacles()
    obstaclesOnScreen = cleanDeadObstaclesAndPropagate(obstaclesOnScreen)
    drawCharacter()
