import pygame
import random
from src.GameBoard import GameBoard
import pygame_menu

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
        # self.fruitCount = self.levelConfigData['completionCriteria']
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
        # print(pygame.display.get_surface().get_size())
        # print("(", self.SQ_SIZE_H, ",", self.SQ_SIZE_W, ")")

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

                        # print(location)  # test to see mouse click coordinates
                        # print(row, col)

                        if sqSelected == (row, col):  # deselect motion reclick on it
                            sqSelected = ()
                            playerClicks = []

                        else:
                            sqSelected = (row, col)
                            playerClicks.append(sqSelected)  # keep record of clicks

                        if len(playerClicks) == 2:
                            self.board.makeMove(playerClicks[0], playerClicks[1])
                            ##ADDED JENN
                            if self.board.makeMove(playerClicks[0], playerClicks[1]):
                                self.turnsRemaining -= 1

                                if self.turnsRemaining == 0 or self.board.checkCompletionCriteria():
                                    running = False
                                    break  # bring up game over ####
                            # resetting the first move
                            sqSelected = ()
                            playerClicks = []

                    self.drawGameState()
        # call end screen win or lose
        self.handleGameEnd()
        return

    def drawGameState(self):
        # self.drawBoard(self.screen)
        self.drawPieces(self.screen)
        score_textX = 635  # left
        score_textY = 15  # top
        self.show_score(score_textX, score_textY)

        turn_textX = 635
        turn_textY = 480  # +15 difference from box
        self.show_turn(self.screen, turn_textX, turn_textY)

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
        # print(pygame.display.get_surface().get_size())
        screen.blit(self.BACKGROUNDIMAGE,
                    pygame.Rect((0, 0), (pygame.display.get_surface().get_size())))

        for r in range(self.gameBoardSize[0]):
            for c in range(self.gameBoardSize[1]):
                piece = self.board.board[r][c]
                if piece != "--":
                    screen.blit(self.IMAGES[piece],
                                pygame.Rect((c * self.SQ_SIZE_W, r * self.SQ_SIZE_H),
                                            (self.SQ_SIZE_W, self.SQ_SIZE_H)))

        # Jenn added score section box section/background pink
        score_bg = pygame.rect.Rect(625, 5, 170, 60)  # col, row, size w x h
        pygame.draw.rect(screen, (255, 111, 255), score_bg)

        turn_bg = pygame.rect.Rect(625, 470, 170, 100)
        pygame.draw.rect(screen, (0, 255, 255), turn_bg)

        return

    def show_score(self, x, y):
        print(pygame.font.get_fonts())
        font = pygame.font.Font("freesansbold.ttf", 28)
        score = font.render("SCORE: " + str(self.board.score), True,
                            (255, 255, 255))  # show text, put on screen, text color
        self.screen.blit(score, (x, y + 10))

    def show_turn(self, screen, x, y):
        font = pygame.font.Font("freesansbold.ttf", 28)
        score = font.render("TURNS: " + str(self.turnsRemaining), True,
                            (255, 255, 255))  # show text, put on screen, text color
        screen.blit(score, (x, y))
        goal = font.render("GOAL: " + str(self.board.criteria), True, (255, 255, 255))
        screen.blit(goal, (x, y + 50))

    def handleGameEnd(self):
        if (self.turnsRemaining == 0):
            self.displayGameEnd("Failure")

        if (self.board.checkCompletionCriteria()):
            self.displayGameEnd("Success")

        return

    def displayGameEnd(self, prompt):
        screenSize = pygame.display.get_surface().get_size()
        fullScreen = pygame.display.get_surface().get_size()

        screenSizeX = int(screenSize[0] * 0.4)
        screenSizeY = int(screenSize[1] * 0.4)

        splashRect = pygame.draw.rect(self.screen, (255, 51, 204),
                                      pygame.Rect(int(0.3 * fullScreen[0]), int(0.3 * fullScreen[1]),
                                                  screenSizeX, screenSizeY))

        font = pygame.font.Font("freesansbold.ttf", 28)
        score = font.render("Final Score: " + str(self.board.score), True,
                            (255, 255, 255))  # show text, put on screen, text color
        self.screen.blit(score, (int(fullScreen[0] / 2 - 80), int(fullScreen[1] / 2 - 30)))
        font = pygame.font.Font("freesansbold.ttf", 28)
        finalString = font.render(prompt, True, (0, 0, 0))  # show text, put on screen, text color
        self.screen.blit(finalString, splashRect)
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return
