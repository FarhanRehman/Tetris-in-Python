from Block_farhan import Block
import pygame
from gameboard_farhan import gameboard_width
from gameboard_farhan import gameboard_height
from gameboard_farhan import activeBoardSpot
from gameboard_farhan import activeBoardColour
import random

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
PINK = (255, 0, 127)
BLACK = (0, 0, 0)



S_Shape =[[gameboard_width/2, 0], [gameboard_width/2 +1, 0], [gameboard_width/2 -1, 1], [gameboard_width/2, 1]]
Z_Shape = [[(gameboard_width/2), 0], [(gameboard_width/2)-1, 0], [(gameboard_width/2),1], [(gameboard_width/2)+1,1]]
L_Shape = [[gameboard_width/2,1], [gameboard_width/2,0], [gameboard_width/2,2], [gameboard_width/2 + 1, 2]]
ML_Shape = [[gameboard_width/2,1], [gameboard_width/2,0], [gameboard_width/2, 2], [gameboard_width/2- 1, 2]]
SQ_Shape =[[gameboard_width/2,0], [gameboard_width/2 - 1, 0], [gameboard_width/2, 1], [gameboard_width/2 -1, 1]]
LINE_Shape =[[gameboard_width/2,1], [gameboard_width/2,0], [gameboard_width/2,2], [gameboard_width/2,3]]
T_Shape = [[gameboard_width/2, 0], [gameboard_width/2 -1 , 0], [gameboard_width/2 + 1, 0], [gameboard_width/2, 1]]

