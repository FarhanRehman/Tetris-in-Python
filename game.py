# getting function from library
import pygame
import time
from Block_farhan import Block
from shape_farhan import Shape
from gameboard_farhan import *
import sys

# colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
PINK = (255, 0, 127)


if __name__ == "__main__":
# initalize the game engine
    pygame.init()
    started = False
    # playing music
    pygame.mixer.init()
    pygame.mixer.music.load('AvalancheBGM.mp3')
    pygame.mixer.music.play(-1)
# making window
    size = (800, 600)
    screen = pygame.display.set_mode(size)
# setting caption
    pygame.display.set_caption('Avalanche')
    shape = Shape()
    nextshape = Shape()
    gameboard = Gameboard(WHITE, 25)
    done = False
    delay = 0
    score = 0
    myfont = pygame.font.SysFont('Gravity', 20)
    myfont1 = pygame.font.SysFont('Gravity', 35)
    myfont3 = pygame.font.SysFont('Gravity', 100)
    slowtimedelay = 0
    leftKey = False
    rightKey = False
    downKey = False
    name = ""
    namelist = [0 for i in range(5)]
    scorelist = [0 for y in range(5)]
    HSFile = open("highscores.txt", "r")
    for i in range(5):
        namelist[i] = HSFile.readline().rstrip("\n")
    for y in range(5):
        scorelist[y] = HSFile.readline().rstrip('\n')
    HSFile.close()
    paused = False
    holding = False
    changehold = False
    holdshape = None



def checkhighscores():
    newHS = False
    tempnamelist = [0 for y in range(5)]
    tempscorelist = [0 for y in range(5)]
    for i in range(5):
        if gameboard.score > int(scorelist[i]) and newHS == False:
            newHS = True
            tempscorelist[i] = gameboard.score
            tempnamelist[i] = name
        elif newHS == True:
            tempscorelist[i] = scorelist[i -1]
            tempnamelist[i] = namelist[i -1]
        else:
            tempscorelist[i] = scorelist[i]
            tempnamelist[i] = namelist[i]

    for i in range(5):
        scorelist[i] = tempscorelist[i]
        namelist[i] = tempnamelist[i]

    HSFile = open("highscores.txt", "w")

    for i in range(5):
        HSFile.write(str(namelist[i]) + "\n")
    for i in range(5):
        HSFile.write(str(scorelist[i]) + "\n")
    HSFile.close()

def Drawscreen():
    screen.fill(BLACK)

    if gameboard.shakescreen:
        gameboard.drawshake(screen)
    else:
        gameboard.draw(screen)

    shape.drawShadow(screen)
    shape.draw(screen)

    scoreText = myfont.render('S C O R E : ' + str(gameboard.score), True, PINK)
    screen.blit(scoreText, (330, 400))
    linesText = myfont.render('L I N E S : ' + str(gameboard.lines), True, PINK)
    screen.blit(linesText, (330, 350))
    LevelText = myfont.render('L E V E L : ' + str(gameboard.levelTracker), True, PINK)
    screen.blit(LevelText, (330, 300))
    nextshapetext = myfont.render('N E X T : ', True, PINK)
    pygame.draw.rect(screen, WHITE, [330, 100, 6 * shape.blocklist[0].size, 6 * shape.blocklist[0].size], 1)
    screen.blit(nextshapetext, (330, 50))
    nextshape.drawNewShape(screen)
    poweruptext = myfont.render("P O W E R U P S : ", True, PINK)
    screen.blit(poweruptext, (50, 525))
    numslowtimestext = myfont.render(" X   " + str(gameboard.numslowtime), True, PINK)
    screen.blit(numslowtimestext, (310, 525))
    slowtime_image = pygame.image.load('clock.png')
    screen.blit(slowtime_image, (250, 515))
    numswaptext = myfont.render('   X ' + str(gameboard.numswap), True, PINK)
    screen.blit(numswaptext, (435, 525))
    swap_image = pygame.image.load("swap.png")
    screen.blit(swap_image, (375, 515))
    highscoretext = myfont.render("H I G H S C O R E S : ", True, PINK)
    screen.blit(highscoretext, (575, 50))
    pygame.draw.rect(screen, WHITE, [575, 100, 200, 400], True)
    playernametext = myfont1.render(name, True, PINK)
    screen.blit(playernametext,(600, 525))
    for i in range(5):
        highscoreplayertext = myfont.render(str(namelist[i]) + "        " + str(scorelist[i]), True, PINK)
        screen.blit(highscoreplayertext, (600, 100 + 30 * i))
    if holding:
        hshtext = myfont.render("H E L D : ", True, WHITE)
        screen.blit(hshtext, (580, 275))
        pygame.draw.rect(screen, WHITE, [600,325, shape.blocklist[0].size * 5, shape.blocklist[0].size * 5], 1)
        holdshape.drawholdshape(screen)
    pygame.display.flip()

