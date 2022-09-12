import random
class GameState():
    def __init__(self):
        self.board = [
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["candy", "candy2", "candy3", "candy4", "candy5", "candy6", "candy", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"]]

        #self.whiteToMove = True
        #self.moveLog = []

    def randomizeBoard(self):
        candies = ["candy", "candy2", "candy3", "candy4", "candy5", "candy6"]
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == "--":
                    self.board[x][y] = random.choice(candies)
        return self.board

    #print(randomizeBoard(board))

    def checkBoard(self):
        while True:
        #break when comparison failed in not crush
            #RANDOMIZE EMPTY SPACES when a crush is successful
            candies = ["candy", "candy2", "candy3", "candy4", "candy5", "candy6"]
            for x in range(len(self.board)):
                for y in range(len(self.board[x])):
                    if self.board[x][y] == "--":
                        self.board[x][y] = random.choice(candies)
            #COMPARE motion
            crush = set()
            #go through different rows
            for i in range(len(self.board)):
                #across the column
                for j in range(len(self.board[0])):
                    #added to crush when 3+ candies same
                    if i>1 and self.board[i][j] != "--" and self.board[i][j]==self.board[i-1][j]==self.board[i-2][j]:
                        #checks in three at a time, re-defines crush with unique values
                        crush |= {(i, j), (i-1, j), (i-2, j)}
                    if j > 1 and self.board[i][j] != "--" and self.board[i][j] == self.board[i][j-1] == self.board[i][j-2]:
                        crush |= {(i, j), (i, j-1), (i, j-2)}
            #CRUSH the candies
            if not crush:
                break
            #crushed candies exist
            for i,j in crush:
                self.board[i][j] = "--"

            #DROP, first going through the rows
            for j in range(len(self.board[0])):
                idx = len(self.board)-1
                #moving across the vertical
                for i in reversed(range(len(self.board))):
                    #if this cell is candy, then change to new candy image and reduce idx by 1
                    if self.board[i][j] != "--":
                        self.board[idx][j]=self.board[i][j]
                        idx -= 1
                for i in range(idx+1):
                    self.board[i][j] = "--"
        return self.board

    def makeMove(self, move):

        #if self.board[move.startRow][move.startColumn] == "--":  # clicking on a candy piece
        if self.board[move.startRow][move.startColumn] != "--": #clicking on a candy piece
            #self.board[move.startRow][move.startColumn] = "--"
            #swapped location of start candy coord with end, and end candy coord with start
            self.board[move.startRow][move.startColumn] = move.pieceCaptured
            self.board[move.endRow][move.endColumn] = move.pieceMoved

        #not included log and player turns

    # def getValidMoves(self):
    #     return self.getAllPossibleMoves
    #
    # def getAllPossibleMoves(self):
    #     moves = []
    #     for r in range(len(self.board)): #number of rows
    #         for c in range (len(self.board[r])): #number of cols in given row
    #             color = self.board[r][c][0] #access the first char of the board's element "c-andy"
    #             if color == 'c': #example of candy color
    #                 self.getCandyMoves(r,c,moves)
    #     return moves
    #
    # def getCandyMoves(self, r,c,moves):
    #     pass

class Move():
    def __init__(self, startSq, endSq, board): #validate later
        self.startRow = startSq[0]
        self.startColumn = startSq[1]

        self.endRow = endSq[0]
        self.endColumn = endSq[1]

        self.pieceMoved = board[self.startRow][self.startColumn]
        self.pieceCaptured = board[self.endRow][self.endColumn]

