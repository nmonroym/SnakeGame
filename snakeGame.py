# Snake Game
# by Neo

# Our game imports
import pygame, sys, random, time

check_errors = pygame.init()
# (6,0)
if check_errors[1] > 0:
    print("(!) Had  {0} initializing errors, exiting....".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGane successfully initialized!")

# Play surface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption("Snake game!")

# Colors
red = pygame.Color(255, 0, 0) # Gameover
green = pygame.Color(0, 255, 0) # Snake
green_2 = pygame.Color(66, 245, 105) # Title Game
lightgreen = pygame.Color(144, 238, 144)
indianred = pygame.Color(220,20,60)
black = pygame.Color(0, 0, 0) # Score
white = pygame.Color(255, 255, 255) # Background
brown = pygame.Color(165, 42, 42) # Food

# FPS controller
fpsController = pygame.time.Clock()

# Important variables
snakePos = [100,50]
snakeBody = [[100,50], [90,50], [80,50]]

foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
foodSpawn = True

direction = 'RIGHT'
changeto = direction

score = 0

gameStarted = False

# Game over function
def gameOver():
    global gameStarted

    showTitleGame()

    myFont = pygame.font.SysFont('monaco', 56)
    GOSurf = myFont.render("Game Over!", True, red)
    GORect = GOSurf.get_rect()
    GORect.midtop = (360, 220)
    playSurface.blit(GOSurf,  GORect)    
    showScore(True)
    pygame.display.flip()
    time.sleep(2)

    gameStarted = False

    # pygame.quit()
    # sys.exit()

def showScore(isGameOver = False):
    sFont = pygame.font.SysFont('monaco', 24)
    print(score)
    SSurf = sFont.render("Score: {0}".format(score), True, black)
    SRect = SSurf.get_rect()
    
    if isGameOver:
        SRect.midtop = (360, 300)
    else:
        SRect.midtop = (80, 10)

    playSurface.blit(SSurf,  SRect)
    pygame.display.flip()

def showTitleGame():
    myFont = pygame.font.SysFont('monaco', 72)
    GOSurf = myFont.render("SNAKE GAME", True, green_2)
    GORect = GOSurf.get_rect()
    GORect.midtop = (360, 100)
    playSurface.blit(GOSurf,  GORect)    

def showPauseTitle():
    myFont = pygame.font.SysFont('monaco', 36)
    GOSurf = myFont.render("Pause", True, black)
    GORect = GOSurf.get_rect()
    GORect.midtop = (360, 220)
    playSurface.blit(GOSurf,  GORect)    


def showMenu():
    global gameStarted
    gameStarted = False
    menu = True

    while menu:
        clickEventRaised = False       

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                clickEventRaised = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    gameStarted = True
                    menu = False

        playSurface.fill(white)

        showTitleGame()

        mousePos = pygame.mouse.get_pos()        

        if 310 + 100 > mousePos[0] > 310 and 250 + 50 > mousePos[1] > 250:
            pygame.draw.rect(playSurface, lightgreen, pygame.Rect(310,250,100,50))
        else:
            pygame.draw.rect(playSurface, green, pygame.Rect(310,250,100,50))

        if 310 + 100 > mousePos[0] > 310 and 320 + 50 > mousePos[1] > 320:
            pygame.draw.rect(playSurface, indianred, pygame.Rect(310,320,100,50))
        else:
            pygame.draw.rect(playSurface, red, pygame.Rect(310,320,100,50))
        
        startFont = pygame.font.SysFont('monaco', 24)
        startSurf = startFont.render("Start", True, black)
        startRect = startSurf.get_rect()
        startRect.center = ( (310+(100/2)), (250+(50/2)) )
        playSurface.blit(startSurf,  startRect)

        exitFont = pygame.font.SysFont('monaco', 24)
        exitSurf = exitFont.render("Exit", True, black)
        exitRect = exitSurf.get_rect()
        exitRect.center = ( (310+(100/2)), (320+(50/2)) )
        playSurface.blit(exitSurf,  exitRect)
        
        if clickEventRaised and 310 + 100 > mousePos[0] > 310:
            if 250 + 50 > mousePos[1] > 250:
               gameStarted = True
               menu = False

            if 320 + 50 > mousePos[1] > 320:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        fpsController.tick(15)


def runGame(): 
    global snakePos, snakeBody, foodPos, foodSpawn, direction, changeto, score
    snakePos = [100,50]
    snakeBody = [[100,50], [90,50], [80,50]]

    foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
    foodSpawn = True

    direction = 'RIGHT'
    changeto = direction

    score = 0
    isPaused = False

    # Main logic
    while gameStarted: 
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    isPaused = not isPaused
                
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

                if not isPaused: 
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        changeto = 'RIGHT'
                    if event.key == pygame.K_LEFT or event.key == ord('a'):
                        changeto = 'LEFT'
                    if event.key == pygame.K_UP or event.key == ord('w'):
                        changeto = 'UP'
                    if event.key == pygame.K_DOWN or event.key == ord('s'):
                        changeto = 'DOWN'
                
        if not isPaused: 
            # Validation of direction
            if changeto == 'RIGHT' and not direction == 'LEFT':
                direction = 'RIGHT'
            if changeto == 'LEFT' and not direction == 'RIGHT':
                direction = 'LEFT'
            if changeto == 'UP' and not direction == 'DOWN':
                direction = 'UP'
            if changeto == 'DOWN' and not direction == 'UP':
                direction = 'DOWN'

            if direction == 'RIGHT':
                snakePos[0] += 10
                
            if direction == 'LEFT':
                snakePos[0] -= 10
            
            if direction == 'UP':
                snakePos[1] -= 10
            
            if direction == 'DOWN':
                snakePos[1] += 10
            
            snakeBody.insert(0, list(snakePos))

            if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
                score += 10
                foodSpawn = False
            else:
                snakeBody.pop()

            # Food Spawn
            if not foodSpawn:
                foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
            
            foodSpawn = True

        playSurface.fill(white)

        for pos in snakeBody:
            pygame.draw.rect(playSurface, green, pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10))

        if isPaused:
            showTitleGame()
            showPauseTitle()

        isGameOver = False

        if snakePos[0] > 710 or snakePos[0] < 0:
            isGameOver = True
        
        if snakePos[1] > 450 or snakePos[1] < 0:
            isGameOver = True
        # print(snakeBody)
        # print(snakeBody[1:])
        for block in snakeBody[1:]:
            # print("block: {0}".format(block))
            # print("snakePos {0}".format(snakePos))
            if snakePos[0] == block[0] and snakePos[1] == block[1]:
                isGameOver = True

        if isGameOver:
            gameOver()
        else:
            showScore()
        

        pygame.display.flip()
        
        fpsController.tick(15)

    # Challenge
    """
    Put a Menu(Start, help, pause)        
    Add sounds
    Add Setting(Set colors, enable setting, dificult)
    Instead rectangulo add image
    Set Icon of image
    create executable(pyinstaller)
    https://pythonprogramming.net/placing-text-pygame-buttons/?completed=/making-interactive-pygame-buttons/
    """

while True:
    showMenu()
    runGame()