def keypressed():
    if event.key == pygame.K_LEFT:
        global leftKey
        leftKey = True
    elif event.key == pygame.K_RIGHT:
        global rightKey
        rightKey = True
    elif event.key == ord('d'):
        global downKey
        downKey = True
    elif event.key == pygame.K_UP or event.key == ord('w'):
        shape.RotateCW()
    elif event.key == pygame.K_DOWN or event.key == ord('s'):
        shape.RotateCCW()
    elif event.key == pygame.K_SPACE:
        gameboard.score += (gameboard_height - shape.blocklist[0].gridy)
        shape.fall()
    elif event.key == ord('t') and gameboard.numslowtime > 0:
        gameboard.numslowtimeon = True
        gameboard.numslowtime -= 1
    elif event.key == ord('f') and gameboard.numswap > 0:
        gameboard.swapshape = True
        gameboard.numswap -= 1
    elif event.key == ord('p'):
        global paused
        paused = True
    elif event.key == ord('p'):
        paused = False




def keyReleased():
    if event.key == pygame.K_LEFT:
        global leftKey
        leftKey = False
    elif event.key == pygame.K_RIGHT:
        global rightKey
        rightKey = False
    elif event.key == pygame.K_d:
        global downKey
        downKey = False
    elif event.key == ord('h'):
        global changehold
        changehold = True


def keycheck():
    if leftKey:
        shape.MoveLeft()
    if rightKey:
        shape.MoveRight()
    if downKey:
        shape.MoveDown()




while not started:  # Title screen
    titlescreen = pygame.image.load('Backdrop.png')
    enternametext = myfont.render("E N T E R  Y O U R  N A M E : ", True, WHITE)
    nametext = myfont.render(name, True, WHITE)
    screen.blit(titlescreen, (0, 0))
    screen.blit(enternametext, (275, 201))
    screen.blit(nametext, (300, 250))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            started = True
        if event.type == pygame.KEYDOWN:
            if event.key >= 33 and event.key <= 126 and len(name) < 10:
                name += chr(event.key)
            if event.key == pygame.K_BACKSPACE:
                name = name[: - 1]
            if event.key == pygame.K_RETURN:
                if name == "":
                    name = "Player"
                started = True



# quit function
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            keypressed()
        elif event.type == pygame.KEYUP:
            keyReleased()

    keycheck()

    if gameboard.swapshape:
        shape = nextshape
        nextshape = Shape()
        gameboard.swapshape = False
    if gameboard.numslowtimeon:
        slowtimedelay += 1
        if slowtimedelay > 100:
            slowtimeelay = 0
            slowtimeon = False

    delay += 1
    if delay > 10:
        shape.falling()
        delay = 0
    if shape.active == False:
        shape = nextshape
        nextshape = Shape()
        gameboard.clearLine()

    Drawscreen()
    time.sleep(0.11 - gameboard.levelTracker * 0.02 + gameboard.numslowtimeon * 0.1)
    if changehold:
        changehold = False
        if holding:
            nextshape = shape
            holdshape.reposition()
            shape = holdshape
            holdshape = None
            holding = False
        else:
            holdshape = shape
            shape = nextshape
            nextshape = Shape()
            holding = True



    while paused:
        pausedscreen = myfont3.render("P A U S E D ", True, PINK)
        screen.blit(pausedscreen, (200, 200))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False
                done = False
            if event.type == pygame.KEYDOWN:
                if event.key == ord('p'):
                    paused = False




    if gameboard.checkLoss():
        checkhighscores()
        gameboard = Gameboard(WHITE, 25)
        shape = Shape
        continueGame = True
        while continueGame == True:
            endscreen = pygame.image.load('endscreen.png')
            endscreen = pygame.transform.scale(endscreen, (800, 600))
            scoretext = myfont.render(str(name) + '  l o s t ,  y o u r  s c o r e  w a s  ' + str(score), True, BLACK)
            screen.blit(endscreen, (0, 0))
            screen.blit(scoretext, (0, 550))
            quitend = myfont.render('P R E S S  Q  T O  Q UI T ', True, BLACK)
            playagaintext = myfont.render('P R E S S  E N T E R  T O  P L A Y  A G A I N', True, BLACK)
            screen.blit(playagaintext,(400, 0 ))
            screen.blit(quitend, (0, 0))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    continueGame = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameboard = Gameboard(WHITE, 25)
                        shape = Shape()
                        nextshape = Shape()
                        holdshape = None
                        continueGame = False
                    if event.key == ord('q'):
                        done = True
                        continueGame= False











