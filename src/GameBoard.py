import random


class GameBoard:

    def __init__(self, size, candyFreq, criteria):
        self.boardSize = size
        self.candyGenArray = []
        #generating an array of candy Strings that has frequency to match candyFreq
        for (key, value) in candyFreq.items():
            for i in range(value):
                self.candyGenArray.append(key)

        self.criteria = criteria
        self.candyNameArray = [x for x in candyFreq.keys()]
        self.board = []
        self.generateInitialBoard()
        self.randomizeBoard()
        self.checkBoard()



    def generateInitialBoard(self):
        for x in range(self.boardSize[0]):
            curList = []
            for y in range(self.boardSize[1]):
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
        self.checkBoard()
        self.checkCompletionCriteria()

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

        if (abs(iPosX - fPosX) +abs(iPosY - fPosY) > 1):
            return False
        return True


    def swapPieces(self, initialPos, finalPos):
        [iPosX, iPosY] = initialPos
        [fPosX, fPosY] = finalPos



        initialPiece = self.board[iPosX][iPosY]
        finalPiece = self.board[fPosX][fPosY]
        self.board[iPosX][iPosY] = finalPiece
        self.board[fPosX][fPosY] = initialPiece
        return




    def checkBoard(self):
        while True:
            # break when comparison failed in not crush
            # RANDOMIZE EMPTY SPACES when a crush is successful
            # candies = ["candy", "candy2", "candy3", "candy4", "candy5", "candy6"]

            candies = self.candyNameArray

            for x in range(len(self.board)):
                for y in range(len(self.board[x])):
                    if self.board[x][y] == "--":
                        self.board[x][y] = random.choice(candies)
            # COMPARE motion
            crush = set()
            # go through different rows
            for i in range(len(self.board)):
                # across the column
                for j in range(len(self.board[0])):
                    # added to crush when 3+ candies same
                    if i > 1 and self.board[i][j] != "--" and self.board[i][j] == self.board[i - 1][j] == \
                            self.board[i - 2][j]:
                        # checks in three at a time, re-defines crush with unique values
                        crush |= {(i, j), (i - 1, j), (i - 2, j)}
                    if j > 1 and self.board[i][j] != "--" and self.board[i][j] == self.board[i][j - 1] == self.board[i][
                        j - 2]:
                        crush |= {(i, j), (i, j - 1), (i, j - 2)}
            # CRUSH the candies
            if not crush:
                break
            # crushed candies exist
            for i, j in crush:
                self.board[i][j] = "--"

            # DROP, first going through the rows
            for j in range(len(self.board[0])):
                idx = len(self.board) - 1
                # moving across the vertical
                for i in reversed(range(len(self.board))):
                    # if this cell is candy, then change to new candy image and reduce idx by 1
                    if self.board[i][j] != "--":
                        self.board[idx][j] = self.board[i][j]
                        idx -= 1
                for i in range(idx + 1):
                    self.board[i][j] = "--"
        return self.board

    #suggested by Pranith not sure how to incorporate
    def checkCompletionCriteria(self):
        #if True: self.displayEndingScreen else: return False
        #pass in dictionary of candy crushed
        #pass
        for (key, value) in self.criteria.items():
            if value > 0:
                return False
        return True