All_Shapes = [S_Shape, Z_Shape, L_Shape, ML_Shape, SQ_Shape, LINE_Shape, T_Shape]
Colour = [RED, GREEN, BLUE, ORANGE, YELLOW, PINK]
class Shape():
    def __init__(self):
        randColour = random.randrange(6)
        self.colour = Colour[randColour]
        RandNum = random.randrange(7)
        self.Shape = All_Shapes[RandNum]
        self.numblocks = 4
        self.blocklist = []
        self.active = True
        for i in range(self.numblocks):
            self.blocklist.append(Block(self.colour, self.Shape[i][0], self.Shape[i][1]))

    def draw(self, screen):
        for i in range(self.numblocks):
            self.blocklist[i].draw(screen)

    def MoveLeft(self):
        blocked = False
        for i in range(self.numblocks):
            if self.blocklist[i].gridx <= 0 or activeBoardSpot[self.blocklist[i].gridx - 1][self.blocklist[i].gridy]:
                blocked = True
        if blocked == False:
            for i in range(self.numblocks):
                self.blocklist[i].gridx -= 1

    def MoveRight(self):
        blocked = False
        for i in range(self.numblocks):
            if self.blocklist[i].gridx >= gameboard_width - 1 or activeBoardSpot[self.blocklist[i].gridx + 1][self.blocklist[i].gridy]:
                blocked = True
        if blocked == False:
            for i in range(self.numblocks):
                self.blocklist[i].gridx += 1

    def MoveDown(self):
        blocked = False
        for i in range(self.numblocks):
            if int(self.blocklist[i].gridy) >= gameboard_height - 1 or activeBoardSpot[int(self.blocklist[i].gridx)][int(self.blocklist[i].gridy) +1]:
                blocked = True
        if blocked == False:
            for i in range(self.numblocks):
                self.blocklist[i].gridy += 1


    def RotateCW(self):
        block1X = self.blocklist[0].gridx
        block1Y= self.blocklist[0].gridy
        block2X = self.blocklist[1].gridx
        block2Y = self.blocklist[1].gridy
        block3X = self.blocklist[2].gridx
        block3Y = self.blocklist[2].gridy
        block4X = self.blocklist[3].gridx
        block4Y = self.blocklist[3].gridy

        if self.Shape != SQ_Shape:
            # moving shape to coordinates(0,0)
            for i in range(self.numblocks):
                self.blocklist[i].gridx -= block1X  # X coordinate for center block
                self.blocklist[i].gridy -= block1Y  # Y coordinate for center block
            # Rotating
            for i in range(self.numblocks):
                oldx = self.blocklist[i].gridx
                oldy = self.blocklist[i].gridy

                self.blocklist[i].gridy = oldx
                self.blocklist[i].gridx = -oldy
            # Moving shape back to previous coordinates
            for i in range(self.numblocks):
                self.blocklist[i].gridy += block1Y
                self.blocklist[i].gridx += block1X

            XPositions = [block1X, block2X, block3X, block4X]
            YPositions = [block1Y, block2Y, block3Y, block4Y]
            canRotate = True

            # Boundraies
            for i in range(self.numblocks):
                if self.blocklist[i].gridx < 0 or self.blocklist[i].gridx >= gameboard_width - 1:
                    canRotate = False
                elif self.blocklist[i].gridy < 0 or self.blocklist[i].gridy >= gameboard_height - 1:
                    canRotate = False
                elif activeBoardSpot[self.blocklist[i].gridx][self.blocklist[i].gridy]:
                    canRotate = False
            # if shape is out of boundraies, reset
            if canRotate == False:
                for i in range(self.numblocks):
                    self.blocklist[i].gridx = XPositions[i]
                    self.blocklist[i].gridy = YPositions[i]


    def RotateCCW(self):
        block1X = self.blocklist[0].gridx
        block1Y= self.blocklist[0].gridy
        block2X = self.blocklist[1].gridx
        block2Y = self.blocklist[1].gridy
        block3X = self.blocklist[2].gridx
        block3Y = self.blocklist[2].gridy
        block4X = self.blocklist[3].gridx
        block4Y = self.blocklist[3].gridy

        if self.Shape != SQ_Shape:
            # moving shape to coordinates(0,0)
            for i in range(self.numblocks):
                self.blocklist[i].gridx -= block1X# X coordinate for center block
                self.blocklist[i].gridy -= block1Y# Y coordinate for center block
            # Rotating
            for i in range(self.numblocks):
                oldx = self.blocklist[i].gridx
                oldy = self.blocklist[i].gridy

                self.blocklist[i].gridy = -oldx
                self.blocklist[i].gridx = oldy
            # Moving shape back to previous coordinates
            for i in range(self.numblocks):
                self.blocklist[i].gridy += block1Y
                self.blocklist[i].gridx += block1X

            XPositions = [block1X, block2X, block3X, block4X]
            YPositions = [block1Y, block2Y, block3Y, block4Y]
            canRotateCCW = True

            # Boundraies

            for i in range(self.numblocks):
                if self.blocklist[i].gridx < 0 or self.blocklist[i].gridx >= gameboard_width - 1:
                    canRotateCCW = False
                elif self.blocklist[i].gridy < 0 or self.blocklist[i].gridy >= gameboard_height - 1:
                    canRotateCCW = False
                elif activeBoardSpot[self.blocklist[i].gridx][self.blocklist[i].gridy]:
                    canRotateCCW = False

            # if shape is out of boundraies, reset
            if canRotateCCW == False:
                for i in range(self.numblocks):
                    self.blocklist[i].gridx = XPositions[i]
                    self.blocklist[i].gridy = YPositions[i]

    def hitbottom(self):
        for i in range(self.numblocks):
            activeBoardSpot[self.blocklist[i].gridx][self.blocklist[i].gridy] = True
            activeBoardColour[self.blocklist[i].gridx][self.blocklist[i].gridy] = self.colour
        self.active = False



    def falling(self):
        for i in range(4):
            if int(self.blocklist[i].gridy) == gameboard_height -1 or activeBoardSpot[int(self.blocklist[i].gridx)][int(self.blocklist[i].gridy) + 1] == True:
                self.hitbottom()
        if self.active == True:
            for i in range(4):
                self.blocklist[i].gridy += 1

    def fall(self):
        while self.active:
            for i in range(self.numblocks):
                if self.blocklist[i].gridy >= gameboard_height - 1 or activeBoardSpot[self.blocklist[i].gridx][self.blocklist[i].gridy + 1]:
                    self.hitbottom()
            if self.active:
                for i in range(self.numblocks):
                    self.blocklist[i].gridy += 1

    def drawNewShape(self,screen):
        xpos = [0, 0, 0, 0]
        ypos = [0, 0, 0, 0]
        for i in range(self.numblocks):
            xpos[i] = self.Shape[i][0] * self.blocklist[i].size
            ypos[i] = self.Shape[i][1] * self.blocklist[i].size
        for i in range(4):
            xpos[i] += 255
            ypos[i] += 145
        for i in range(4):
            pygame.draw.rect(screen, self.colour, [xpos[i], ypos[i], self.blocklist[i].size - 1, self.blocklist[i].size - 1], 0)


    def drawShadow(self, screen):
        updatePattern = True
        xPos = [0, 0, 0, 0]
        yPos = [0, 0, 0, 0]
        for i in range(self.numblocks):
            xPos[i] = int(self.blocklist[i].gridx)
            yPos[i] = int(self.blocklist[i].gridy)

        while updatePattern:

            for i in range(4):
                if yPos[i] == gameboard_height - 1 or activeBoardSpot[xPos[i]][yPos[i] + 1]:
                    updatePattern = False

            for i in range(4):
                if updatePattern:
                    yPos[i] += 1


        for i in range(self.numblocks):
            pygame.draw.rect(screen,BLUE, [xPos[i] * self.blocklist[i].size, yPos[i] * self.blocklist[i].size, self.blocklist[i].size - 1, self.blocklist[i].size -1], 1)

    def drawholdshape(self, screen):
        xpos = [0, 0, 0, 0]
        ypos = [0, 0, 0, 0]
        for i in range(self.numblocks):
            xpos[i] = self.Shape[i][0] * self.blocklist[i].size
            ypos[i] = self.Shape[i][1] * self.blocklist[i].size
        for i in range(4):
            xpos[i] += 515
            ypos[i] += 350
        for i in range(4):
            pygame.draw.rect(screen, self.colour, [xpos[i], ypos[i], self.blocklist[i].size - 1, self.blocklist[i].size - 1],0)


    def reposition(self):
        for i in range(self.numblocks):
            self.blocklist[i].gridx = int(self.Shape[i][0])
            self.blocklist[i].gridy = int(self.Shape[i][1])