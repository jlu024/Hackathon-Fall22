import random


class GameBoard:

    def __init__(self, size, candyFreq):
        self.boardSize = size
        self.candyGenArray = []
        #generating an array of candy Strings that has frequency to match candyFreq
        for (key, value) in candyFreq.items():
            for i in range(value):
                self.candyGenArray.append(key)

        self.board = []
        self.generateInitialBoard()
        self.randomizeBoard()



    def generateInitialBoard(self):
        for x in range(self.boardSize[0]+1):
            curList = []
            for y in range(self.boardSize[1]+1):
                curList.append("--")
            self.board.append(curList)
        return

    def randomizeBoard(self):
        candies = ["candy", "candy2"] # TODO: need to connect to candyFreqDict

        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == "--":
                    self.board[x][y] = random.choice(self.candyGenArray)
        return

    def makeMove(self, initialPos, finalPos):
        """

        :param initialPos: [x, y] for initial grid position
        :param finalPos: [x, y] for final grid position
        :return: ( acceptable move{true/false} )
        """
        if (not self.isValidMove(initialPos, finalPos)):
            return False
        self.swapPieces(initialPos, finalPos)
        return True





    def isValidMove(self, initialPos, finalPos):
        """
        checks if it is a valid move
        :param initialPos: [x, y] for initial grid position
        :param finalPos: [x, y] for final grid position
        :return: True or False
        """
        [iPosX, iPosY] = initialPos
        [fPosX, fPosY] = finalPos

        if (abs(iPosX - fPosX) > 1):
            return False

        if (abs(iPosY - fPosY) > 1):
            return False

        if (iPosX - fPosX == 1):
            direction = "vertical"
        else:
            direction = "horizontal"

        # TODO: need to complete this function. Are we checking if pieces should be removed here?
        return True


    def swapPieces(self, initialPos, finalPos):
        [iPosX, iPosY] = initialPos
        [fPosX, fPosY] = finalPos



        initialPiece = self.board[iPosX][iPosY]
        finalPiece = self.board[fPosX][fPosY]
        self.board[iPosX][iPosY] = finalPiece
        self.board[fPosX][fPosY] = initialPiece
        return
