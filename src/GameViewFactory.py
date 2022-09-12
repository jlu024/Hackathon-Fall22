import pygame
import random
from src.GameBoard import GameBoard

# import RegularLevelFunctions as regLelFunc
# import FruitLevelFunctions as fruitLelFunc
from src.config import CONFIG_DATA


class GameView:
    """
    constructor Inputs:
        levelType: "Regular" or "Fruit"
        levelNum: integer greater than 0
    """

    def __init__(self, levelType, levelNum, screen):
        self.levelType = levelType
        self.levelNum = levelNum
        configDataKey = levelType + "-" + str(levelNum)
        self.levelConfigData = CONFIG_DATA[configDataKey]

        # level configuration
        self.candyFreqDict = self.levelConfigData['candyFreq']
        #self.fruitCount = self.levelConfigData['completionCriteria']
        self.completionCriteria = self.levelConfigData['completionCriteria']
        self.turnsRemaining = self.levelConfigData['turns']
        self.gameBoardSize = self.levelConfigData['boardSize']
        self.board = GameBoard(self.gameBoardSize, self.candyFreqDict, self.completionCriteria)

        # print("GenerateGameView: __init__")
        # print("candyFreqDict", self.candyFreqDict)
        # print("fruitCount", self.fruitCount)
        # print("turnsRemaining", self.turnsRemaining)

        self.IMAGES = {}
        self.BACKGROUNDIMAGE = None

        w, h = pygame.display.get_surface().get_size()
        self.SQ_SIZE_H = h // self.gameBoardSize[0]
        self.SQ_SIZE_W = int(w // self.gameBoardSize[1] // (1.3))
        self.screen = screen
        print(pygame.display.get_surface().get_size())
        print("(", self.SQ_SIZE_H, ",", self.SQ_SIZE_W, ")")

        # prepping images
        self.loadImages()
        self.drawGameState()
        return

    def loadImages(self):
        pieces = self.candyFreqDict.keys()

        self.BACKGROUNDIMAGE = pygame.transform.scale(pygame.image.load("images/candyWallBackground.png"),
                                                      (pygame.display.get_surface().get_size()))

        # Mapping each candy piece with its data path graphics path value
        for piece in pieces:
            # r_image = random.choice(pieces)
            self.IMAGES[piece] = pygame.transform. \
                scale(pygame.image.load("images/" + piece + ".png"),
                      (self.SQ_SIZE_W, self.SQ_SIZE_H)).convert_alpha()
            # IMAGES[piece] = p.transform.scale(p.image.load("images/" + r_image + ".png"), (SQ_SIZE, SQ_SIZE))
        return

    def runGame(self):
        running = True
        sqSelected = ()  # track last click of the user (row, col)
        playerClicks = []  # tracks player clicks [(row1,col1)(row2,col2)]
        while running:

            # Game Events
            for event in pygame.event.get():
                # Default event.type to exit game by closing window
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # ensures only left click
                        location = pygame.mouse.get_pos()  # x,y coordinate get integers
                        # truncate the location coordinate as integers
                        col = location[0] // self.SQ_SIZE_H
                        row = location[1] // self.SQ_SIZE_W
                        if col >= self.gameBoardSize[1] or row >= self.gameBoardSize[0]:
                            continue

                        print(location)  # test to see mouse click coordinates
                        print(row, col)

                        if sqSelected == (row, col):  # deselect motion reclick on it
                            sqSelected = ()
                            playerClicks = []

                        else:
                            sqSelected = (row, col)
                            playerClicks.append(sqSelected)  # keep record of clicks

                        if len(playerClicks) == 2:
                            # engine move the first piece, to second piece location on board
                            # second piece gets nonexistant
                            print("playerClicks[0]", playerClicks[0],
                                  self.board.board[playerClicks[0][0]][playerClicks[0][1]])
                            print("playerClicks[1]", playerClicks[1],
                                  self.board.board[playerClicks[1][0]][playerClicks[1][1]])
                            self.board.makeMove(playerClicks[0], playerClicks[1])
                            ##ADDED JENN
                            if self.board.makeMove(playerClicks[0], playerClicks[1]):
                                self.turnsRemaining -= 1

                                if self.turnsRemaining == 0 or self.board.checkCompletionCriteria():
                                    running = False
                                    break #bring up game over ####
                            # resetting the first move
                            sqSelected = ()
                            playerClicks = []


                    self.drawGameState()
        #call end screen win or lose
        self.handleGameEnd()

    def drawGameState(self):
        # self.drawBoard(self.screen)
        self.drawPieces(self.screen)
        ##Jenn ADDED
        score_textX = 635  # left
        score_textY = 125  # top
        self.show_score(self.screen, score_textX, score_textY)

        turn_textX = 635
        turn_textY = 365 #+15 difference from box
        self.show_turn(self.screen, turn_textX, turn_textY) ##END

        pygame.display.flip()

    def drawBoard(self, screen):
        colors = [pygame.Color("gray"), pygame.Color("red")]
        # TODO: update from config file
        for r in range(self.gameBoardSize[0]):
            for c in range(self.gameBoardSize[1]):
                color = colors[((r + c) % 2)]
                pygame.draw.rect(screen, color,
                                 pygame.Rect(c * self.SQ_SIZE_H, r * self.SQ_SIZE_W,
                                             self.SQ_SIZE_H, self.SQ_SIZE_W))
        return

    def drawPieces(self, screen):
        print(pygame.display.get_surface().get_size())
        screen.blit(self.BACKGROUNDIMAGE,
                    pygame.Rect((0, 0), (pygame.display.get_surface().get_size())))

        for r in range(self.gameBoardSize[0]):
            for c in range(self.gameBoardSize[1]):
                piece = self.board.board[r][c]
                if piece != "--":
                    screen.blit(self.IMAGES[piece],
                                pygame.Rect((c * self.SQ_SIZE_W, r * self.SQ_SIZE_H),
                                            (self.SQ_SIZE_W, self.SQ_SIZE_H)))

        #Jenn added score section box section/background pink
        score_bg = pygame.rect.Rect(625, 110, 170, 200) #col, row, size w x h
        pygame.draw.rect(screen, (255, 111, 255), score_bg)
        #Jenn added turn section box turquise
        turn_bg = pygame.rect.Rect(625, 350, 170, 200)
        pygame.draw.rect(screen, (0, 255, 255), turn_bg)

        return

    #Jenn added

    def show_score(self, screen, x, y):
        font = pygame.font.Font("freesansbold.ttf", 28)
        score = font.render("SCORE: " + str(self.turnsRemaining), True, (255,255,255)) #show text, put on screen, text color
        screen.blit(score, (x, y))

    def show_turn(self, screen, x, y):
        font = pygame.font.Font("freesansbold.ttf", 28)
        score = font.render("TURNS: " + str(self.turnsRemaining), True, (255,255,255)) #show text, put on screen, text color
        screen.blit(score, (x, y))

    #suggested by Pranith not sure how to incorporate
    def checkCompletionCriteria(self):
        #if True: self.displayEndingScreen else: return False
        pass

    def handleGameEnd(self):
        if (self.turnsRemaining == 0):
            self.displayGameFail()

        if (self.board.checkCompletionCritiera()):
            self.displayGameWin()

    def displayGameEnd(self, prompt):
        print(pygame.display.get_surface().get_size())
        self.screen.blit(self.BACKGROUNDIMAGE,
                         pygame.Rect((0, 0), (pygame.display.get_surface().get_size())))

        screenSize = pygame.display.get_surface().get_size()
        fullScreen = pygame.display.get_surface().get_size()
        screenSize[0] = screenSize[0] * 0.4
        screenSize[1] = screenSize[1] * 0.4
        pygame.draw.rect(self.screen, pygame.Color("gray"),
                         pygame.Rect(0.3 * fullScreen[0], 0.3 * fullScreen[1],
                                     screenSize[0], screenSize[1]))

    # def displayGameWin(self):
    #     pass