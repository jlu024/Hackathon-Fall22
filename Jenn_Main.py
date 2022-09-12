import time

import pygame as p
import DemoEngine
import random

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION //2
MAX_FPS = 15
IMAGES = {}

"""Load images"""
def loadImages():
    pieces = ['candy','candy2', 'candy3', 'candy4', 'candy5', 'candy6']

    #Mapping each candy piece with its data path graphics path value
    for piece in pieces:
        #r_image = random.choice(pieces)
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
        #IMAGES[piece] = p.transform.scale(p.image.load("images/" + r_image + ".png"), (SQ_SIZE, SQ_SIZE))

def main():

    p.init()
    screen = p.display.set_mode([WIDTH, HEIGHT])
    clock = p.time.Clock()
    p.display.set_caption("Demo Test")
    screen.fill(p.Color("blue"))
    gs = DemoEngine.GameState()
    gs.board = gs.randomizeBoard() #arrange the data in board to match image path

    #update = gs.checkBoard()

    #sol = DemoEngine.Solution()
    #sol.candyCrush()

    #validMoves = gs.getValidMoves() #once made move check if valid
    #moveMade = False #check when move actually made

    loadImages()
    #drawGameState(screen, update)
    #time.sleep(5000)

    running = True
    sqSelected = () #track last click of the user (row, col)
    playerClicks = [] #tracks player clicks [(row1,col1)(row2,col2)]
    while running:

        # GAME EVENTS
        for event in p.event.get():
            # Default event.type to exit game by closing window
            if event.type == p.QUIT:
                running = False

            elif event.type == p.MOUSEBUTTONDOWN:
                if event.button == 1:  # ensures only right click
                    location = p.mouse.get_pos() #x,y coordinate get integers
                    #truncate the location coordinate as integers
                    col = location[0] // SQ_SIZE
                    row = location[1] // SQ_SIZE
                    print(location)  # test to see mouse click coordinates
                    print (row,col)

                    if sqSelected == (row, col): #deselect motion reclick on it
                        sqSelected = ()
                        playerClicks = []

                    else:
                        sqSelected = (row, col)
                        playerClicks.append(sqSelected) #keep record of clicks

                    if len(playerClicks) == 2:
                        #engine move the first piece, to second piece location on board
                        #second piece gets nonexistant
                        #move = DemoEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                        move = DemoEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                        #if move in validMoves:
                        gs.makeMove(move)
                        #moveMade = True
                        #resetting the first move
                        sqSelected = ()
                        playerClicks = []

        # if moveMade:
        #     validMoves = gs.getValidMoves()
        #     moveMade = False #reset move made flag

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


"""Graphics to surface game state"""
def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

"""Draw squares on board, good initial background"""
def drawBoard(screen):
    colors = [p.Color("gray"), p.Color("red")]
    for r in range (DIMENSION):
        for c in range (DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

"""Interaction of Engine and actual screen in drawing/placing images to game state"""
def drawPieces(screen, board):
    for r in range (DIMENSION):
        for c in range (DIMENSION):
            #access the string in each board tile
            piece = board[r][c]
            if piece != "--":
            #if piece == "--":
                #That manipulated pixel area, manifest its image represenation to screen
                #testing = IMAGES[piece]
                #testing = random.choice(list(IMAGES.values()))
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                #screen.blit(random.choice(list(IMAGES_TEST.values())), p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

                #screen.blit((testing), p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()

