
class GameState():
    def __init__(self):
        self.board = [
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "candy", "candy2", "candy", "candy", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"]]
            # ["candy", "candy2", "candy", "candy2", "candy", "candy", "candy2", "candy"],
            # ["candy", "candy2", "candy", "candy2", "candy", "candy", "candy2", "candy"],
            # ["candy", "candy2", "candy", "candy2", "candy", "candy", "candy2", "candy"],
            # ["candy", "candy2", "candy", "candy2", "candy", "candy", "candy2", "candy"],
            # ["candy", "candy2", "candy", "candy2", "candy", "candy", "candy2", "candy"],
            # ["candy", "candy2", "candy", "candy2", "candy", "candy", "candy2", "candy"],
            # ["candy", "candy2", "candy", "candy2", "candy", "candy", "candy2", "candy"],
            # ["candy", "candy2", "candy", "candy2", "candy", "candy", "candy2", "candy"]]

        #self.whiteToMove = True
        #self.moveLog = []

    def makeMove(self, move):

        #if self.board[move.startRow][move.startColumn] == "--":  # clicking on a candy piece
        if self.board[move.startRow][move.startColumn] != "--": #clicking on a candy piece
            #self.board[move.startRow][move.startColumn] = "--"
            #swapped location of start candy coord with end, and end candy coord with start
            self.board[move.startRow][move.startColumn] = move.pieceCaptured
            self.board[move.endRow][move.endColumn] = move.pieceMoved

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
