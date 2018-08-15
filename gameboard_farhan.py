import pygame
import random
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
PINK = (255, 0, 127)

AllColours = [RED, GREEN, BLUE, ORANGE, YELLOW, PINK, BLACK, WHITE]
pygame.init()
linesound = pygame.mixer.Sound('clearline.wav')
gameboard_width = 12
gameboard_height = 20
activeBoardSpot = [[0 for y in range(gameboard_height)] for x in range(gameboard_width)]
activeBoardColour = [[0 for y in range(gameboard_height)] for x in range(gameboard_width)]

class Gameboard():
    def __init__(self, colour, blocksize):
        self.colour = colour
        self.multiplier = blocksize
        self.score = 0
        self.lines = 0
        self.tempTracker = 0
        self.levelTracker = 1
        self.numslowtime = 0
        self.numslowtimeon = False
        self.numswap = 0
        self.swapshape = False
        self.linescounter = 0
        self.shakescreen = False
        for i in range(gameboard_width):
            for j in range(gameboard_height):
                activeBoardSpot[i][j] = False
                activeBoardColour[i][j] = BLACK

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, [0, 0, gameboard_width * self.multiplier, gameboard_height * self.multiplier], 0)
        for i in range(gameboard_width):
            for j in range(gameboard_height):
                if activeBoardSpot[i][j]:
                    pygame.draw.rect(screen, activeBoardColour[i][j], [i * self.multiplier, j * self.multiplier, self.multiplier -1, self.multiplier -1], 0)



    def checkLoss(self):
        for i in range(gameboard_width):
            if activeBoardSpot[i][0]:
                return True
        return False

    def isCompleteLine(self, rownum):
        for i in range(gameboard_width):
            if activeBoardSpot[i][rownum] == False:
                return False
        return True
    def drawshake(self, screen):
        normalwidth = gameboard_width * self.multiplier
        normalheight = gameboard_height * self.multiplier
        shakeamount = 10
        shakecounter = 0
        while self.shakescreen:
            pygame.draw.rect(screen, WHITE,[0, 0, normalwidth+ shakeamount, normalheight + shakeamount], 5)
            for i in range(gameboard_width):
                for j in range(gameboard_height):
                    Colour = AllColours[random.randrange(7)]
                    pygame.draw.rect(screen, Colour, [i * self.multiplier, j *self.multiplier, self.multiplier -1, self.multiplier -1], 0)
            pygame.display.flip()
            if shakeamount%5 == 0:
                if shakeamount == 10:
                    shakeamount = -shakeamount

            if shakecounter > 100:
                self.shakescreen = False

            shakecounter += 1


    def clearLine(self):
        for j in range(gameboard_height):
            if self.isCompleteLine(j): # is a row is complete
                self.linescounter += 1
                linesound.play()
                self.lines += 1
                self.tempTracker += 1
                if self.tempTracker == 5:
                    self.numswap += 1
                if self.tempTracker%4 == 0:
                    self.shakescreen = True
                if self.tempTracker == 10:
                    self.numswap += 1
                    self.levelTracker += 1
                    self.numslowtime += 1
                    self.tempTracker = 0
                for c in range(j, 1, -1):
                    for i in range(gameboard_width): # giving current fow the same value as above
                        activeBoardSpot[i][c] = activeBoardSpot[i][c - 1]
                        activeBoardColour[i][c] = activeBoardColour[i][c -1]
                for r in range(gameboard_width):
                    activeBoardSpot[r][0] = False
                    activeBoardColour[r][0] = BLACK
        if self.isCompleteLine:
            if self.linescounter == 1:
                self.score += 50
                self.linescounter = 0
            elif self.linescounter == 2:
                self.score += 100
                self.linescounter = 0
            elif self.linescounter == 3:
                self.score += 150
                self.linescounter = 0
            elif self.linescounter == 4:
                self.score += 200
                self.linescounter = 0

