import pygame



from src.GameViewFactory import GameView


class GameEngine:

    resolution = None
    screen = None

    def __init__(self, resolutionP, fpsP=60, debug="True"):
        GameEngine.resolution = resolutionP
        GameEngine.fps = fpsP
        self.screen = None

    def mainLoop(self):
        self.screen = self.__initialize_display()
        #add the main menu -> ("Regular" , 1)
        curGameView = GameView("Regular", 1, self.screen)
        curGameView.runGame()
        # (isSuccess, score) = curGameView.


    def __initialize_display(self):
        """Creating the main pygame display.
        Update this to contain all base configuration for the visual
        :return: no return value
        """
        pygame.init()
        screen = pygame.display.set_mode(GameEngine.resolution)
        clock = pygame.time.Clock()
        pygame.display.set_caption("Demo Test")
        screen.fill(pygame.Color("blue"))
        return screen











    # def start(self):
    #     """Main loop for the whole game.
    #     :return: nothing
    #     """
    #     self.__initialize_display()
    #     self.__mainMenuObj.run()
    #
    #     #waiting for user to select a level...
    #     (GameEngine.selected_Level_Type, GameEngine.selected_Level_Num) = \
    #         GameEngine.__UserInputObj.getInput("main_menu")
    #
    #     #Running the level:
    #     # GameEngine.__gameViewObj = GameViewFactory.generateGameView()

